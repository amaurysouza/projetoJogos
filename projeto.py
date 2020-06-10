#Projeto Jogos Amaury & Gabriel
#Snack Time!
import pygame

pygame.init()

#Tela do jogo
screen = pygame.display.set_mode((1500, 1500))
pygame.display.set_caption("Snack Time")

#Upload das imagens/Fundo/Personagem
andarDir = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
andarEsq = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')


#inimigo
andarDir1 = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
andarEsq1 = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]

char1 = pygame.image.load('R11E.png')

clock = pygame.time.Clock()
bg = pygame.image.load('bg1.jpg')


#Personagem/Dimensoes/CaracteristicasFisicas
class personagem(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.esq = False
        self.dire = False
        self.andarCont = 0

#Movimentacao visual do personagem
    def draw(self,screen):
        if self.andarCont + 1 >= 27:
            self.andarCont = 0

        if self.esq:
            screen.blit(andarEsq[self.andarCont//3], (self.x, self.y))
            self.andarCont += 1

        elif self.dire:
            screen.blit(andarDir[self.andarCont//3], (self.x, self.y))
            self.andarCont += 1

        else:
            screen.blit(char, (self.x, self.y))

#Inimigo/Dimensoes/CaracteristicasFisicas
class inimigo(object):
    def __init__(self, x1, y1, width1, height1, end):
        self.x1 = x1
        self.y1 = y1
        self.width1 = width1
        self.height1 = height1
        self.end = end
        self.path = [self.x1 , self.end]
        self.vel1 = 5
        #self.esq1 = False
        #self.dire1 = False
        self.andarCont1 = 0
        #self.standing  = True
        
        
#Movitacao visual do inimigo
    def draw(self, screen):
        self.move()
        if self.andarCont1 + 1 <= 33:
            self.andarCont1 = 0

        if self.vel1 > 0:
            screen.blit(andarDir1[self.andarCont1//3], (self.x1 , self.y1))
            self.andarCont1 += 1

        else:
            screen.blit(andarEsq1[self.andarCont1//3], (self.x1 , self.y1))
            self.andarCont1 += 1

         #if self.andarCont1 + 1 >= 27:
          #   self.andarCont1 = 0
             
             
         #if not(self.standing):
          #   if self.esq1:
           #      screen.blit(andarEsq1[self.andarCont1//3], (self.x1, self.y1))
            #     self.andarCont1 += 1

             #elif self.dire1:
              #   screen.blit(andarDir1[self.andarCont1//3], (self.x1 , self.y1))
               #  self.andarCont1 += 1

         #else:
          #   screen.blit(char1, (self.x1, self.y1))
    def move(self):
        if self.vel1 > 0:
            if self.x1 + self.vel1 < self.path[1]:
                self.x1 ++ self.vel1
            else:
                self.vel1 = self.vel1 * -1
                self.andarCont1 = 0
        else:
            if self.x1 - self.vel1 > self.path[0]:
                self.x1 += self.vel1
            else:
                self.vel1 = self.vel1 * -1
                self.andarCont1 = 0
                
                 
#Tiros
class municao(object):
    def __init__(self,x, y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        

#Obstaculos
class obstaculo(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    
      

    
#Janela do Jogo
def redrawGameWindow():
    screen.blit(bg, (0, 0))
    ch.draw(screen)
    ch1.draw(screen)
   
    for tiro in tiros:
        tiro.draw(screen)
    pygame.display.update()







#Instancia/Personagem/Imigos/Tiros/DirecaoDoTiro
ch = personagem(200, 400, 64, 64)
ch1 = inimigo(3, 3, 64, 64, 450)
tiros = []
facing = 1
#Loop principal
jogando  = True
while jogando:
    clock.tick(27)
    

#Fechando a tela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    for tiro in tiros:
        if tiro.y < 500 and tiro.y > 0:
            tiro.y += tiro.vel
        else:
            tiros.pop(tiros.index(tiro))
        
#Movimentando o Personagem
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        #if ch1.esq1:
         #   facing = -1
        #else:
         #   facing = 1
        
        if len(tiros) < 5:
            tiros.append(municao(round(ch1.x1 + ch1.width1 // 2), round(ch1.y1 + ch1.height1//2), 6,(255,0,0) , facing ))
            
    
    if keys[pygame.K_LEFT] and ch.x > ch.vel:
        ch.x -= ch.vel
        ch.esq = True
        ch.dire = False
        
    elif keys[pygame.K_RIGHT] and ch.x < 500 - ch.width - ch.vel:
        ch.x += ch.vel
        ch.dire = True
        ch.esq = False
        
    else:
        ch.dire = False
        ch.esq = False
        ch.andarCont = 0
        
    if not(ch.isJump):    
        if keys[pygame.K_UP]:
            ch.isJump = True
            ch.esq = False
            ch.dire = False
            ch.andarCont = 0
            
    else:
        if ch.jumpCount >= - 10:
            neg = 1
            if ch.jumpCount < 0:
                neg = -1
            ch.y -= (ch.jumpCount ** 2) * 0.5 * neg
            ch.jumpCount -= 1
            
        else:
            ch.isJump = False
            ch.jumpCount = 10

#movimentando o inimigo
            
    if keys[pygame.K_LEFT] and ch1.x1 > ch1.vel1:
        ch1.x1 -= ch1.vel1
        ch1.esq1 = True
        ch1.dire1 = False
        ch1.standing = False
        
    elif keys[pygame.K_RIGHT] and ch1.x1 < 500 - ch1.width1 - ch1.vel1:
        ch1.x1 += ch1.vel1
        ch1.dire1 = True
        ch1.esq1 = False
        ch1.standing = False
        
    else:
        ch1.standing = True
        ch1.andarCont1 = 0
        
            
            
    redrawGameWindow()     
#Prenchimentos da surface  
    

    



pygame.quit()
