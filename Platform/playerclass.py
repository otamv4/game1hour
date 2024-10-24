import pygame as py
from os.path import join
import random 

#sprites
class Player(py.sprite.Sprite):
    def __init__(self, groups, frames, sizex, sizey):
        super().__init__( groups)
        self.frames = frames
        self.frames_index = 0
        self.image = py.image.load(join('Platform','images','player', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center= (sizex/2, sizey/2))
        self.direction = py.math.Vector2(0,0)
        self.speed = 300

    def update(self, dt):
        keys = py.key.get_pressed()
        self.direction.x = int(keys[py.K_d] or keys[py.K_RIGHT]) - int(keys[py.K_a] or keys[py.K_LEFT])
        self.direction.y = int(keys[py.K_s] or keys[py.K_DOWN]) - int (keys[py.K_w] or keys[py.K_UP])

        if self.direction.y:
            self.frames_index += 20 * dt
            if self.frames_index < len(self.frames):
                self.image = self.frames[int(self.frames_index)]
            else:
                self.frames_index = 0

        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

class ColisionSprite():
    def __init__(self, pos, size,groups):
        super().__init__(groups)
        self.image = py.Surface(size)
        self.image.fill('blue')
        self.rect = self. image.get_frect(center = pos)
    
class Game:
    def __init__(self):
        self.sizex,self.sizey= 1280,720
        self.screen = py.display.set_mode((self.sizex, self.sizey))
        self.game = True

        py.init()
        py.display.set_caption("jogo da lua")
        self.Clock = py.time.Clock()

        player_frames = [py.image.load(join('Platform','images','player', f'{i}.png')).convert_alpha() for i in range(3)]

        #sprites objects
        self.all_sprites = py.sprite.Group()
        player = Player(self.all_sprites, player_frames, self.sizex, self.sizey)

        for i in range(6):
            x,y = random.randint(0,self.sizex), random.randint(0,self.sizey)
            w,h = random.randint(50,150), random.randint(60,120)
    
    def run(self):
        while self.game:
            dt = self.Clock.tick()/1000
            #event loop
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.game = False

            # update
            self.screen.fill('darkgrey')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.screen)
            
            py.display.update()
    
        py.quit()

if __name__ == "__main__":
    game = Game()
    game.run()