"""
Kentucky Child Support calculator
See: https://www.ardfky.org/sites/ardfky.org/files/Child%20Support%20Worksheet%20CS71.pdf
Effective March 31, 2023, KRS 403.2121
"""
from worksheet import SSRTable, TimeAdjustment


class IncomePeriod:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def to_monthly(self, income):
        return income * self.unit / 12


incomePeriods = [
    IncomePeriod("unknown", 0),
    IncomePeriod("weekly", 52),
    IncomePeriod("monthly", 12),
    IncomePeriod("annually", 1),
]


def get_income_period_opts():
    return {
        index: period.name for (index, period)
        in enumerate(incomePeriods)
        if period.unit > 0
    }


class Parent:
    def __init__(self, name="", days=0, income=0, care_expense=0, insurance=0, maintenance=0,
                 other_support=0):
        self.name = name
        self.days = days
        self.care_expense = care_expense
        self.income = income
        self.insurance = insurance
        self.maintenance = maintenance
        self.other_support = other_support
        self.adjusted_income = income - maintenance - other_support
        self.perc = None
        self.ssr = False
        self.isA = False
        self._income_val = 0
        self._income_period = 0

    def __repr__(self):
        letter = "A" if self.isA else "B"
        return f"{self.name} ({letter})"

    def calc_income(self):
        period = incomePeriods[self._income_period or 0]
        self.income = period.to_monthly(self._income_val)

    @property
    def income_val(self):
        return self._income_val

    @income_val.setter
    def income_val(self, income_val):
        self._income_val = income_val
        self.calc_income()

    @property
    def income_period(self):
        return self._income_period

    @income_period.setter
    def income_period(self, period):
        self._income_period = period
        self.calc_income()

    def recalc(self):
        self.adjusted_income = self.income - self.maintenance - self.other_support
        self.perc = None
        self.ssr = False
        self.isA = False

    def calc_percent(self, combined):
        self.perc = 0
        if combined > 0:
            self.perc = self.adjusted_income / combined

    def check_ssr(self):
        table = SSRTable()
        self.ssr = table.for_value(self.adjusted_income)
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
