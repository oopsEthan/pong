from turtle import *
from game_objects import *

class UI():
    def __init__(self) -> None:
        self.ui_turtle = Turtle()
        self.score_turtle = Turtle()
        self.player_score = 0
        self.opponent_score = 0
        self.render_ui()

    def render_ui(self) -> None:
        initialize_basic_graphics(self.ui_turtle, "white", 1, 1)
        initialize_basic_graphics(self.score_turtle, "white", 1, 1)
        self.ui_turtle.hideturtle()
        self.score_turtle.hideturtle()
        self.ui_turtle.width(4)
        self.ui_turtle.rt(90)
        self.reset_position(self.ui_turtle)
        self.draw_line_down_middle()
        self.draw_score()
    
    def draw_line_down_middle(self) -> None:
        lines = 40
        dotted = True
        while lines > 0:
            if dotted:
                self.ui_turtle.pd()
            else:
                self.ui_turtle.pu()
            dotted = not dotted
            self.ui_turtle.fd(30)
            lines -= 1
        self.reset_position(self.ui_turtle)

    def draw_score(self):
        self.score_turtle.clear()
        player_score_position = -50
        opponent_score_position = 50
        self.score_turtle.goto(player_score_position, 275)
        self.score_turtle.write(f"{self.player_score}", align="center", font=("Courier", 48, "normal"))
        self.score_turtle.goto(opponent_score_position, 275)
        self.score_turtle.write(f"{self.opponent_score}", align="center", font=("Courier", 48, "normal"))
    

    def update_score(self, scorer) -> None:
        if(scorer == "player"):
            self.player_score += 1
        else:
            self.opponent_score += 1
        
        self.draw_score()

    def reset_position(self, tur) -> None:
        tur.goto(0, 365)

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
        self.ui = UI()

        self.collisions = [self.player, self.opponent, self.top_wall, self.bottom_wall]
        self.ball.set_possible_collisions(self.collisions)
        
        self.game_screen.listen()
        self.game_screen.onkeypress(self.player.go_up, "w")
        self.game_screen.onkeypress(self.player.go_down, "s")
        self.game_screen.onkeyrelease(self.player.stop, "w")
        self.game_screen.onkeyrelease(self.player.stop, "s")
        
        self.game_loop()

    def run_moves(self):
        self.ball.detect_score(self.ui)
        self.ball.travel()
        self.player.move()

    def game_loop(self):
        self.run_moves()
        self.game_screen.update()
        self.game_screen.ontimer(self.game_loop, 20)

    def run(self):
        self.game_screen.mainloop()