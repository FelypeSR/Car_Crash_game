#todas as fuções atendidas
#porém o aviso de tela não dura mais de 2 segundos
#optei por não mexer, pois quando as alterações eram feitas, os blocos de obstáculos não funcionavam. 


import pygame
import random

# Aqui faço a inicialização da biblioteca Pygame
pygame.init()

# Determinei 800x600 mas vc pode aplicar a resolução que achar melhor 
largura_tela = 1280
altura_tela = 720
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Car Crash')
#background 
background = pygame.image.load('pista.png')
background = pygame.transform.scale(background, (largura_tela, altura_tela))
#background inserido com sucesso
#som de batida#
crash_song = pygame.mixer.Sound('uh.mpeg')
#volume
crash_song.set_volume(0.5)
#gameoverscreen
gameoverscreen = pygame.image.load('gameover.png')
#song car

#aviso de velocidade
temporizador_aviso_velocidade = pygame.time.get_ticks()
duracao_aviso_velocidade = 60000





            
# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Aqui coloquei separado para ajustar as configurações do carro
carro_largura = 80
carro = pygame.image.load('carro3.png')  
carro = pygame.transform.scale(carro, (carro_largura, 100))

# Posição inicial do carro
x = (largura_tela * 0.45)
y = (altura_tela * 0.8)

# Configurações dos obstáculos
obstaculo_largura = 50
obstaculo_altura = 100
obstaculo_cor = (255, 0, 0)  # Veja que é usado o padrão RGB, não preciso entrar em detalhes, certo?
obstaculo_velocidade = 7 # Falarei disso na sala (Será também uma implementação como Atividade)
obstaculo_x = random.randrange(0, largura_tela)
obstaculo_y = -600
contador_obstaculos = 0

# Desenhando os obstáculos [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def desenha_obstaculo(x, y, largura, altura, cor):
    pygame.draw.rect(tela, cor, [x, y, largura, altura])
    if y < obstaculo_y and x < obstaculo_x + obstaculo_largura or x + carro_largura < obstaculo_x + obstaculo_largura:
        jogo_ativo = False 







# Redesenhando a tela [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def redesenhar_tela():
    tela.fill(branco)
    tela.blit(background, (0,0))
    tela.blit(carro, (x, y))
  
    
    desenha_obstaculo(obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura, obstaculo_cor)
    pygame.display.update()
#função em que ao bater nos obstaculos, o carro para
def colidir(x, y, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura):
    if y < obstaculo_y + obstaculo_altura and y + 100 > obstaculo_y:
        if x > obstaculo_x and x < obstaculo_x + obstaculo_largura or x + carro_largura > obstaculo_x and x + carro_largura < obstaculo_x + obstaculo_largura:
            return True
    return False

#trabalhar esta função//def exibir_game_over():
    tela.blit(gameoverscreen, ((largura_tela - gameoverscreen.get_width()) // 2, (altura_tela - gameoverscreen.get_height()) // 2))
    pygame.display.update()

#mostra o aviso de velocidade, notificando que foi aumentada
def exibir_aviso_velocidade():  
   
    #global temporizador_aviso_velocidade 
    fonte = pygame.font.Font(None, 40)
    aviso_texto = fonte.render('Vamos mais rápido!', True, (255, 0, 0))
    tela.blit(aviso_texto, ((largura_tela - aviso_texto.get_width()) // 2, 50))
    aviso_velocidade = True
    pygame.display.update()


     #Inicia o temporizador do aviso
    temporizador_aviso_velocidade = duracao_aviso_velocidade 





      


           

# Parte principal do jogo (aqui executo a criação do loop)

jogo_ativo = True
verificar_colisao = False #impede que o jogo feche após a colisão
clock = pygame.time.Clock()


while jogo_ativo:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

         


    
    #alteração 1: concluída
    keys = pygame.key.get_pressed()
    #para corrigir o movimento de sair da tela, é preciso limitar o espaço de movimento
    if keys[pygame.K_LEFT] and x >0:
        x -= 5
    # o eixo x de movimento deve ser menor que a largura da tela menos a largura do carro
    if keys[pygame.K_RIGHT] and x < largura_tela - carro_largura:
        x += 5

    obstaculo_y += obstaculo_velocidade
    if obstaculo_y > altura_tela:
        obstaculo_y = 0 - obstaculo_altura
        obstaculo_x = random.randrange(0, largura_tela)
        # Verifica colisão
        # Incrementar o contador de obstáculos
        contador_obstaculos += 1
        
        # Aumentar a velocidade após 10 obstáculos
        if contador_obstaculos >= 10:
            obstaculo_velocidade = 10  # Altere para a velocidade desejada
            #exibir_aviso_velocidade()
        if contador_obstaculos >=1:
            obstaculo_velocidade = 10 # Altere para a velocidade desejada
        
            exibir_aviso_velocidade() # print

            
    if colidir(x, y, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura):
        verificar_colisao = True
        crash_song.play()
        #tela.blit(gameoverscreen)
        
    
   
        #se verificar_colisao for definido como false, o movimento de colidir não é incrementado
       
    redesenhar_tela()
    clock.tick(60)
    

    #se colidir 
    while verificar_colisao:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_ativo = False
                verificar_colisao= False  # Garante que o loop interno seja interrompido ao fechar o jogo
                

pygame.quit()