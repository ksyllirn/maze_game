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

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 10:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y <= 425:
            self.rect.y += self.speed

        if keys_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x <= 625:
            self.rect.x += self.speed 

class Enemy(GameSprite):
    direction = "right"
    def update(self):
        if self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x == 620:
                self.direction = "left"
        elif self.direction == "left":
            self.rect.x -= self.speed
            if self.rect.x == 400:
                self.direction = "right"

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3,wall_x, wall_y, wall_height, wall_width):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.height = wall_height
        self.width = wall_width
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


hero = Player("chicken.png", 80, 400, 6)
enemy = Enemy("creep.png", 400, 400, 2)
treasure = GameSprite("diam.png", 300, 230, 0)

wall_1 = Wall(255, 94, 0, 10, 50, 10, 640)
wall_2 = Wall(255, 94, 0, 180, 180, 340, 10)
wall_3 = Wall(255, 94, 0, 180, 180, 10, 290)
wall_4 = Wall(255, 94, 0, 470, 180, 150, 10)
wall_5 = Wall(255, 94, 0, 370, 320, 10, 100)
wall_6 = Wall(255, 94, 0, 650, 50, 280, 10)
wall_7 = Wall(255, 94, 0, 10, 50, 280, 10)




#mixer.init()
#mixer.music.load("sweden.mp3")
#mixer.music.play()

font.init()
win = font.Font(None, 70).render("nice play", True, (0,255,255))
loose_creep = font.Font(None, 70).render("oops....", True, (33,94,60))
loose_wall = font.Font(None, 70).render("u crashed try better", True, (255,0,0))

clock = time.Clock()
game = True
finish = False
FPS = 60

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0,0))
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()

        hero.update()
        enemy.update()

        hero.reset()
        enemy.reset()
        treasure.reset()

        if sprite.collide_rect(hero, treasure):
            result = win
            finish = True

        if sprite.collide_rect(hero, enemy):
            result = loose_creep
            finish = True

        if sprite.collide_rect(hero, wall_1) or sprite.collide_rect(hero, wall_2)\
            or sprite.collide_rect(hero, wall_3) or sprite.collide_rect(hero, wall_4) or sprite.collide_rect(hero, wall_5)\
                or sprite.collide_rect(hero, wall_6):
                    result = loose_wall
                    finish = True
    else: 
        window.blit(result,(100,70))

    display.update()
    clock.tick(FPS)        