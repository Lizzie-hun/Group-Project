# The gates that go inside of the levels.
from actor import Actor
import random

class Gates(Actor):
    def __init__(self):
        self._wrong_ans = ""
        self._right_ans = ''
        self._operation = ''

    def get_gate(self):
        return (self._operation, self._right_ans, self._wrong_ans)

    def create_operation(self):
        # Putting together the operation, the right answer, and the wrong answer
        num = random.randint(1, 4)
        first_num = random.randint(1, 12)
        second_num = random.randint(1, 12)
        while first_num < second_num and num == 3 or not first_num % second_num == 0 and num == 3:
            first_num = random.randint(1, 12)
            second_num = random.randint(1, 12)
        
        print(not first_num % second_num == 0, first_num % second_num)

        if num == 1:
            self._operation = f"{first_num} + {second_num}"
        elif num == 2:
            self._operation = f"{first_num} - {second_num}"
        elif num == 3:
            self._operation = f"{first_num} / {second_num}"
        else:
            self._operation = f"{first_num} * {second_num}"

        self._create_answers(first_num, second_num)

    def _create_answers(self, first_num, second_num):
        operand = ''
        for i in self._operation:
            if i in ["+", "-", "/", "*"]:
                operand = i
                break
        
        if operand == '+':
            self._right_ans = f"{first_num + second_num}"
            self._wrong_ans = f"{first_num + second_num + random.randint(-10, 10)}"
        elif operand == '-':
            self._right_ans = f"{first_num - second_num}"
            self._wrong_ans = f"{(first_num - second_num) + random.randint(-10, 10)}"
        elif operand == '/':
            self._right_ans = f"{int(first_num / second_num)}"
            self._wrong_ans = f"{int((first_num / second_num)) + random.randint(-10, 10)}"
        else:
            self._right_ans = f"{first_num * second_num}"
            self._wrong_ans = f"{(first_num * second_num) + random.randint(-10, 10)}"