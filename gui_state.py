from parent import Parent
from worksheet import Worksheet


class State:
    def __init__(self):
        self.children = 3
        self.parents = [
            Parent(name="Him"),
            Parent(name="Her"),
        ]
        self.worksheet = None
        self.help = None

    def calc(self):
        self.worksheet = Worksheet(self.children, *self.parents).calc_support()

    def reflect_days(self, parent, value):
        for p in self.parents:
            val = 365 - value
            if p != parent and p.days != val:
                p.days = val

        return True

    def mk_reflect(self, state, parent, callback):
        return lambda e: state.reflect_days(parent, e.value) and callback()

    def set_help(self, help_content):
        changed = self.help != help_content
        if changed:
            self.help = help_content
        return changed

