import vgamepad as vg
DAC_MAX_VALUE = 1023

class Gamepad():
    def __init__(self, externalGamepad : vg.VDS4Gamepad,
                 deadzoneRadius = 50,
                 zeroOffset = DAC_MAX_VALUE/2,
                 x_inverted = False,
                 y_iverted = False,
                 activationFunction = (lambda x : x)):
        self.externalGamepad = externalGamepad
        self.deadzoneRadius = deadzoneRadius
        self.zeroOffset = zeroOffset
        self.x_inverted = x_inverted
        self.y_inverted = y_iverted
        self.activationFunction = activationFunction

    def compute(self, decimal_value : int, is_inverted : bool):
        decimal_value -= self.zeroOffset
        decimal_value = self.activationFunction(decimal_value)
        if abs(decimal_value) < self.deadzoneRadius:
            return 0
        float_value = decimal_value / (DAC_MAX_VALUE/2)
        if is_inverted: float_value *= -1
        return float_value

    def getComputed(self, joyCord):
        return self.compute(joyCord[0], self.x_inverted), self.compute(joyCord[1], self.y_inverted)
        
        