import pygame
import random
pygame.init()
root=pygame.display.set_mode((200,200))
block=pygame.Surface((10,10))
block.fill((0,255,0))
 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                
                print("Hey, you pressed the key, '0'!")
            if event.key == pygame.K_1:
                print("Doing whatever")
            
            if event.key == pygame.K_5:
                            print("Leo")
            if event.key ==pygame.K_9:
                x=random.randint(0,100)
                y=random.randint(0,100)
                root.fill((0,0,0))
                root.blit(block,(x,y))
                
                pygame.display.update()

