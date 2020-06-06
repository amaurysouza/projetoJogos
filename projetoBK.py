#Projeto Jogos Amaury & Gabriel
#Snack Time!
import pygame

pygame.init()

#Tela do jogo
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Snack Time")

#Upload das imagens/Fundo/Personagem
andarDir = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
andarEsq = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')

#inimigo"
andarDir1 = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
andarEsq1 = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
bg = pygame.image.load('bg.jpg')
pontos = 0

clock = pygame.time.Clock()


#Personagem/Dimensoes/CaracteristicasFisicas"
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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

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
            
        self.hitbox = (self.x + 17, self.y, 31, 57)
        #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)


#Hit
    def hit(self):
        print('hit')
        if self.vel > 1:
            print('velocidade reduzida')
            self.vel -= 1
           
        else:
            print('velocidade minima atingida')
            self.vel = 1
                                 
#Inimigo/Dimensoes/CaracteristicasFisicas
class inimigo(object):
   def __init__(self, x, y, width, height, end):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.end = end
       self.path = [self.x , self.end]
       self.andarCont = 0
       self.vel = 6
       self.hitbox = (self.x + 17, self.y +2, 31, 57)

   def draw(self,screen):
       self.move()
       if self.andarCont + 1 <= 33:
           self.andarCont = 0

       if self.vel > 0:
           screen.blit(andarDir1[self.andarCont //3], (self.x, self.y))
           self.andarCont += 1

       else:
           screen.blit(andarEsq1[self.andarCont //3], (self.x, self.y))
           self.andarCont += 1          

       self.hitbox = (self.x + 17, self.y, 29, 52)
       #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

   def move(self):
       if self.vel > 0:
           if self.x + self.vel < self.path[1]:
               self.x += self.vel
           else:
               self.vel = self.vel * -1
               self.andarCont = 0
       else:
           if self.x - self.vel > self.path[0]:
               self.x += self.vel
           else:
               self.vel = self.vel * -1
               self.andarCont = 0
        
                 
#Classe dos disparos
class municao(object):
    def __init__(self,x, y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
        

    
#GameWindow
def redrawGameWindow():
    screen.blit(bg, (0, 0))
    texto = font.render('Score: ' + str(pontos),1, (0,0,0))
    screen.blit(texto, (390,10))
    ch.draw(screen)
    npc.draw(screen)
    for tiro in tiros:
        tiro.draw(screen)
    pygame.display.update()



#Loop principal
#Instancia/Personagem/Imigos/Tiros/DirecaoDoTiro
font = pygame.font.SysFont('comicsans', 30, True)
ch = personagem(3, 400, 64, 64)
npc = inimigo(3, 3, 64, 64, 850)
tiroLoop = 0
tiros = []
facing = 1
jogando  = True
while jogando:
    clock.tick(27)

    if tiroLoop > 0:
        tiroLoop += 1
    if tiroLoop > 3:
        tiroLoop = 0

#Fechando a tela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    for tiro in tiros:
        if tiro.y + tiro.radius < ch.hitbox[1] + ch.hitbox[3] and tiro.y + tiro.radius > ch.hitbox[1]:
            if tiro.x + tiro.radius > ch.hitbox[0] and tiro.x - tiro.radius < ch.hitbox[0] + ch.hitbox[2]:
                ch.hit()
                tiros.pop(tiros.index(tiro))
                pontos += 1

        if tiro.y < 500 and tiro.y > 0:
            tiro.y += tiro.vel
        else:
            
            tiros.pop(tiros.index(tiro))
        
#Movimentando o Personagem
    keys = pygame.key.get_pressed()

    if jogando and tiroLoop == 0:
        if len(tiros) < 5:
            tiros.append(municao(round(npc.x + npc.width //2), round(npc.y + npc.height//2), 4, (255,0,0), facing))

        tiroLoop = 1
    
    if keys[pygame.K_LEFT] and ch.x > ch.vel:
        ch.x -= ch.vel
        ch.esq = True
        ch.dire = False
        
    elif keys[pygame.K_RIGHT] and ch.x < 900 - ch.width - ch.vel:
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
            

            
            
    redrawGameWindow()     
#Prenchimentos da surface  
    

    



pygame.quit()
