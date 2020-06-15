#Projeto Jogos Amaury & Gabriel
#Snack Time!
import pygame
import sys
from random import *

pygame.init()

#Tela do jogo
screen = pygame.display.set_mode((900, 500))
surface = screen.subsurface((0,0),(900,500))
pygame.display.set_caption("Snack Time")

#Upload das imagens/Fundo/Personagem/


char = pygame.image.load('gael h.png')
andarDir = [pygame.image.load('gael h.png')]
andarEsq = [pygame.image.load('gael esq.png')]
andarDir1 = [pygame.image.load('TDP W.png')]
andarEsq1 = [pygame.image.load('TDP H.png')]
andarDir2 = [pygame.image.load('Amy W.png')]
andarEsq2 = [pygame.image.load('Amy H.png')]
pizza = [pygame.image.load('3.png')]
brocolis = [pygame.image.load('6.png')]

bg = pygame.image.load('bg1.jpg')
menu = pygame.image.load('Menu.jpg')
info = pygame.image.load('Continuar.jpg')
ranking = pygame.image.load('Ranking.jpg')
bg2 = pygame.image.load('bg2.jpg')
bg3 = pygame.image.load('bg3.jpg')

#Variáveis de Tempo e Pontuacao
pontos = 0
temporizador = 0
YELLOW = (255, 255, 0)
clock = pygame.time.Clock()
xBuff = randrange(30,700)
yBuff = 440

