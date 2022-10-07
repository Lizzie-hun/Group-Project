import arcade
import globals

#This will go into the HUD file

class Score:
    def __init__(self, _starting_score, _location):
        """Starting score, Location object"""
        self.score = _starting_score
        self.location = _location

    def draw_score(self):
        """Draws the score"""
        arcade.Text(
            self.score, #Text to display
            self.location.x, #Starting x location
            self.location.y,  #Starting y location
            arcade.color.BLACK, #Color to draw in
            font_size=globals.SCORE_FONT_SIZE
        )

    def update_score(self, value):
        """value: the value that will be added to the score"""
        self.score += value
