from pygame import *

window_width = 700
window_height = 500

window = display.set_mode((window_width,window_height))
display.set_caption("maze")
background = transform.scale(image.load("back.jpg"), (window_width,window_height))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


hero = GameSprite("chicken.png", 100, 200, 0)
enemy = GameSprite("creep.png", 200, 200, 0)
treasure = GameSprite("diam.png", 300, 200, 0)

#mixer.init()
#mixer.music.load("sweden.mp3")
#mixer.music.play()

clock = time.Clock()
game = True
FPS = 60

while game:
    window.blit(background, (0,0))
    hero.reset()
    enemy.reset()
    treasure.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)        
