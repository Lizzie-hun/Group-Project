import arcade
from director import Director
import globals
from level import Level
from gates import Gates

def main():
    # window = Director(globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH, "Running Game")
    # arcade.run()
    level = Level(5)
    level.create_gates()
    for gate in level.get_gates():
        print(gate.get_gate())

main()