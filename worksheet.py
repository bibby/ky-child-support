import re

from fmt import to_double
from printer import WorksheetPrinter
from tables import MIN_SPA_DAYS, SSR_TABLE, GUIDELINES, TIME_ADJUSTMENT


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
        self.children = min(children, 6)
        self.parents = parents[:2]
        self.lines = dict()
        self.shared_parenting = None
        self.ssr = None
        self.A = parents[0]
        self.B = parents[1]
        self.final = ""

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
        X.recalc()
        Y.recalc()
        if X.days == Y.days:
            (A, B) = sorted([X, Y], key=lambda p: p.income)
        else:
            (A, B) = sorted([X, Y], key=lambda p: p.days, reverse=True)

        self.A = A
        self.B = B

        A.isA = True
        B.isA = False

        self.add_line(WorksheetLine(1, a=A.income, b=B.income))
        self.add_line(WorksheetLine(2, a=A.maintenance, b=B.maintenance))
        self.add_line(WorksheetLine(3, a=A.other_support, b=B.other_support))
        self.add_line(WorksheetLine(4, a=A.adjusted_income, b=B.adjusted_income))

        combined_income = A.adjusted_income + B.adjusted_income
        self.add_line(WorksheetLine(5, c=combined_income))

        A.calc_percent(combined_income)
        B.calc_percent(combined_income)

        self.add_line(WorksheetLine(6, a=A.perc * 100, b=B.perc * 100, percent=True))

        self.ssr = B.check_ssr()

        # 7c
        if self.ssr:
            obligation = self.ssr.for_children(self.children)
        else:
            guidelines = ObligationGuidelines()
            item = guidelines.for_value(value=combined_income)
            obligation = item.for_children(self.children)

        self.shared_parenting = B.days >= MIN_SPA_DAYS

        self.add_line(
            WorksheetLine(
                7,
                c=obligation,
                checks=dict(
                    ssr=self.ssr is not None,
                    shared_parenting=self.shared_parenting
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
                a=self.get_val("10C") * self.get_val("6A") / 100,
                b=self.get_val("10C") * self.get_val("6B") / 100,
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

        if not self.shared_parenting:
            self.finalize(self.get_val("12B"), A, B)
            return self

        ta = TimeAdjustment()
        adjustment_item = ta.for_value(B.days)
        adjustment = adjustment_item.at_index(0)

        self.add_line(
            WorksheetLine(
                14,
                b=adjustment,
                percent=True
            )
        )

        self.add_line(
            WorksheetLine(
                15,
                b=self.get_val("7C") * adjustment / 100
            )
        )

        self.add_line(
            WorksheetLine(
                16,
                b=self.get_val("12B") - self.get_val("15B")
            )
        )

        self.finalize(self.get_val("16B"), A, B)
        return self

    def finalize(self, support, A, B):
        (payer, pays) = (B, A) if support > 0 else (A, B)
        support = abs(support)
        self.final = f"{payer} pays ${support:.2f} to {pays}"

    def print(self):
        WorksheetPrinter.print(self)

    @property
    def ready(self):
        return sum([p.income_val for p in self.parents]) > 0


class WorksheetLine:
    def __init__(self, num, a=None, b=None, c=None, checks=None, percent=False):
        # columns
        self.num = num
        self.a = to_double(a)
        self.b = to_double(b)
        self.c = to_double(c)
        self.checks = checks
        self.is_percent = percent

    def __repr__(self):
        return str(self.num)

    def get_a(self):
        if self.a and self.is_percent:
            return f"{self.a * 100:0.2f}%"
        return self.a

    def get_b(self):
        if self.b and self.is_percent:
            return f"{self.b * 100:0.2f}%"
        return self.b


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


class TimeAdjustment(Table):
    def __init__(self):
        super(TimeAdjustment, self).__init__()
        self.build(TIME_ADJUSTMENT)
