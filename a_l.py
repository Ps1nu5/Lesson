import arcade
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'Название окна'


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(resizable=False, center_window=True)
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.set_caption(SCREEN_TITLE)
        self.set_mouse_visible(True)
        arcade.set_background_color((230, 230, 255))

        self.speed = 5

        self.direction_x = self.speed
        self.direction_y = self.speed

        self.square_x = 20
        self.square_y = 300

        self.sqare_angle = 0



    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_rectangle_filled(self.square_x, self.square_y, 50, 50, (255, 0, 0), self.sqare_angle)

    def update(self, delta_time: float):
        self.square_x += self.direction_x
        self.square_y += self.direction_y
        self.sqare_angle += 1

        if self.square_x >= self.width or self.square_x <= 0:
            self.direction_x *= -1
        if self.square_y >= self.height or self.square_y <= 0:
            self.direction_y *= -1

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
