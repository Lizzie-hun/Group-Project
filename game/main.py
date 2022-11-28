import arcade
from director import Director
import globals
from level import Level

def main():
    """ Main function """

    window = Director(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, globals.SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()