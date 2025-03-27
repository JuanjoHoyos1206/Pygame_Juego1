import pygame
import sys
# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sober Up")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Lógica del juego aquí
    
    # Renderizado
    pantalla.fill(NEGRO)
    
    # Dibujar elementos del juego aquí
    
    # Actualizar pantalla
    pygame.display.flip()
    
    # Limitar a 60 FPS
    reloj.tick(60)

# Salir de pygame
pygame.quit()
sys.exit()