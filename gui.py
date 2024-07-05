from nicegui import ui

from gui_state import State
from help_text import help_text
from parent import get_income_period_opts
from tables import YEAR_DAYS
from worksheet import TimeAdjustment, LineItem


def gui():
    state = State()
    state.calc()
    ui.dark_mode().enable()

    def calc():
        state.calc()
        draw_table.refresh()
        draw_lookups.refresh()

    def even_days():
        for p in state.parents:
            p.days = YEAR_DAYS / 2

    def draw_controls():
        with ui.row():
            ui.label("Children")
            ui.label().bind_text_from(state, "children")
        ui.slider(min=1, max=6, on_change=calc).bind_value(state, "children")

        with ui.row():
            for parent in state.worksheet.parents:
                with ui.column():
                    ui.input("Name", on_change=calc).bind_value(parent, "name")
                    ui.number("Income", on_change=calc, step=100).bind_value(parent, "income_val")
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

    def cell(label=None, classes=[], method='label', bind=None, mouseenter=None, mouseleave=None, percent=None):
        label = str(label or "")
        if percent and label:
            label += "%"
        classes = ['border', 'px-2', 'py-0'] + classes
        elm = getattr(ui, method)(label).classes(" ".join(classes))
        if bind:
            elm.bind_text_from(*bind)
        if mouseenter:
            elm.on('mouseenter', mouseenter)
        if mouseleave:
            elm.on('mouseleave', mouseleave)
        return elm

    def head(label, classes=[], **kwargs):
        return cell(label, ["font-bold"] + classes, **kwargs)

    @ui.refreshable
    def draw_table():
        with ui.grid(columns=4).classes('gap-0'):
            head("#", **show_help('header'))
            head("A", **show_help('header'))
            head("B", **show_help('header'))
            head("C", **show_help('header'))

            cell("Name", **show_help('name'))
            cell(state.worksheet.A.name, bind=(state.worksheet.A, "name"), **show_help('name'))
            cell(state.worksheet.B.name, bind=(state.worksheet.B, "name"), **show_help('name'))
            cell(**show_help('name'))

            for line_num in sorted(state.worksheet.lines.keys()):
                label = [line_num]
                line = state.worksheet.get_line(line_num)
                if line.checks:
                    for check_name, check in line.checks.items():
                        label.append(check_name + ": " + str(check))

                topic = f'line{line_num}'
                cell("<br />".join(map(str, label)), method='html', **show_help(topic))

                draw_data(line, **show_help(topic))

        if state.worksheet and state.worksheet.ready:
            ui.label(state.worksheet.final).classes("font-bold")
            ui.button(
                "Draw Chart",
                on_click=lambda e: draw_chart.refresh()
            )

    def draw_data(line, **kwargs):
        cell(line.a, percent=line.is_percent, **kwargs)
        cell(line.b, percent=line.is_percent, **kwargs)
        cell(line.c, percent=line.is_percent, **kwargs)

    @ui.refreshable
    def draw_help():
        ui.markdown(state.help or "")

    def set_help(help_content):
        if state.set_help(help_content):
            draw_help.refresh()

    def show_help(topic):
        return dict(
            mouseenter=lambda: set_help(help_text[topic]),
            mouseleave=lambda: set_help(None),
        )

    @ui.refreshable
    def draw_chart():
        ui.echart({
            'xAxis': {'type': 'category'},
            'yAxis': {'axisLabel': {':formatter': 'value => "$" + value'}},
            'series': [{'type': 'line', 'data': state.worksheet.sim()}],
        })

    @ui.refreshable
    def draw_lookups():
        if not state.worksheet.ready:
            return

        with ui.column():
            if state.worksheet.ssr:
                obligation_label = "Obligation with SSR [KRS 403.212(5)(b)]"
                line = state.worksheet.ssr
            else:
                obligation_label = "Obligation from Guidelines [KRS 403.212(9)]"
                line = state.worksheet.guideline

            ui.label(obligation_label)
            ui.markdown(line.to_markdown(LineItem.markdown_headers()), extras=['tables'])

            spa_label = "Shared Parenting Adjustment"
            if state.worksheet.shared_parenting:
                ui.label(spa_label)
                ui.markdown(state.worksheet.time_adjustment.to_markdown(TimeAdjustment.markdown_headers()))
            else:
                spa_label += ": None"
                ui.label(spa_label)

    with ui.grid(columns=3).classes('gap-2'):
        with ui.column():
            draw_controls()
        with ui.column():
            draw_table()
            draw_chart()
        with ui.column():
            draw_lookups()
            draw_help()
    ui.run()
