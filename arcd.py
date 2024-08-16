import arcade

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/boxCrate_double.png')
        self.change_x = 1
        self.scale = 2

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDHT:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_WIDHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/boxCrate_double.png')
        self.scale = 0.1

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDHT:
            self.right = SCREEN_WIDHT
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDHT / 2
        self.bar.center_y = SCREEN_HEIGHT / 2
        self.ball.center_x = SCREEN_WIDHT / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDHT, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()