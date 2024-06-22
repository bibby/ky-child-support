from nicegui import ui
import sys

from lib import Parent, Worksheet, State


def cli():
    # your mileage may vary
    others_days = 52
    children = 3

    if len(sys.argv) > 1:
        others_days = float(sys.argv[1])
    if len(sys.argv) > 2:
        children = int(sys.argv[2])

    her_days = others_days
    his_days = 365 - her_days

    her = Parent(
        "HerName",
        her_days,
        15 * 40 * 52 / 12,
        care_expense=0,
        insurance=0
    )

    him = Parent(
        "HisName",
        his_days,
        110 * 1000 / 12,
        care_expense=0,  # 20 * 3 * 2 * 4,
        insurance=335
    )

    worksheet = Worksheet(children, him, her)
    print("\n")
    worksheet.calc_support()
    print("\n")
    worksheet.print()


def gui():
    state = State()
    state.calc()
    ui.dark_mode().enable()

    def calc():
        state.calc()
        draw_table.refresh()

    def even_days():
        for p in state.parents:
            p.days = 182.5

    @ui.refreshable
    def draw_table():
        with ui.grid(columns=4).classes('gap-0'):
            def cell(label=None, classes=[], method='label', bind=None):
                label = label or ""
                classes = ['border', 'px-2', 'py-0'] + classes
                elm = getattr(ui, method)(label).classes(" ".join(classes))
                if bind:
                    elm.bind_text_from(*bind)
                return elm

            def head(label, classes=[]):
                return cell(label, ["font-bold"] + classes)

            head("#")
            head("A")
            head("B")
            head("C")

            cell("Name")
            cell(state.worksheet.A.name, bind=(state.worksheet.A, "name"))
            cell(state.worksheet.B.name, bind=(state.worksheet.B, "name"))
            cell()

            for line_num in sorted(state.worksheet.lines.keys()):
                label = [line_num]
                line = state.worksheet.get_line(line_num)
                if line.checks:
                    for check_name, check in line.checks.items():
                        label.append(check_name + ": " + str(check))

                cell("<br />".join(map(str, label)), method='html')

                cell(line.a)
                cell(line.b)
                cell(line.c)
        ui.label(state.worksheet.final).classes("font-bold")

    with ui.row():
        with ui.column():
            with ui.row():
                ui.label("Children")
                ui.label().bind_text_from(state, "children")
            ui.slider(min=1, max=6, on_change=calc).bind_value(state, "children")

            with ui.row():
                for parent in state.worksheet.parents:
                    with ui.column():
                        ui.input("Name", on_change=calc).bind_value(parent, "name")
                        ui.number("Income", on_change=calc).bind_value(parent, "income")

                        with ui.row():
                            ui.label("Custodial Days")
                            ui.button("Equal", on_click=even_days)
                        ui.slider(
                            min=0,
                            max=365,
                            step=0.5,
                            on_change=state.mk_reflect(state, parent, calc)
                        ).bind_value(parent, "days")

                        ui.number("Child Care Expenses", on_change=calc).bind_value(parent, "care_expense")
                        ui.number("Insurance", on_change=calc).bind_value(parent, "insurance")
                        ui.number("Spousal Maintenance", on_change=calc).bind_value(parent, "maintenance")
                        ui.number("Other Child Support", on_change=calc).bind_value(parent, "other_support")

            ui.button('Calculate', on_click=calc)
        with ui.column():
            draw_table()

    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    gui()
    # cli()
