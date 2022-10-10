import arcade
import globals
import score
import point

class HUD:
    def __init__(self):
        self.score = score(globals.STARTING_SCORE, point(globals.SCORE_X, globals.SCORE_Y))

    def draw_HUD(self):
        """Draws the HUD"""
        self.score.draw_score()

