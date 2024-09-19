from turtle import *

# Global variables
PLAYER_X = -550 # Starting location of player paddle
OPPONENT_X = -PLAYER_X # Starting location of opponent paddle (opposite of player paddle)
BALL_DIAMETER = 0.75 # Diameter of ball
TOP_WALL_Y = 365 # Starting location for top wall
BOTTOM_WALL_Y = -350 # Start location for bottom wall

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
        self.update_paddle_boundaries()

    def detect_wall(self) -> bool:
        if (self.y_velocity > 0 and self.paddle_top_y >= TOP_WALL_Y) or (self.y_velocity < 0 and self.paddle_bottom_y <= BOTTOM_WALL_Y):
            return True
        return False
    
    def update_paddle_boundaries(self) -> None:
        self.paddle_top_y = self.paddle_obj.ycor() + (self.paddle_height * 20) / 2
        self.paddle_bottom_y = self.paddle_obj.ycor() - (self.paddle_height * 20) / 2

    def set_up_paddle_obj(self) -> None:
        self.paddle_obj = Turtle()
        initialize_basic_graphics(self.paddle_obj, "white", self.paddle_height, self.paddle_width)

class Player(Paddle):
    def set_up_paddle_obj(self) -> None:
        super().set_up_paddle_obj()
        self.MOVE_SPEED = 10
        self.paddle_obj.goto(PLAYER_X, 0)
        self.y_velocity = 0
    
    def go_up(self) -> None:
        self.y_velocity = self.MOVE_SPEED
    
    def go_down(self) -> None:
        self.y_velocity = -self.MOVE_SPEED
    
    def move(self) -> None:
        if not self.detect_wall():
            new_y = self.paddle_obj.ycor() + self.y_velocity
            self.paddle_obj.goto(PLAYER_X, new_y)
        self.update_paddle_boundaries()
    
    def stop(self) -> None:
        self.y_velocity = 0

class Opponent(Paddle):
    def set_up_paddle_obj(self) -> None:
        super().set_up_paddle_obj()
        self.paddle_obj.goto(OPPONENT_X, 0)
        self.y_velocity = 0

    def movement(self) -> None:
        if self.detect_wall():
            self.y_velocity = self.bounce_off_wall()
        else:
            new_y = self.paddle_obj.ycor() + self.y_velocity
            self.paddle_obj.goto(OPPONENT_X, new_y)
        self.update_paddle_boundaries()

    def set_opponent_speed(self, opp_speed) -> None:
        self.y_velocity = opp_speed
    
    def bounce_off_wall(self) -> int:
        return -self.y_velocity

class Ball:
    def __init__(self) -> None:
        self.set_up_ball_obj()
        self.collisions = []
        self.ball_radius = 5

    def set_up_ball_obj(self) -> None:
        self.ball_obj = Turtle()
        initialize_basic_graphics(self.ball_obj, "white", BALL_DIAMETER, BALL_DIAMETER)

    def travel(self) -> None:
        if(self.collisions):
            self.check_for_collision()
        new_x = self.ball_obj.xcor() + self.x_velocity
        new_y = self.ball_obj.ycor() + self.y_velocity
        self.ball_obj.goto(new_x, new_y)
        
    def set_possible_collisions(self, possible_collisions) -> None:
        self.collisions = possible_collisions
    
    def set_ball_speed(self, ball_speed) -> None:
        self.ball_speed = ball_speed
        self.y_velocity = -self.ball_speed
        self.x_velocity = -self.ball_speed
    
    def check_for_collision(self) -> None:
        for col in self.collisions:
            if isinstance(col, Wall):
                if abs(self.ball_obj.ycor() - col.wall_obj.ycor()) <= self.ball_radius + col.wall_height:
                    self.bounce(col)
            elif isinstance(col, Paddle):
                if abs(self.ball_obj.xcor() - col.paddle_obj.xcor()) <= self.ball_radius + col.paddle_width:
                    paddle_top = col.paddle_obj.ycor() + (col.paddle_height * 20 / 2)
                    paddle_bottom = col.paddle_obj.ycor() - (col.paddle_height * 20 / 2)
                    if paddle_bottom <= self.ball_obj.ycor() <= paddle_top:
                        self.bounce(col)

    # Bouncing off wall reverses y_velocity, bouncing off paddle reverses x_velocity
    def bounce(self, collider) -> None:
        if isinstance(collider, Wall):
            self.y_velocity = -self.y_velocity

        else:
            self.x_velocity = - self.x_velocity

    def detect_score(self, score_ui) -> None:
        if self.ball_obj.xcor() < (PLAYER_X - 25):
            score_ui.update_score("opponent")
            self.reset()

        elif self.ball_obj.xcor() > (OPPONENT_X + 25):
            score_ui.update_score("player")
            self.reset()
    
    def reset(self) -> None:
        self.y_velocity = -self.ball_speed
        self.x_velocity = -self.ball_speed
        self.ball_obj.goto(0, 0)

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
            self.y = TOP_WALL_Y
        
        elif self.location == "bottom":
            self.y = BOTTOM_WALL_Y