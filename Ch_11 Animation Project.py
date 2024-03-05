import random

import arcade

SW = 700
SH = 600


class Ball:
    def __init__(self, x, y, vx, vy, rad, col):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rad = rad
        self.color = col

    def draw_ball(self):
        arcade.draw_rectangle_filled(SW/2, 570, 720, 80, (85, 84, 92))
        arcade.draw_rectangle_filled(SW / 2, 70, 720, 150, (4, 7, 36))
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)

    def update_ball(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= 730:
            self.x = -20


class Boat:
    def __init__(self, boat_x, boat_y, boat_vx, boat_vy, boat_side_w, boat_side_h, boat_color, tilt):
        self.boat_x = boat_x
        self.boat_y = boat_y
        self.boat_vx = boat_vx
        self.boat_vy = boat_vy
        self.b_side_w = boat_side_w
        self.b_side_h = boat_side_h
        self.b_color = boat_color
        self.tilt = tilt

    def draw_boat(self):
        arcade.draw_rectangle_filled(self.boat_x, self.boat_y, self.b_side_w-190, self.b_side_h+180, (15, 7, 0))

        """Boat"""
        arcade.draw_rectangle_filled(self.boat_x, self.boat_y, self.b_side_w, self.b_side_h, self.b_color, self.tilt)
        arcade.draw_rectangle_filled(self.boat_x + 75, self.boat_y + 45, self.b_side_w - 90, self.b_side_h - 15, self.b_color)
        arcade.draw_rectangle_filled(self.boat_x + 100, self.boat_y, self.b_side_w - 100, self.b_side_h - 65, self.b_color, -70)
        arcade.draw_rectangle_filled(self.boat_x - 100, self.boat_y, self.b_side_w - 120, self.b_side_h - 60, self.b_color, 70)
        arcade.draw_rectangle_filled(self.boat_x - 100, self.boat_y + 35, self.b_side_w, self.b_side_h - 70, self.b_color)

        #arcade.draw_rectangle_filled(self.boat_x, self.boat_y, self.b_side_w, self.b_side_h+100, (153, 145, 139))

    def update_boat(self):
        self.boat_x -= self.boat_vx
        self.boat_y += self.boat_vy
        if self.boat_x <= 350:
            self.boat_vx *= -1
            self.boat_vy *= -1
        if self.boat_x == 430:
            self.boat_vy *= -1
        if self.boat_x >= 500:
            self.boat_vx *= -1
            self.boat_vy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PINK)
        self.ball_list = []
        self.clock = 0
        self.distance = 0
        for i in range(30):
            radius = random.randint(30, 50)
            velocity_x = 6
            velocity_y = 0
            pos_x = 0 + self.distance
            pos_y = 525
            color = (64, 64, 66)
            self.ball = Ball(pos_x, pos_y, velocity_x, velocity_y, radius, color)
            self.ball_list.append(self.ball)
            self.distance += 40
        self.distance = 0
        for i in range(30):
            radius = random.randint(30, 50)
            velocity_x = 5
            velocity_y = 0
            pos_x = 0 + self.distance
            pos_y = 540
            color = (85, 84, 92)
            self.ball = Ball(pos_x, pos_y, velocity_x, velocity_y, radius, color)
            self.ball_list.append(self.ball)
            self.distance += 40
        self.boat_list = []
        for i in range(1):
            b_x = 450
            b_y = 220
            b_vx = 2
            b_vy = 1
            b_side_h = 80
            b_side_w = 200
            tilt = 0
            self.boat = Boat(b_x, b_y, b_vx, b_vy, b_side_w, b_side_h, (43, 25, 12), tilt)
            self.boat_list.append(self.boat)
        self.distance = 0
        for i in range(30):
            radius = random.randint(30, 50)
            velocity_x = 5
            velocity_y = 0
            pos_x = 0 + self.distance
            pos_y = 165
            color = (3, 0, 28)
            self.ball = Ball(pos_x, pos_y, velocity_x, velocity_y, radius, color)
            self.ball_list.append(self.ball)
            self.distance += 40
        self.distance = 0
        for i in range(30):
            radius = random.randint(30, 50)
            velocity_x = 7
            velocity_y = 0
            pos_x = 0 + self.distance
            pos_y = 135
            color = (4, 7, 36)
            self.ball = Ball(pos_x, pos_y, velocity_x, velocity_y, radius, color)
            self.ball_list.append(self.ball)
            self.distance += 40

    def on_draw(self):
        arcade.start_render()
        self.boat.draw_boat()
        for ball in self.ball_list:
            ball.draw_ball()

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()
        self.clock += dt
        if self.clock <= 1:
            arcade.set_background_color((15, 6, 71))
        elif self.clock <= 2:
            arcade.set_background_color((6, 0, 48))
        else:
            self.clock = 0
        self.boat.update_boat()


def main():
    window = MyGame(SW, SH, "Ship In A Storm")
    arcade.run()


if __name__ == "__main__":
    main()
