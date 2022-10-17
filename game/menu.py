import arcade
import arcade.gui
import globals


class Menu:
    def __init__(self):
        self.background_color = globals.MENU_BACKGROUND_COLOR
        self.v_box = arcade.gui.UIBoxLayout(space_between=20)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.button_style = {
            "font_name": (globals.MENU_FONT, globals.MENU_BACKUP_FONT),
            "font_size": globals.MENU_FONT_SIZE,
            "font_color": globals.MENU_FONT_COLOR,
            "border_width": globals.MENU_BUTTON_BORDER_WIDTH,
            "border_color": globals.MENU_BUTTON_BORDER_COLOR,
            "bg_color": globals.MENU_BUTTON_BACKGROUND_COLOR,

            # used if button is pressed
            "bg_color_pressed": globals.MENU_BUTTON_PRESS_BACKGROUND_COLOR,
            "border_color_pressed": globals.MENU_BUTTON_PRESS_BORDER_COLOR,  # also used when hovered
            "font_color_pressed": arcade.color.BLACK,
        }

        self.start_button = arcade.gui.UIFlatButton(text="Start", width=200, style=self.start_style)
        self.quit_button = arcade.gui.UIFlatButton(text="Quit", width=200, style=self.start_style)

        self.v_box.add(self.start_button)
        self.v_box.add(self.quit_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )


    def draw_menu(self):
        arcade.set_background_color(self.background_color)
        self.clear()
        self.manager.draw()

