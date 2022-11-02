import arcade
from director import Director
import globals
from level import Level
from gates import Gates

def main():
    window = Director(globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH, "Running Game")
    arcade.run()

main()