from settings import *
from player import Player
from sprites import *

from random import randint

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        # sprites
        self.player = Player((500, 300), self.all_sprites, self.collision_sprites)
        for i in range(10):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(10, 300), randint(10, 300)
            CollisionSprite((x, y), (50, 50), (self.all_sprites, self.collision_sprites))
        
    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000
            
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # update
            self.all_sprites.update(dt)
            
            # draw
            self.display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()