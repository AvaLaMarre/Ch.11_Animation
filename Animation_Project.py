'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''

import arcade

SW = 600
SH = 600


class Ball:
    def __init__(self, x, y, vy, side, col, rad, dot_color):
        self.x = x
        self.y = y
        self.vy = vy
        self.side = side
        self.color = col
        self.rad = rad
        self.dot_color = dot_color

    def draw_ball(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.color)

    def draw_dot(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.dot_color)

    def update_ball(self):
        self.y += self.vy
        if self.y <= 200:
            self.vy *= 0
        if self.side <= 50:
            self.side += 0.8
            self.rad += 0.15


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)
        self.ball_list = []
        self.clock = 0
        x_value = 70
        for i in range(6):
            radius = 6
            pos_x = x_value
            pos_y = 550
            velocity_y = -6
            color = arcade.color.RED
            rad = 0
            dot_color = arcade.color.WHITE
            self.ball = Ball(pos_x, pos_y, velocity_y, radius, color, rad, dot_color)
            self.ball_list.append(self.ball)
            x_value += 90

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw_ball()
            ball.draw_dot()
        if self.clock >= 10:
            arcade.draw_rectangle_filled(60, 60, 60, 60, arcade.color.WHITE)

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()
            self.clock += dt


def main():
    window = MyGame(SW, SH, "Dice")
    arcade.run()


if __name__ == "__main__":
    main()
