# The parent class for all the levels

class Level:
    def __init__(self, difficulty):
        self._difficulty = difficulty
        self._speed = (difficulty/100) + 1
        self._gate_num = difficulty + 9
        self._gates_list = []

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed
    