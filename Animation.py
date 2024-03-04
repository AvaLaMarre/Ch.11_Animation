import random

import arcade

SW = 600
SH = 600


class Ball:
    def __init__(self, x, y, vx, vy, side_w, side_h, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.side_w = side_w
        self.side_h = side_h
        self.color = color

    def draw_ball(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side_w, self.side_h, self.color)

    def draw_background(self):
        arcade.draw_rectangle_filled(SW/2, SH/2, 60, 700, arcade.color.BLACK)
        arcade.draw_rectangle_filled(SW / 2, SH / 2, 700, 60, arcade.color.BLACK)

    def update_ball(self):
        self.x += self.vx
        self.y += self.vy
        if self.y >= 700:
            self.x = 800
            self.y = SH/2
            self.side_w = 100
            self.side_h = 50
            self.vy = 0
            self.vx = -5
        if self.x == -100:
            self.x = SW/2
            self.y = -200
            self.side_w = 50
            self.side_h = 100
            self.vy = 5
            self.vx = 0


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PINK)
        self.ball_list = []
        self.clock = 0
        self.ball_space = 0
        for i in range(6):
            side_w = 50
            side_h = 100
            velocity_x = 0
            velocity_y = 5
            pos_x = SW/2
            pos_y = -100 - self.ball_space
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.ball = Ball(pos_x, pos_y, velocity_x, velocity_y, side_w, side_h, color)
            self.ball_list.append(self.ball)
            self.ball_space += side_h * 2 + 160

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_background()
        for ball in self.ball_list:
            ball.draw_ball()


    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()
            self.clock += dt
            if self.clock <= 3:
                arcade.set_background_color(arcade.color.WHITE)
            elif self.clock <= 6:
                arcade.set_background_color(arcade.color.RED)
            elif self.clock <= 9:
                arcade.set_background_color(arcade.color.BLUE)
            else:
                self.clock = 0



def main():
    window = MyGame(SW, SH, "UHS PARKING LOT!")
    arcade.run()


if __name__ == "__main__":
    main()
