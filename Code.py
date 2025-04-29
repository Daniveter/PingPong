from pygame import *
from random import randint
clock=time.Clock()
wind= 700, 500
rand=randint(1,2)
window=display.set_mode(wind)
display.set_caption('Пинг-понг')
back = 5, 236, 252
ballspeed=-1
font.init()
font1 = font.SysFont('Arial', 36)
win1 = font1.render('Первый игрок победил!', True, (28, 172, 120))
win2 = font1.render('Второй игрок победил!', True, (28, 172, 120))
window.fill(back)
class GameSprite(sprite.Sprite):
    def __init__(self, picture, pos_1, pos_2, speed, width, height):
        super(). __init__()
        self.image = transform.scale(image.load(picture),(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_1
        self.rect.y = pos_2
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>=0:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y<=420:
            self.rect.y+=self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>=0:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<=420:
            self.rect.y+=self.speed
class Ball(GameSprite):
    def update(self):
        pass
rocket1=Player('roketka.png',10,250,3,40,80)
rocket2=Player('roketka.png',650,250,3,40,80)
ball=Ball('мяч.jpeg', 330, 250, ballspeed, 50, 50)
speed_x=3
speed_y=1
game=True
finish=False
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish!=True:
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if sprite.collide_rect(ball, rocket2):
            speed_x=0
            speed_y=0
            speed_x-=6
            if rand==1:
                speed_y+=2
            if rand==2:
                speed_y-=2
        if sprite.collide_rect(ball, rocket1):
            speed_x=0
            speed_y=0
            speed_x+=6
            if rand==1:
                speed_y+=2
            if rand==2:
                speed_y-=2
        if ball.rect.y>=450:
            speed_y=0
            speed_y-=3
        if ball.rect.y<=0:
            speed_y=0
            speed_y+=3
        window.fill(back)
        rand=randint(1,2)
        rocket1.reset()
        rocket1.update_l()
        rocket2.reset()
        rocket2.update_r()
        ball.reset()
        ball.update()
        if ball.rect.x>=700:
            window.blit(win1, (165, 200))
            finish=True
        if ball.rect.x<=-50:
            window.blit(win2, (165, 200))
            finish=True
        display.update()
        clock.tick(60)
