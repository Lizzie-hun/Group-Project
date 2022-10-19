import arcade
import globals
from director import Director
def main():
    window = Director(globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH, "Running Game")
    arcade.run()

main()