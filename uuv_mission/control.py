class Controller:
    def __init__(self, Kp: float = 0.15, Kd: float = 0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0.0
