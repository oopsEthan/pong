from turtle import *
from game_objects import *

class Game():
    def __init__(self) -> None:
        self.SCREEN_X = 1280
        self.SCREEN_Y = 720
        self.game_screen = Screen()
        self.game_screen.tracer(0)
        self.game_screen.setup(self.SCREEN_X, self.SCREEN_Y)
        self.game_screen.bgcolor("black")

        self.ball = Ball()
        self.player = Player()
        self.opponent = Opponent()

        self.top_wall = Wall("top")
        self.bottom_wall = Wall("bottom")
        self.game_screen.update()

        self.collisions = [self.player, self.opponent, self.top_wall, self.bottom_wall]
        self.ball.set_possible_collisions(self.collisions)
        
        self.game_screen.listen()
        self.game_screen.onkeypress(self.player.go_up, "w")
        self.game_screen.onkeypress(self.player.go_down, "s")
        self.game_screen.onkeyrelease(self.player.stop, "w")
        self.game_screen.onkeyrelease(self.player.stop, "s")
        
        self.game_loop()

    def run_moves(self):
        self.ball.travel()
        self.player.move()

    def game_loop(self):
        self.run_moves()
        self.game_screen.update()
        self.game_screen.ontimer(self.game_loop, 20)

    def run(self):
        self.game_screen.mainloop()