from turtle import *

# Many objects are the same color, shape, pen_up, etc.
#   Call this function when needing to set up the basics
def initialize_basic_graphics(tur, color, x, y) -> None:
    tur.pu()
    tur.shape("square")
    tur.shapesize(x, y)
    tur.color(color)

# Paddle is for shared variables
class Paddle:
    def __init__(self) -> None:
        self.set_up_paddle_obj()

    def set_up_paddle_obj(self) -> None:
        self.paddle_obj = Turtle()
        initialize_basic_graphics(self.paddle_obj, "white", 5.5, 1)

class Player(Paddle):
    def set_up_paddle_obj(self) -> None:
        super().set_up_paddle_obj()
        self.paddle_obj.goto(-550, 0)

class Opponent(Paddle):
    def set_up_paddle_obj(self) -> None:
        super().set_up_paddle_obj()
        self.paddle_obj.goto(550, 0)

class Ball:
    def __init__(self) -> None:
        self.set_up_ball_obj()
        self.collisions = []
        self.y_velocity = -3
        self.x_velocity = -3
        self.ball_radius = 5

    def set_up_ball_obj(self) -> None:
        self.ball_obj = Turtle()
        diameter = 0.75
        initialize_basic_graphics(self.ball_obj, "white", diameter, diameter)

    def travel(self) -> None:
        # check_for_collision()
        new_x = self.ball_obj.xcor() + self.x_velocity
        new_y = self.ball_obj.ycor() + self.y_velocity
        self.ball_obj.goto(new_x, new_y)
        
    def set_possible_collisions(self, possible_collisions) -> None:
        self.collisions = possible_collisions
    
    def check_for_collision(self) -> None:
        for col in self.collisions:
            distance = self.ball_obj.distance(col)

            # Code needs to change to consider the wall at bottom too
            if distance <= self.ball_radius + col.paddle_width:
                self.bounce()
    
    def bounce(self) -> None:
        # It'll need to bounce x_velocity?
        self.y_velocity = -self.y_velocity
        pass

class Wall():
    def __init__(self, location) -> None:
        self.wall_obj = Turtle()
        self.location = location
        initialize_basic_graphics(self.wall_obj, "black", 1, 100)
        self.determine_vars_by_location()

        self.wall_obj.goto(0, self.y)

    def determine_vars_by_location(self) -> None:
        if self.location == "top":
            self.y = 365
        
        elif self.location == "bottom":
            self.y = -350