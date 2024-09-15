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
        self.paddle_width = 1
        self.paddle_height = 5.5
        self.set_up_paddle_obj()

    def set_up_paddle_obj(self) -> None:
        self.paddle_obj = Turtle()
        initialize_basic_graphics(self.paddle_obj, "white", self.paddle_height, self.paddle_width)

class Player(Paddle):
    def set_up_paddle_obj(self) -> None:
        super().set_up_paddle_obj()
        self.MOVE_SPEED = 10
        self.paddle_obj.goto(-550, 0)
        self.y_velocity = 0
    
    def go_up(self):
        self.y_velocity = self.MOVE_SPEED
    
    def go_down(self):
        self.y_velocity = -self.MOVE_SPEED
    
    def move(self):
        new_y = self.paddle_obj.ycor() + self.y_velocity
        self.paddle_obj.goto(-550, new_y)
    
    def stop(self):
        self.y_velocity = 0

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
        self.check_for_collision()
        new_x = self.ball_obj.xcor() + self.x_velocity
        new_y = self.ball_obj.ycor() + self.y_velocity
        self.ball_obj.goto(new_x, new_y)
        
    def set_possible_collisions(self, possible_collisions) -> None:
        self.collisions = possible_collisions
    
    def check_for_collision(self) -> None:
        for col in self.collisions:
            if isinstance(col, Wall):
                if abs(self.ball_obj.ycor() - col.wall_obj.ycor()) <= self.ball_radius + col.wall_height:
                    self.bounce(col)
            elif isinstance(col, Paddle):
                if abs(self.ball_obj.xcor() - col.paddle_obj.xcor()) <= self.ball_radius + col.paddle_width:
                    if abs(self.ball_obj.ycor() - col.paddle_obj.ycor()) <= self.ball_radius + (col.paddle_height / 2):
                        self.bounce(col)
    
    def bounce(self, collider) -> None:
        if isinstance(collider, Wall):
            self.y_velocity = -self.y_velocity

        else:
            self.x_velocity = - self.x_velocity

class Wall():
    def __init__(self, location) -> None:
        self.wall_obj = Turtle()
        self.wall_height = 1
        self.location = location
        initialize_basic_graphics(self.wall_obj, "black", self.wall_height, 100)
        self.determine_vars_by_location()

        self.wall_obj.goto(0, self.y)

    def determine_vars_by_location(self) -> None:
        if self.location == "top":
            self.y = 365
        
        elif self.location == "bottom":
            self.y = -350