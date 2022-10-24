# The gates that go inside of the levels.
from distutils.command.build_scripts import first_line_re
from game.actor import Actor
import random

class Gates(Actor):
    def __init__(self):
        self._wrong_ans = ""

    def create_operation(self):
        # Putting together the operation, the right answer, and the wrong answer
        num = random.randint(1, 4)
        first_num = random.randint(1, 12)
        second_num = random.randint(1, 12)
        if num == 1:
            self._operation = f"{first_num} + {second_num}"
            self._right_ans = f"{first_num + second_num}"
            self._wrong_ans = f"{first_num + second_num + random.randint(-10, 10)}"
        elif num == 2:
            self._operation = f"{first_num} - {second_num}"
            self._right_ans = f"{first_num - second_num}"
            self._wrong_ans = f"{(first_num - second_num) + random.randint(-10, 10)}"
        elif num == 3:
            self._operation = f"{first_num} / {second_num}"
            self._right_ans = f"{first_num / second_num}"
            self._wrong_ans = f"{(first_num / second_num) + random.randint(-10, 10)}"
        else:
            self._operation = f"{first_num} * {second_num}"
            self._right_ans = f"{first_num * second_num}"
            self._wrong_ans = f"{(first_num * second_num) + random.randint(-10, 10)}"

    def create_answers(self, operation, first_num, second_num):
        pass