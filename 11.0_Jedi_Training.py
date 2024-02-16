import arcade
import random
'''
# 11.0 Jedi Training (50pts)  Name:________________



 
CHAPTER 11 FINAL CODE QUESTIONS: (10pts)
--------------------------------
1.) Where is the ball's original location?

2.) What are the variables dx and dy?

3.) How many pixels/sec does the ball move in the x-direction?

4.) How many pixels/sec does the ball move in the y-direction?

5.) Which method is run 60 times/second?

6.) What does this code do?   self.dx *= -1

7.) What does this code do?  self.pos_y += self.dy

8.) What is the width of the window?

9.) What is this code checking?  self.pos_y > SH - self.rad:

10.) What is this code checking? if self.pos_x < self.rad
'''

'''
30 BOX BOUNCE PROGRAM (20pts)
---------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''


'''
SNOWFALL  (20pts)
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.
'''

SW = 600
SH = 600


class Ball:
    def __init__(self, x, y, vy, rad, col):
        self.x = x
        self.y = y
        self.vy = vy
        self.rad = rad
        self.color = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)

    def update_ball(self):
        self.y += self.vy
        if self.y <= self.rad:
            self.y = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball_list = []
        for i in range(300):
            radius = random.randint(1, 3)
            velocity_y = random.randint(-4, -1)
            pos_x = random.randint(0, 600)
            pos_y = random.randint(600, 800)
            color = arcade.color.WHITE
            if i == 3:
                color = arcade.color.RED
            self.ball = Ball(pos_x, pos_y, velocity_y, radius, color)
            self.ball_list.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw_ball()
        arcade.draw_rectangle_filled(SW / 2, SH / 2, 10, SH, arcade.color.BROWN)
        arcade.draw_rectangle_filled(SW / 2, SH / 2, SW, 10, arcade.color.BROWN)

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()


def main():
    window = MyGame(SW, SH, "SnowFall")
    arcade.run()


if __name__ == "__main__":
    main()
