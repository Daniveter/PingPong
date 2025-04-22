from pygame import *
clock=time.Clock()
win= 700, 500
window=display.set_mode(win)
display.set_caption('Пинг-понг')
back = 5, 236, 252
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
        if keys_pressed[K_w] and self.rect.y!=0:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y!=420:
            self.rect.y+=self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y!=0:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y!=420:
            self.rect.y+=self.speed
rocket1=Player('roketka.png',10,0,3,40,80)
rocket2=Player('roketka.png',650,0,3,40,80)
game=True
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    window.fill(back)
    rocket1.reset()
    rocket1.update_l()
    rocket2.reset()
    rocket2.update_r()
    display.update()
    clock.tick(60)
