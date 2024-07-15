import arcade
import math
count = 50
x = 0
class Game(arcade.Window):

   def __init__(self):
       super().__init__(width=800, height=600, title='Рисование фигур')
       self.background_color = (255, 255, 255)
       self.texture = arcade.load_texture(':resources:images/animated_characters/zombie/zombie_jump.png')

   def on_draw(self):
        self.batch = arcade.ShapeElementList()
        self.clear()
        global x
        x += 0.1
        for i in range(count):
            e = arcade.create_ellipse_filled_with_colors(
                center_x=i*(600//(count//2)),
                center_y=(math.sin(x+i) * 100 + 300) * 20//count + (count*3),
                width=800//count,
                height=800//count,
                outside_color=arcade.color.RED,
                inside_color=arcade.color.GREEN
            )
            self.batch.append(e)

        self.batch.draw()


if __name__ == '__main__':
   game = Game()
   arcade.run()
