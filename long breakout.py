import pygame#imports
import random
import math

pygame.init()

class Brick:
  def __init__(self, xpos, ypos):
    self.xpos = xpos
    self.ypos = ypos
    self.alive = True
  def draw(self):
    self.color = (138 +random.randint(-10,10), 23 +random.randint(-10,10), 17 +random.randint(-10,10))
    self.color2 = (138-22, 23-12, 17-10)
    if self.alive is True:
        pygame.draw.ellipse(screen, self.color, (self.xpos, self.ypos, 100, 80))
        pygame.draw.arc(screen, self.color2, (self.xpos+10, self.ypos-16, 110, 115), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.xpos+30, self.ypos-36, 110, 150), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.xpos-22, self.ypos-16, 110, 115), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.xpos-42, self.ypos-36, 110, 150), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, ((22, 100, 8)), (self.xpos+45, self.ypos-51, 110, 115), (5*math.pi)/6, (math.pi), 8)
        pygame.draw.ellipse(screen, ((0, 0, 0)), (self.xpos, self.ypos, 100, 80), 5)
  def collide(self, x, y):
    if self.alive is True:
      if x+20>self.xpos and x<self.xpos+50 and y+20 > self.ypos and y < self.ypos+20:
        self.alive = False
        return True


screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
#variables
doExit = False
px = 300
py = 450

bx = 200
by = 200
bVx = 5
bVy = 5
#da bricks
b1 = Brick(20,20)
b2 = Brick(120, 20)
b3 = Brick(220,20)
b4 = Brick(320, 20)
b5 = Brick(420, 20)
b6 = Brick(520, 20)
b7 = Brick(620, 20)
b8 = Brick (40,60)
b9 = Brick(140, 60)
b10 = Brick(240,60)
b11 = Brick(340, 60)
b12 = Brick(440, 60)
b13 = Brick(540, 60)
b14 = Brick(640,60)
b15 = Brick(60,100)
b16 = Brick(260,100)
b17 = Brick(460, 100)
b18 = Brick(350, 250)
b19 = Brick(0, 250)
b20 = Brick(700,200)

while not doExit:#game loop#########################
  #I/O section................................
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      doExit = True
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    px-=5
  if keys[pygame.K_RIGHT]:
    px+=5


  #physics.....................................
  bx += bVx
  by += bVy
  #wall ball collision
  if bx < 0 or bx+20 > 700:
    bVx *= -1
  if by < 0 or by+20 > 500:
    bVy *= -1
  #bounce ball off paddle
  if by + 20 > py and bx+20 > px and bx < px+100:
    bVy *= -1

  if b1.collide(bx, by):
    bVy *= -1
  if b2.collide(bx, by):
    bVy *= -1
  if b3.collide(bx, by):
    bVy *= -1
  if b4.collide(bx, by):
    bVy *= -1
  if b5.collide(bx, by):
    bVy *= -1
  if b6.collide(bx, by):
    bVy *= -1
  if b7.collide(bx, by):
    bVy *= -1
  if b8.collide(bx, by):
    bVy *= -1
  if b9.collide(bx, by):
    bVy *= -1
  if b10.collide(bx, by):
    bVy *= -1
  if b11.collide(bx, by):
    bVy *= -1
  if b12.collide(bx, by):
    bVy *= -1
  if b13.collide(bx, by):
    bVy *= -1
  if b14.collide(bx, by):
    bVy *= -1
  if b15.collide(bx, by):
    bVy *= -1
  if b16.collide(bx, by):
    bVy *= -1
  if b17.collide(bx, by):
    bVy *= -1
  if b18.collide(bx, by):
    bVy *= -1
  if b19.collide(bx, by):
    bVy *= -1
  if b20.collide(bx, by):
    bVy *= -1

  #render section...........................
  screen.fill((0,0,0))


  pygame.draw.rect(screen, (255,100,100), (px,py, 100, 20))
  pygame.draw.rect(screen, (255,0,100), (bx,by, 20, 20))

  b1.draw()
  b2.draw()
  b3.draw()
  b4.draw()
  b5.draw()
  b6.draw()
  b7.draw()
  b8.draw()
  b9.draw()
  b10.draw()
  b11.draw()
  b12.draw()
  b13.draw()
  b14.draw()
  b15.draw()
  b16.draw()
  b17.draw()
  b18.draw()
  b19.draw()
  b20.draw()
  


  pygame.display.flip()

#end game loop#########################################
pygame.quit()
