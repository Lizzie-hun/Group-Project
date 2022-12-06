import arcade
from director import Director
import menu
import globals

def main():
    """ Main function """

    window = arcade.Window(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, globals.SCREEN_TITLE)
    start_game = menu()
    window.show_view(start_game)
    start_game.setup()
    arcade.run()

if __name__ == "__main__":
    main()