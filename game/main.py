import arcade
from director import Director
import globals
from level import Level
from gates import Gates

def main():
    """ Main function """
    # first_level = Level(1)
    # first_level.create_gates()
    # print(first_level.get_gates())

    window = Director(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, globals.SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()