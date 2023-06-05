import pygame
import sys

pygame.init() # Inicializa pygame

ventana = pygame.display.set_mode(size=(800,600)) # Tamaño ventana

pygame.display.set_caption("Prueba juego 0.1") # Titulo ventana

fps = pygame.time.Clock() # Guarda el frame rate

fuente_juego = pygame.font.Font(None, 50) # Crea nueva fuente

# Se usa .convert() para convertir la imagen importada a un
# formato mas eficiente para pygame. Usar .convert_alpha()
# si es una imagen con transparencias (.png)

### Surfaces ###

fondo_surface = pygame.image.load("sprites/fondo.jpg").convert() # Importa fondo

piso_surface = pygame.image.load("sprites/piso.jpg").convert() # Importa piso

texto_surface = fuente_juego.render("Score: ", False, "Blue") # Escribe texto con fuente creada

bala_surface = pygame.image.load("sprites/bala.png").convert_alpha() # Importa bala

paloma_surface = pygame.image.load("sprites/paloma.png").convert_alpha()

################

### Rectangles ###

bala_rectangulo = bala_surface.get_rect(center = (800,300))

paloma_rectangulo = paloma_surface.get_rect(center = (100,300))

##################

### Flags ###

flag_collide = True

#############

### Bucle principal ###

while True:

    ### Bucle de eventos ###

    for even in pygame.event.get(): 

        if even.type == pygame.QUIT: # Permite cerrar ventana
            pygame.quit() # Comando de Pygame para cerrar ventana
            exit() # Comando de Python para cerrar completamente

    ### Posiciona imagenes en la pantalla (surface, posicion(x,y)) ###

    ventana.blit(fondo_surface,(0,0)) 

    ventana.blit(piso_surface,(0,500))

    ventana.blit(texto_surface,(50,200))

    ventana.blit(bala_surface,bala_rectangulo) # Usa variable para definir eje X de forma dinamica

    ventana.blit(paloma_surface,paloma_rectangulo)

    ### Bala se mueve hacia la izquierda y reinicia cuando sale de la pantalla ###

    bala_rectangulo.left -= 4

    if bala_rectangulo.right <= 0: # Si la bala sale de la pantalla reinicia posicion

        bala_rectangulo.left = 800

    ### Si paloma choca con la bala, paloma desaparece ###

    if paloma_rectangulo.colliderect(bala_rectangulo) and flag_collide == True:

        paloma_rectangulo.left = -200

        flag_collide = False
    
    ### Movimientos teclado ###

    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_DOWN]:

        paloma_rectangulo.top += 4
    
    if key_input[pygame.K_UP]:

        paloma_rectangulo.bottom -= 4

    pygame.display.update() # Renderizar gráficos

    fps.tick(60) # Define el limite de frame rate

