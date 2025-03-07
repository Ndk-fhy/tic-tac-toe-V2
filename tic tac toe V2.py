import pygame

pygame.init()

ecran = pygame.display.set_mode((640, 480))

# image menu principale
image1J=pygame.image.load("./texture/bouton1J.png").convert_alpha()
image2J = pygame.image.load("./texture/bouton2J.png").convert_alpha()
imagepara=pygame.image.load("./texture/paramètres.png").convert_alpha()
imagequit=pygame.image.load("./texture/quitter.png").convert_alpha()

# image menu 1 joueur
imagefacile=pygame.image.load("./texture/boutonfacile.png").convert_alpha()
imagemoyen=pygame.image.load("./texture/boutonmoyen.png").convert_alpha()
imagedifficile=pygame.image.load("./texture/boutondifficile.png").convert_alpha()
imageretour=pygame.image.load("./texture/retour.png").convert_alpha()

largeur = 10
hauteur = 10
couleur = (20, 180, 20)

def menu(img1,img2,img3,img4):
    ecran.blit(img1, (0, 0))
    ecran.blit(img2, (0, 125))
    ecran.blit(img3, (0, 250))
    ecran.blit(img4, (0, 375))
    
    pygame.display.update(0,0, 500, 100)
    pygame.display.update(0,125, 500, 100)
    pygame.display.update(0,250, 500, 100)
    pygame.display.update(0,375, 500, 100)
    

continuer = True
variable = True
while continuer:
    if variable:
        menu(image1J,image2J,imagepara,imagequit)
    
    for event in pygame.event.get():
        x,y=pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and (0 <= y <= 100):
            
            print("soupe")   
            print(event)
            menu(imagefacile,imagemoyen,imagedifficile,imageretour)   
            variable = False
            

            jeu1j = True
            while jeu1j:
                for event in pygame.event.get():
                    x,y=pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONUP:
                            
                        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and (0 <= y <= 100):
                            jeu1j= False
                                
                        if event.type == pygame.MOUSEBUTTONUP and(0 <= x <= 500) and (125 <= y <= 225):
                            jeu1j= False
                            print("1")
                                
                        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and (250 <= y <= 350):
                            jeu1j= False
                                
                        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and (375 <= y <= 475):
                            
                            jeu1j= False
                            variable=True
                            print("quit")
                                
                    if event.type == pygame.QUIT:
                        jeu1j = False
                        continuer = False
            pygame.event.clear()
            
        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and (125 <= y <= 225):
            ecran.subsurface(0, 0, 500, 100).fill(0)
            ecran.subsurface(0, 125, 500, 100).fill(0) 
            ecran.subsurface(0, 250, 500, 100).fill(0) 
            ecran.subsurface(0, 375, 500, 100).fill(0)   
            variable = False
            pygame.display.update(0,0, 500, 100)
            print("2")
                
            
        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and (250 <= y <= 350):
            ecran.subsurface(0, 0, 500, 100).fill(0)
            ecran.subsurface(0, 125, 500, 100).fill(0) 
            ecran.subsurface(0, 250, 500, 100).fill(0) 
            ecran.subsurface(0, 375, 500, 100).fill(0)   
            variable = False
            pygame.display.update(0,0, 500, 100)
        print(event)
        if event.type == pygame.MOUSEBUTTONUP and (0 <= x <= 500) and (375 <= y <= 475):
            continuer = False
            print("soue")  
            
        if event.type == pygame.QUIT:
            continuer = False
            
        
    pygame.display.flip()

pygame.quit()
