import re
from tables import TIME_ADJUSTMENT, SSR_TABLE, GUIDELINES, MIN_SPA_DAYS

"""
Kentucky Child Support calculator
See: https://www.ardfky.org/sites/ardfky.org/files/Child%20Support%20Worksheet%20CS71.pdf
Effective March 31, 2023, KRS 403.2121
"""


class Parent:
    def __init__(self, name, days, income, care_expense=0, insurance=0, maintenance=0, other_support=0):
        self.name = name
        self.days = days
        self.income = income
        self.care_expense = care_expense
        self.insurance = insurance
        self.maintenance = maintenance
        self.other_support = other_support
        self.adjusted_income = income - maintenance - other_support
        self.perc = None
        self.ssr = False
        self.isA = False

    def __repr__(self):
        letter = "A" if self.isA else "B"
        return f"{self.name} ({letter})"

    def calc_percent(self, combined):
        self.perc = self.adjusted_income / combined

    def check_ssr(self):
        table = SSRTable()
        ssr = table.for_value(self.adjusted_income)
        if ssr:
            self.ssr = True
        return self.ssr

    def calc_obligation(self, obligation, adjust=False):
        # 11
        share = obligation * self.perc

        # 12
        share -= self.care_expense
        share -= self.insurance

        #
        if adjust:
            # 13
            ta = TimeAdjustment()
            adjustment = ta.for_value(self.days)
            if adjustment:
                # 14
                v = adjustment.at_index(0) / 100
                # 15
                adjust = obligation * v
                # 16
                share -= adjust

        return share


class Table:
    def __init__(self):
        self.items = []
        self.sorted = False
        self.reversed = False

    def build(self, data):
        data = data.replace(",", "")
        data = data.replace("$", "")
        for line in data.split("\n"):
            self.add_line(line.strip())
        self.sort()

    def add_line(self, line):
        self.add(LineItem.parse(line))

    def add(self, ssr):
        self.items.append(ssr)
        self.sorted = False

    def for_value(self, value):
        self.sort()
        last = None
        for item in self.items:
            if self.reversed:
                if value > item.value:
                    continue
                return item
            else:
                if value >= item.value:
                    return last or item
                last = item

    def sort(self):
        if self.sorted:
            return

        self.items = sorted(self.items, key=lambda ssr: ssr.value, reverse=True)
        self.sorted = True


class SSRTable(Table):
    """self-support reserve """

    def __init__(self):
        super(SSRTable, self).__init__()
        self.reversed = True
        self.build(SSR_TABLE)


class ObligationGuidelines(Table):
    def __init__(self):
        super(ObligationGuidelines, self).__init__()
        self.build(GUIDELINES)


class LineItem:
    def __init__(self, value, *table):
        self.value = value
        self.table = table

    def __repr__(self):
        return str(self.value)

    @staticmethod
    def parse(line):
        parts = list(map(float, line.split(" ")))
        return LineItem(parts[0], *parts[1:])

    def for_children(self, children):
        return self.at_index(children - 1)

    def at_index(self, index):
        return self.table[index]


