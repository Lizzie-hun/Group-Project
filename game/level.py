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
    
    def get_gate_num(self):
        return self._gate_num

    def set_gate_num(self, gates):
        self._gate_num = gates

    def get_gates(self):
        return self._gates_list

    def set_gates(self, list):
        self._gates_list = list

    def create_gates(self):
        # This creates the gates based off of the difficulty input into level
        for i in range(self._gate_num ):
            # This creates an instance of the Gate and then appends it to the gate list
            level_gate = Gates()
            level_gate.create_operation()
            self._gates_list.append(level_gate)
