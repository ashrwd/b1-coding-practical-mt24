class Controller:
    """
    Controller: u[t] = Kp * e[t] + Kd * (e[t] - e[t-1])
    with e[t] = r[t] - y[t]
    """
    def __init__(self, Kp: float = 0.15, Kd: float = 0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0.0

    def compute(self, reference: float, output: float) -> float:
        error = reference - output
        derivative = error - self.prev_error
        u = self.Kp * error + self.Kd * derivative
        self.prev_error = error
        return u
