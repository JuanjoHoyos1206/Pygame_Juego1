import pygame
import os  # Importamos os para manejar rutas relativas

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sober up")

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Propiedades del personaje
player_size = 30
player_x = WIDTH // 2 - 14
player_y = HEIGHT // 2 + 80
player_speed = 1.5
isKnifetaken = False

# Diccionario para el estado de las teclas
keys = {"left": False, "right": False, "up": False, "down": False, "h": False}

# Rutas relativas
ruta_base = os.path.dirname(__file__)  # Obtiene la carpeta donde está el script
ruta_background = os.path.join(ruta_base, "background1.png")
ruta_knife = os.path.join(ruta_base, "cuchillo2.png")

# Cargar imágenes con rutas relativas
background = pygame.image.load(ruta_background)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

cuchillo_WIDHT, cuchillo_HEIGHT = 30, 30
knife = pygame.image.load(ruta_knife)
knife = pygame.transform.scale(knife, (cuchillo_WIDHT, cuchillo_HEIGHT))

# Posición inicial del cuchillo
knife_x, knife_y = 185, 155

# Bucle del juego
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Limpiar pantalla
    screen.blit(background, (0, 0))

    if isKnifetaken:
        screen.blit(knife, (player_x + 2, player_y - 30))
    else:
        screen.blit(knife, (knife_x, knife_y))

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                keys["left"] = True
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                keys["right"] = True
            if event.key in (pygame.K_UP, pygame.K_w):
                keys["up"] = True
            if event.key in (pygame.K_DOWN, pygame.K_s):
                keys["down"] = True
            if event.key == pygame.K_h:
                is_near_knife = (
                    player_x + player_size >= knife_x
                    and player_x <= knife_x + cuchillo_WIDHT
                    and player_y + player_size >= knife_y
                    and player_y <= knife_y + cuchillo_HEIGHT
                )
                if is_near_knife and not isKnifetaken:
                    keys["h"] = True
                    isKnifetaken = True
                elif isKnifetaken:
                    isKnifetaken = False
                    knife_x, knife_y = player_x, player_y

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                keys["left"] = False
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                keys["right"] = False
            if event.key in (pygame.K_UP, pygame.K_w):
                keys["up"] = False
            if event.key in (pygame.K_DOWN, pygame.K_s):
                keys["down"] = False
            if event.key == pygame.K_h:
                keys["h"] = False

    # Actualizar posición del personaje
    ruta_player = os.path.join(ruta_base, "playerdown.png")  # Por defecto, mirando hacia abajo

    if keys["left"] and player_x > 1:
        player_x -= player_speed
        ruta_player = os.path.join(ruta_base, "playerleft.png")
    if keys["right"] and player_x < WIDTH - player_size:
        player_x += player_speed
        ruta_player = os.path.join(ruta_base, "playerright.png")
    if keys["up"] and player_y > 1:
        player_y -= player_speed
        ruta_player = os.path.join(ruta_base, "playerup.png")
    if keys["down"] and player_y < HEIGHT - player_size:
        player_y += player_speed
        ruta_player = os.path.join(ruta_base, "playerdown.png")

    # Dibujar personaje con ruta relativa
    player_img = pygame.image.load(ruta_player)
    player_img = pygame.transform.scale(player_img, (player_size, player_size))
    screen.blit(player_img, (player_x, player_y))

    pygame.display.flip()  # Actualizar pantalla
    clock.tick(60)  # Limitar FPS a 60

pygame.quit()
