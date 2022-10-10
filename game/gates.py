# The gates that go inside of the levels.
from actor import Actor
import random

class Gates(Actor):
    def __init__(self):
        self._operation = ""
        self._right_ans = ""
        self._wrong_ans = ""

    def create_operation(self):
        num = random.randint(1, 4)
        if num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
        else:
            pass

    def create_answers(self):
        pass
