import random

import arcade

SW = 600
SH = 600


class Ball:
    def __init__(self, x, y, vx, vy, rad, col, box, bulb_col):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rad = rad
        self.color = col
        self.box_color = box
        self.light_color = bulb_col

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)

    def draw_background(self):
        arcade.draw_rectangle_filled(475, 30, 20, 20, arcade.color.SILVER)
        arcade.draw_rectangle_outline(475, 30, 20, 20, arcade.color.BLACK)
        arcade.draw_rectangle_filled(570, 30, 60, 60, arcade.color.BLACK_OLIVE)
        arcade.draw_rectangle_filled(510, 30, 60, 60, arcade.color.BRONZE)
        arcade.draw_rectangle_outline(510, 30, 60, 60, arcade.color.BLACK)
        arcade.draw_rectangle_filled(SW/2, SH/2, SW-120, SH-120, self.box_color)
        arcade.draw_circle_filled(SW/2, 450, 100, self.light_color, )
        arcade.draw_rectangle_filled(SW/2, 570, 100, 64, arcade.color.GRAY)

    def update_ball(self):
        if not self.vx == 0:
            self.x += self.vx
        if not self.vy == 0:
            self.y += self.vy
        if self.x <= self.rad:
            self.vx *= 0
            self.vy = 10
        if self.y <= self.rad - 1 or self.y >= SH - self.rad:
            self.vy *= 0
            self.vx = 10
        if self.x == 570 and self.y > 30:
            self.vx *= 0
            self.vy = -10


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ANTIQUE_BRASS)
        self.ball_list = []
        self.ball_space = 0
        for i in range(150):
            radius = 30
            velocity_x = -10
            velocity_y = 0
            pos_x = 500 + self.ball_space
            pos_y = 30
            box = arcade.color.BLACK
            bulb_col = arcade.color.SILVER
            color = arcade.color.COPPER

            self.ball = Ball(pos_x, pos_y, velocity_x, velocity_y, radius, color, box, bulb_col)
            self.ball_list.append(self.ball)
            self.ball_space += radius*2

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw_ball()
        self.ball.draw_background()

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()


def main():
    window = MyGame(SW, SH, "Electricity")
    arcade.run()


if __name__ == "__main__":
    main()
