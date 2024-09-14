from turtle import *

class Game():
    def __init__(self) -> None:
        self.SCREEN_X = 1280
        self.SCREEN_Y = 720
        self.game_screen = Screen()
        self.game_screen.setup(self.SCREEN_X, self.SCREEN_Y)
        self.game_screen.bgcolor("black")
    

    def run(self):
        self.game_screen.mainloop()