class WorksheetPrinter:
    COL_WIDTH = 8

    @staticmethod
    def print(worksheet):
        print(worksheet.final)
        WorksheetPrinter.print_header()
        for line in worksheet.get_lines():
            WorksheetPrinter.print_line(line)
        WorksheetPrinter.print_checks(worksheet)
        WorksheetPrinter.print_footer()

    @staticmethod
    def print_line(line):
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
    def fmt_line(fields, sep="|", width=None):
        if isinstance(width, list):
            lines = []
            for i, val in enumerate(fields):
                wid = width[i]
                lines.append(WorksheetPrinter.fixed_width(val, wid))
        else:
            lines = [WorksheetPrinter.fixed_width(val, width) for val in fields]
        return sep.join(lines)

    @staticmethod
    def fixed_width(val, width=None):
        width = width or WorksheetPrinter.COL_WIDTH
        s = " " * width
        s += WorksheetPrinter.fmt_val(val)
        return s[-width:]

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
    def print_checks(worksheet):
        WorksheetPrinter.out(
            WorksheetPrinter.fmt_line(
                ["-" * WorksheetPrinter.COL_WIDTH] * 4
            )
        )

        triple = WorksheetPrinter.COL_WIDTH * 3 + 2
        WorksheetPrinter.out(WorksheetPrinter.fmt_line([
            "Shared-Parenting Adjusted",
            str(worksheet.shared_parenting)
        ], width=[triple, WorksheetPrinter.COL_WIDTH]))

        WorksheetPrinter.out(WorksheetPrinter.fmt_line([
            "Self-Support Reserve",
            str(worksheet.ssr)
        ], width=[triple, WorksheetPrinter.COL_WIDTH]))

    @staticmethod
    def print_footer():
        WorksheetPrinter.out(
            WorksheetPrinter.fmt_line(
                ["-" * WorksheetPrinter.COL_WIDTH] * 4,
                sep="-"
            ),
            border="+"
        )
