class LogicGate(object):
    ''' Implement basic characteristics of logic gate:
    - Label
    - Output line
    '''
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class UnaryGate(LogicGate):
    def __init__(self, n):
        super(UnaryGate, self).__init__(n)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input('Enter Pin input for gate %s -->' % (
                self.get_label())))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        # Connect source gate output to this gate's available pin.
        # If pin isn't available, not possible to connect to this gate.
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA is None:
            return int(input('Enter Pin A input for gate %s -->' % (
                self.get_label())))
        else:
            return self.pinA.get_from().get_output()

    def get_pinB(self):
        if self.pinB is None:
            return int(input('Enter Pin B input for gate %s -->' % (
                self.get_label())))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        # Connect source connector to first available pin.
        # If no pins are available, not possible to connect to this gate.
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def perform_gate_logic(self):
        p = self.get_pin()

        return 1 if p == 0 else 0


class Connector(object):
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate
