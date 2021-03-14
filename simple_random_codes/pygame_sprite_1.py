import pygame
GREEN=(0,255,0)
WIDTH=400
HEIGHT=400


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
        
    def update(self):
         
        self.rect.x += 5
        screen.fill((0,0,0))
        screen.blit(self.image,(self.rect.x,0))
        pygame.display.flip()
        if self.rect.left > WIDTH:
            self.rect.right = 0
screen=pygame.display.set_mode((400,400))
all1=pygame.sprite.Group()   
play1=Player()
all1.add(play1)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print("aba")
 
        play1.update()
        
        pygame.display.update()

