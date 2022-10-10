# The parent class for all the levels
from gates import Gates


class Level:
    def __init__(self, difficulty):
        self._difficulty = difficulty
        self._speed = (1 * (difficulty/100)) + 1
        self._gate_num = difficulty
        self._gates_list = []

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed
    
    def get_gates(self):
        return self._gate_num

    def set_gates(self, gates):
        self._gate_num = gates

    def create_gates(self):
        # This creates the gates based off of the difficulty input into level
        for i in range(self._gate_num + 1):
            level_gate = Gates()
            # Add code to make the gate
            self._gates_list.append(level_gate)
