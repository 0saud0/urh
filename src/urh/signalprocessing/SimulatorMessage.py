from urh.signalprocessing.SimulatorItem import SimulatorItem
from urh.signalprocessing.SimulatorRule import SimulatorRule, SimulatorRuleCondition
from urh.signalprocessing.Message import Message
from urh.signalprocessing.MessageType import MessageType

class SimulatorMessage(Message, SimulatorItem):
    def __init__(self, destination, plain_bits, pause: int, message_type: MessageType, decoder=None, source=None):
        Message.__init__(self, plain_bits, pause, message_type, decoder=decoder, participant=source)
        SimulatorItem.__init__(self)
        self.destination = destination
        self.received_messages = []

    def set_parent(self, value):
        if value is not None:
            assert value.parent() is None or isinstance(value, SimulatorRuleCondition)

        super().set_parent(value)

    @property
    def children(self):
        return self.message_type

    def insert_child(self, pos, child):
        self.children.append(child)
        child.set_parent(self)

    def check(self):
        return all(child.is_valid for child in self.children)