class Worksheet:
    def __init__(self, children, *parents):
        self.children = children
        self.parents = parents
        self.lines = dict()

    def add_line(self, line):
        self.lines[line.num] = line

    def get_lines(self):
        return sorted(self.lines.values(), key=lambda l: int(l.num))

    def get_val(self, item):
        num = int(re.search("^\d+", item)[0])
        col = str(re.search("[^\d]*$", item)[0]).lower()
        try:
            line = self.get_line(num)
        except IndexError:
            return 0
        return getattr(line, col, 0)

    def get_line(self, num):
        return self.lines.get(num)

    def calc_support(self):
        (X, Y) = self.parents
        if X.days == Y.days:
            (A, B) = sorted([X, Y], key=lambda p: p.income)
        else:
            (A, B) = sorted([X, Y], key=lambda p: p.days, reverse=True)

        A.isA = True
        self.add_line(WorksheetLine(1, a=A.income, b=B.income))
        self.add_line(WorksheetLine(2, a=A.maintenance, b=B.maintenance))
        self.add_line(WorksheetLine(3, a=A.other_support, b=B.other_support))
        self.add_line(WorksheetLine(4, a=A.adjusted_income, b=B.adjusted_income))

        combined_income = A.adjusted_income + B.adjusted_income
        self.add_line(WorksheetLine(5, c=combined_income))

        A.calc_percent(combined_income)
        B.calc_percent(combined_income)

        self.add_line(WorksheetLine(6, a=A.perc, b=B.perc, percent=True))

        ssr = B.check_ssr()

        # 7c
        if ssr:
            obligation = ssr.for_children(self.children)
        else:
            guidelines = ObligationGuidelines()
            item = guidelines.for_value(value=combined_income)
            obligation = item.for_children(self.children)

        shared_parenting = B.days >= MIN_SPA_DAYS

        self.add_line(
            WorksheetLine(
                7,
                c=obligation,
                checks=dict(
                    ssr=ssr is not None,
                    shared_parenting=shared_parenting
                )
            )
        )

        self.add_line(
            WorksheetLine(
                8,
                a=A.care_expense,
                b=B.care_expense,
                c=A.care_expense + B.care_expense
            )
        )

        self.add_line(
            WorksheetLine(
                9,
                a=A.insurance,
                b=B.insurance,
                c=A.insurance + B.insurance
            )
        )

        self.add_line(
            WorksheetLine(
                10,
                c=self.get_val("7C") + self.get_val("8C") + self.get_val("9C")
            )
        )

        self.add_line(
            WorksheetLine(
                11,
                a=self.get_val("10C") * self.get_val("6A"),
                b=self.get_val("10C") * self.get_val("6B"),
            )
        )

        self.add_line(
            WorksheetLine(
                12,
                a=self.get_val("11A") - A.care_expense - B.insurance,
                b=self.get_val("11B") - B.care_expense - B.insurance,
            )
        )

        self.add_line(
            WorksheetLine(
                13,
                a=A.days,
                b=B.days
            )
        )

        if not shared_parenting:
            return self.finalize(self.get_val("12B"), A, B)

        ta = TimeAdjustment()
        adjustment_item = ta.for_value(B.days)
        adjustment = adjustment_item.at_index(0) / 100

        self.add_line(
            WorksheetLine(
                14,
                b=adjustment
            )
        )

        self.add_line(
            WorksheetLine(
                15,
                b=self.get_val("7C") * adjustment
            )
        )

        self.add_line(
            WorksheetLine(
                16,
                b=self.get_val("12B") - self.get_val("15B")
            )
        )

        self.finalize(self.get_val("16B"), A, B)

    @staticmethod
    def finalize(support, A, B):
        (payer, pays) = (B, A) if support > 0 else (A, B)
        support = abs(support)
        print(f"{payer} pays ${support:.2f} to {pays}")

    def print(self):
        WorksheetPrinter.print(self)


class WorksheetLine:
    def __init__(self, num, a=None, b=None, c=None, checks=None, percent=False):
        # columns
        self.num = num
        self.a = a
        self.b = b
        self.c = c
        self.checks = checks
        self.is_percent = percent

    def __repr__(self):
        return str(self.num)

    def get_a(self):
        if self.is_percent:
            return f"{self.a*100:0.2f}%"
        return self.a

    def get_b(self):
        if self.is_percent:
            return f"{self.b*100:0.2f}%"
        return self.b


class TimeAdjustment(Table):
    def __init__(self):
        super(TimeAdjustment, self).__init__()
        self.build(TIME_ADJUSTMENT)


class WorksheetPrinter:
    COL_WIDTH = 8

    @staticmethod
    def print(worksheet: Worksheet):
        WorksheetPrinter.print_header()
        for line in worksheet.get_lines():
            WorksheetPrinter.print_line(line)
        WorksheetPrinter.print_footer()

    @staticmethod
    def print_line(line: WorksheetLine):
        WorksheetPrinter.out(
            WorksheetPrinter.fmt_line(
                [
                    line.num,
                    line.get_a(),
                    line.get_b(),
                    line.c
                ]
            )
        )

    @staticmethod
    def fmt_line(fields, sep="|"):
        return sep.join(
            list(
                map(
                    WorksheetPrinter.fixed_width,
                    fields
                )
            )
        )

    @staticmethod
    def fixed_width(val):
        s = " " * WorksheetPrinter.COL_WIDTH
        s += WorksheetPrinter.fmt_val(val)
        return s[-WorksheetPrinter.COL_WIDTH:]

    @staticmethod
    def fmt_val(val):
        if val is None:
            return ""
        if isinstance(val, float):
            return f"{val:,.0f}"
        return str(val)

    @staticmethod
    def out(inner, border="|"):
        print(f"{border}{inner}{border}")

    @staticmethod
    def print_header():
        WorksheetPrinter.out(WorksheetPrinter.fmt_line([
            "Number",
            "A",
            "B",
            "C"
        ]))

        WorksheetPrinter.out(
            WorksheetPrinter.fmt_line(
                ["=" * WorksheetPrinter.COL_WIDTH] * 4
            )
        )

    @staticmethod
    def print_footer():
        WorksheetPrinter.out(
            WorksheetPrinter.fmt_line(
                ["-" * WorksheetPrinter.COL_WIDTH] * 4,
                sep="-"
            ),
            border="+"
        )
