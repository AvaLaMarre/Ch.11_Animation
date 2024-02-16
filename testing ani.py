import random

import arcade

SW = 640
SH = 480


class Ball:
    def __init__(self, x, y, vx, vy, rad, col):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rad = rad
        self.color = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)

    def update_ball(self):
        self.x += self.vx
        self.y += self.vy
        if self.x <= self.rad or self.x >= SW - self.rad:
            self.vx *= -1
        if self.y <= self.rad or self.y >= SH - self.rad:
            self.vy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PINK)
        self.ball_list = []
        for i in range(60):
            radius = random.randint(10, 30)
            velocity_x = random.randint(-5, 5)
            velocity_y = random.randint(-5, 5)
            pos_x = random.randint(radius, SW)
            pos_y = random.randint(radius, SH)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball = Ball(pos_x, pos_y, velocity_x, velocity_y, radius, color)
            self.ball_list.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw_ball()

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()


if __name__ == "__main__":
    main()
