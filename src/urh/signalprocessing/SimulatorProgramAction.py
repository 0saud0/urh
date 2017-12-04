from urh.signalprocessing.SimulatorItem import SimulatorItem
from urh.signalprocessing.SimulatorRule import SimulatorRuleCondition

class SimulatorProgramAction(SimulatorItem):
    def __init__(self):
        super().__init__()
        self.ext_prog = None
        self.args = None

    def set_parent(self, value):
        if value is not None:
            assert value.parent() is None or isinstance(value, SimulatorRuleCondition)

        super().set_parent(value)