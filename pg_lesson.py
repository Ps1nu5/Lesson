import pygame
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.15

level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]


class Player(sprite.Sprite):
   def __init__(self, x, y):
       sprite.Sprite.__init__(self)
       self.yvel = 0
       self.onGround = False
       self.xvel = 0
       self.startX = x
       self.startY = y
       self.image = Surface((WIDTH, HEIGHT))
       self.image.fill(Color(COLOR))
       self.rect = Rect(x, y, WIDTH, HEIGHT)

   def update(self, left, right, up, platforms):
       if up:
           if self.onGround:
               self.yvel = -JUMP_POWER
       if left:
           self.xvel = -MOVE_SPEED

       if right:
           self.xvel = MOVE_SPEED

       if not (left or right):
           self.xvel = 0
       if not self.onGround:
           self.yvel += GRAVITY
       self.onGround = False
       self.rect.y += self.yvel
       self.collide(0, self.yvel, platforms)

       self.rect.x += self.xvel
       self.collide(self.xvel, 0, platforms)

   def collide(self, xvel, yvel, platforms):
       for p in platforms:
           if sprite.collide_rect(self, p):

               if xvel > 0:
                   self.rect.right = p.rect.left

               if xvel < 0:
                   self.rect.left = p.rect.right

               if yvel > 0:
                   self.rect.bottom = p.rect.top
                   self.onGround = True
                   self.yvel = 0

               if yvel < 0:
                   self.rect.top = p.rect.bottom
                   self.yvel = 0

class Platform(sprite.Sprite):
    def __init__(self, x, y):
       sprite.Sprite.__init__(self)
       self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
       self.image.fill(Color(PLATFORM_COLOR))
       self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

def main():
    hero = Player(55, 55)
    left = right = False
    up = False
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)

    timer = pygame.time.Clock()
    x = y = 0
    for row in level:
       for col in row:
           if col == "-":
               pf = Platform(x, y)
               entities.add(pf)
               platforms.append(pf)

           x += PLATFORM_WIDTH
       y += PLATFORM_HEIGHT
       x = 0
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Платформер")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    while 1:
       timer.tick(60)
       for e in pygame.event.get():
           if e.type == QUIT:
               raise SystemExit
           if e.type == KEYDOWN and e.key == K_LEFT:
               left = True
           if e.type == KEYDOWN and e.key == K_RIGHT:
               right = True

           if e.type == KEYUP and e.key == K_RIGHT:
               right = False
           if e.type == KEYUP and e.key == K_LEFT:
               left = False
           if e.type == KEYDOWN and e.key == K_UP:
               up = True
           if e.type == KEYUP and e.key == K_UP:
               up = False
       screen.blit(bg, (0, 0))

       hero.update(left, right, up, platforms)
       entities.draw(screen)
       pygame.display.update()

if __name__ == "__main__":
    main()
