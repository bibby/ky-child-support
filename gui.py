from nicegui import ui

from gui_state import State
from parent import incomePeriods, get_income_period_opts
from tables import YEAR_DAYS


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

        if state.worksheet and state.worksheet.ready:
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
                        ui.number("Income", on_change=calc).bind_value(parent, "income_val")
                        ui.toggle(get_income_period_opts(), on_change=calc).bind_value(parent, "income_period")

                        ui.label("Custodial Days")
                        day_opts = dict(
                            min=0,
                            max=YEAR_DAYS,
                            step=0.5,
                            on_change=state.mk_reflect(state, parent, calc)
                        )
                        ui.slider(**day_opts).bind_value(parent, "days")
                        with ui.row():
                            ui.number("Custodial Days", **day_opts).bind_value(parent, "days")
                            ui.button("Equalize", on_click=even_days).classes("p-0.5 py-0 leading-0")

                        ui.number("Child Care Expenses", on_change=calc).bind_value(parent, "care_expense")
                        ui.number("Insurance", on_change=calc).bind_value(parent, "insurance")
                        ui.number("Spousal Maintenance", on_change=calc).bind_value(parent, "maintenance")
                        ui.number("Other Child Support", on_change=calc).bind_value(parent, "other_support")
        with ui.column():
            draw_table()

    ui.run()
