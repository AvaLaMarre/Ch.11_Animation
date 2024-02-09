import random

import arcade

SW = 640
SH = 480

class Ball():
    def __init__(self):

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PINK)
        self.x = width/2
        self.y = height/2
        self.vx = random.randint(-2,2)
        self.vy = random.randint(-2,2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, 15, arcade.color.BANANA_MANIA)

    def on_update(self, dt):
        self.x += self.vx
        self.y += self.vy
def main():
    window =MyGame(SW, SH, "Drawing Example")
    arcade.run()


if __name__ == "__main__":
    main()