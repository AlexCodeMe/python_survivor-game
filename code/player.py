from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collison_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png'))
        self.rect = self.image.get_rect(center = pos)
        
        # movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collison_sprites
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
    
    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt
    
    def update(self, dt):
        self.input()
        self.move(dt)