#Variáveis Sound Effects
#tiroSound = pygame.mixer.Sound('')
#hitSound = pygame.mixer.Sound('')
musicas = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


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
            

        elif self.dire:
            screen.blit(andarDir[self.andarCont//3], (self.x, self.y))
            

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

#Bufado
    def buff(self):
        print('buffinho')
        if self.vel >= 1 and self. vel < 8:
            self.vel += 1
        else:
            print('velocidae máxima atingida')
            
            
        

        
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
        
        screen.blit(pizza[0], (self.x, self.y))
        

#Classe dos powerups
class powerUp(object):
    def __init__(self, x, y, radius,color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        screen.blit(brocolis[0], (self.x, self.y))

    
#GameWindow elementos que aparecem na tela
def redrawGameWindow():
    #screen.blit(bg, (0, 0))
    ##screnn.blit(fase02, (0, 0))
    ##screen.blit(menu, (0, 0))
    texto = font.render('Score: ' + str(pontos),1, (0,0,0))
    screen.blit(texto, (390,10))
    timer1 = font.render('Tempo: ' + str(temporizador), True, (YELLOW))
    screen.blit(timer1,(750,10))
    ch.draw(screen)
    npc.draw(screen)
    for buff in buffs:
        buff.draw(screen)
    for tiro in tiros:
        tiro.draw(screen)
    pygame.display.update()




#Instancia/Personagem/Imigos/Tiros/DirecaoDoTiro
font = pygame.font.SysFont('comicsans', 30, True)
ch = personagem(3, 430, 80, 80) #posição de inicio do personagem
npc = inimigo(30, 30, 64, 64, 850) #posição de inicio do inimigo


buffs = []
buffLoop = 0

tiroLoop = 0
tiros = []
facing = 1
jogandoOn  = False
jogandoOn2 = False
jogandoOn3 = False
rankingOn = False
continuarOn = False
menuOn = True
fase01 = False
fase02 = False
fase03 = False

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) #Configurado o time do Pygame para execução a cada 1s



#-------------------------------------Loop principal----------------------------------------------------------


#Tele de menu
while menuOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Jogar Click Event, ao clicar o jogador inicia o jogo
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            print(pygame.mouse.get_pos())
            if x > 374 and y > 213 and x < 532 and y < 256:
                menuOn = False
                continuarOn = True
                #jogandoOn = True
                #fase01 = True
                print('Jogo Iniciado')
            
           #Ranking Click Event, ao Clicar o jogador visualiza a tela de ranking
            elif x > 374 and y > 288 and x < 532 and y < 328:
                menuOn = False
                rankingOn = True
                print('Tela de Ranking')

            #Sair Click Event, fecha o jogo
            elif x > 374 and y > 360 and x < 532 and y < 400:
                menuOn = False
                pygame.quit()
                sys.exit()            
                
        screen.blit(menu, (5, 5))       
        #Atualizando a tela para inicio do jogo
        pygame.display.update()   
        pygame.display.flip()


#Tela de informações
while continuarOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Informações Click Event
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            print(pygame.mouse.get_pos())
            if x > 383 and y > 400 and x < 522 and y < 500:
                jogandoOn = True
                continuarOn = False
                fase01 = True
            

        #Atualizando a tela para inicio do jogo
        screen.blit(info, (5, 5))       
        pygame.display.update()   
        pygame.display.flip()


###Ranking####
while rankingOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #Atualizando a tela para inicio do jogo
    screen.blit(ranking, (5,5))
    pygame.display.update()   
    pygame.display.flip()


###Jogando###
while jogandoOn and fase01:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(27)

    if tiroLoop > 0:
        tiroLoop += 1
    if tiroLoop > 1:
        tiroLoop = 0

    #Fechando a tela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogandoOn = False

        #capturando evento do cronometro a cada 1s e atualizando a variável contadora
        if event.type == CLOCKTICK:
            temporizador = temporizador + 1

    #Disparos do inimigo(NPC)
    for tiro in tiros:
        if tiro.y + tiro.radius < ch.hitbox[1] + ch.hitbox[3] and tiro.y + tiro.radius > ch.hitbox[1]:
            if tiro.x + tiro.radius > ch.hitbox[0] and tiro.x - tiro.radius < ch.hitbox[0] + ch.hitbox[2]:
                #hitSound.play()
                ch.hit()
                tiros.pop(tiros.index(tiro))
                pontos += 1

        if tiro.y < 500 and tiro.y > 0:
            tiro.y += tiro.vel
        else:
            
            tiros.pop(tiros.index(tiro)) 
        
    if jogandoOn and tiroLoop == 0:
        if len(tiros) < 5:
            tiros.append(municao(round(npc.x + npc.width //2), round(npc.y + npc.height//2), 4, (255,0,0), facing))
            #bulletSound.play()
        tiroLoop = 1
        
    #Buffs espalhados pelo mapa
    if buffLoop >0:
        buffLoop += 1
    if buffLoop >1:
        buffLoop = 0
        
    for buff in buffs:  
        if buff.y + buff.radius < ch.hitbox[1] + ch.hitbox[3] and buff.y + buff.radius > ch.hitbox[1]:
            if buff.x + buff.radius > ch.hitbox[0] and buff.x - buff.radius < ch.hitbox[0] + ch.hitbox[2]:
                print('bufado')
                ch.buff()
        else:
            buffs.pop(buffs.index(buff))
    if jogandoOn and buffLoop == 0:
        if len(buffs) < 5:
            buffs.append(powerUp(round(xBuff), round(yBuff), 6, (0,255,0), facing))
        buffLoop = 1

    #Movimentando o Personagem
    keys = pygame.key.get_pressed()
    
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
    if ch.x > 800 and ch.x < 900 and ch.y > 400 and ch.y < 500:
        print ('segunda fase')
        fase01 = False
        jogandoOn = False
        jogandoOn2 = True
        fase02 = True
    #Atualizando a tela para inicio do jogo
    screen.blit(bg, (0,0))
    pygame.display.update()   
    pygame.display.flip()
    redrawGameWindow()
    
    
     
########################################--------- FASE 02 -------############################################
while jogandoOn2 and fase02:
    
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    if tiroLoop > 0:
        tiroLoop += 1
    if tiroLoop > 1:
        tiroLoop = 0

    #Fechando a tela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogandoOn = False

        #capturando evento do cronometro a cada 1s e atualizando a variável contadora
        if event.type == CLOCKTICK:
            temporizador = temporizador + 1

    #Disparos do inimigo(NPC)
    for tiro in tiros:
        if tiro.y + tiro.radius < ch.hitbox[1] + ch.hitbox[3] and tiro.y + tiro.radius > ch.hitbox[1]:
            if tiro.x + tiro.radius > ch.hitbox[0] and tiro.x - tiro.radius < ch.hitbox[0] + ch.hitbox[2]:
                #hitSound.play()
                ch.hit()
                tiros.pop(tiros.index(tiro))
                pontos += 1

        if tiro.y < 500 and tiro.y > 0:
            tiro.y += tiro.vel
        else:
            
            tiros.pop(tiros.index(tiro)) 
        
    if jogandoOn and tiroLoop == 0:
        if len(tiros) < 5:
            tiros.append(municao(round(npc.x + npc.width //2), round(npc.y + npc.height//2), 4, (255,0,0), facing))
            #bulletSound.play()
        tiroLoop = 1
        
    #Buffs espalhados pelo mapa
    if buffLoop >0:
        buffLoop += 1
    if buffLoop >1:
        buffLoop = 0
        
    for buff in buffs:  
        if buff.y + buff.radius < ch.hitbox[1] + ch.hitbox[3] and buff.y + buff.radius > ch.hitbox[1]:
            if buff.x + buff.radius > ch.hitbox[0] and buff.x - buff.radius < ch.hitbox[0] + ch.hitbox[2]:
                print('Ta bufado lek')
                ch.buff()
        else:
            buffs.pop(buffs.index(buff))
    if jogandoOn and buffLoop == 0:
        if len(buffs) < 5:
            buffs.append(powerUp(round(xBuff), round(yBuff), 6, (0,255,0), facing))
        buffLoop = 1

    #Movimentando o Personagem
    keys = pygame.key.get_pressed()
    
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
    if ch.x >= 800 and ch.x <= 900 and ch.y >= 400 and ch.y <= 500:
        print ('terceira fase')
        fase02 = False
        jogandoOn2 = False
        jogandoOn3 = True
        fase03 = True
    #Atualizando a tela para inicio do jogo
    screen.blit(bg2, (0,0))
    pygame.display.update()   
    pygame.display.flip()
    redrawGameWindow()        

########################################--------- FASE 03 -------############################################
while jogandoOn3 and fase03:
    
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    if tiroLoop > 0:
        tiroLoop += 1
    if tiroLoop > 1:
        tiroLoop = 0

    #Fechando a tela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogandoOn = False

        #capturando evento do cronometro a cada 1s e atualizando a variável contadora
        if event.type == CLOCKTICK:
            temporizador = temporizador + 1

    #Disparos do inimigo(NPC)
    for tiro in tiros:
        if tiro.y + tiro.radius < ch.hitbox[1] + ch.hitbox[3] and tiro.y + tiro.radius > ch.hitbox[1]:
            if tiro.x + tiro.radius > ch.hitbox[0] and tiro.x - tiro.radius < ch.hitbox[0] + ch.hitbox[2]:
                #hitSound.play()
                ch.hit()
                tiros.pop(tiros.index(tiro))
                pontos += 1

        if tiro.y < 500 and tiro.y > 0:
            tiro.y += tiro.vel
        else:
            
            tiros.pop(tiros.index(tiro)) 
        
    if jogandoOn and tiroLoop == 0:
        if len(tiros) < 5:
            tiros.append(municao(round(npc.x + npc.width //2), round(npc.y + npc.height//2), 4, (255,0,0), facing))
            #bulletSound.play()
        tiroLoop = 1
        
    #Buffs espalhados pelo mapa
    if buffLoop >0:
        buffLoop += 1
    if buffLoop >1:
        buffLoop = 0
        
    for buff in buffs:  
        if buff.y + buff.radius < ch.hitbox[1] + ch.hitbox[3] and buff.y + buff.radius > ch.hitbox[1]:
            if buff.x + buff.radius > ch.hitbox[0] and buff.x - buff.radius < ch.hitbox[0] + ch.hitbox[2]:
                print('Ta bufado lek')
                ch.buff()
        else:
            buffs.pop(buffs.index(buff))
    if jogandoOn and buffLoop == 0:
        if len(buffs) < 5:
            buffs.append(powerUp(round(xBuff), round(yBuff), 6, (0,255,0), facing))
        buffLoop = 1

    #Movimentando o Personagem
    keys = pygame.key.get_pressed()
    
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
    if ch.x > 800 and ch.x < 900 and ch.y > 400 and ch.y < 500:
        print ('segunda fase')
        fase01 = False
        jogandoOn = False
        jogandoOn2 = True
        fase02 = True
    #Atualizando a tela para inicio do jogo
    screen.blit(bg3, (0,0))
    pygame.display.update()   
    pygame.display.flip()
    redrawGameWindow()  
        
#Prenchimentos da surface  
    

    



pygame.quit()
