import pygame

pygame.init()

ecran = pygame.display.set_mode((640, 480))

image1J=pygame.image.load("./texture/bouton1J.png").convert_alpha()
image2J = pygame.image.load("./texture/bouton2J.png").convert_alpha()
imagepara=pygame.image.load("./texture/paramètres.png").convert_alpha()
imagequit=pygame.image.load("./texture/quitter.png").convert_alpha()

largeur = 10
hauteur = 10
couleur = (20, 180, 20)

continuer = True

while continuer:
    ecran.blit(image1J, (0, 0))
    ecran.blit(image2J, (0, 125))
    ecran.blit(imagepara, (0, 250))
    ecran.blit(imagequit, (0, 375))
    
    for event in pygame.event.get():
        x,y=pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and 375 <= y <= 475:
            continuer = False
            
        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and 375 <= y <= 475:
            continuer = False
            
        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and 375 <= y <= 475:
            continuer = False
            
        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and 375 <= y <= 475:
            continuer = False
            
        if event.type == pygame.QUIT:
            continuer = False
        
    pygame.display.flip()

pygame.quit()