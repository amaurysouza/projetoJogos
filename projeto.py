#Projeto Jogos Amaury & Gabriel
#Snack Time!
import pygame

pygame.init()

#Tela do jogo
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snack Time")

#Upload das imagens/Fundo/Personagem
andarDir = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
andarEsq = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

#EIXO X / Y Vel Speed 
x = 50
y = 405
width = 64
height = 64
vel = 5

#Variables
isJump = False
jumpCount = 10
esq = False
dire = False
andarCont = 0


def redrawGameWindow():
    global andarCont  
    screen.blit(bg, (0, 0))

    if andarCont + 1 >= 27:
        andarCont = 0

    if esq:
        screen.blit(andarEsq[andarCont//3], (x,y))
        andarCont += 1

    elif dire:
        screen.blit(andarDir[andarCont//3], (x,y))
        andarCont += 1

    else:
        screen.blit(char, (x,y))
    
    pygame.display.update()




#Loop principal
jogando  = True
while jogando:
    clock.tick(27)

#Fechando a tela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

#Movimentando o Personagem
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        esq = True
        dire = False
        
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        dire = True
        esq = False
        
    else:
        dire = False
        esq = False
        andarCont = 0
        
    if not(isJump):    
        if keys[pygame.K_UP]:
            isJump = True
            esq = False
            dire = False
            andarCont = 0
            
    else:
        if jumpCount >= - 10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
            
        else:
            isJump = False
            jumpCount = 10
    redrawGameWindow()     
#Prenchimentos da surface  
    

    



pygame.quit()
