import pygame
import sys

# Inicializar Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 200)
GRIS = (180, 180, 180)

# Pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sober Up")

# Fuente
fuente = pygame.font.SysFont("Times New Roman", 48)
fuente_pequeña = pygame.font.SysFont("Times New Roman", 32)

# Opciones de menú
opciones = ["Iniciar Juego", "Instrucciones", "Salir"]
opcion_seleccionada = 0

def dibujar_menu():
    pantalla.fill(GRIS)
    titulo = fuente.render("Sober Up", True, AZUL)
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 100))
    
    for i, texto in enumerate(opciones):
        color = AZUL if i == opcion_seleccionada else NEGRO
        texto_render = fuente_pequeña.render(texto, True, color)
        pantalla.blit(texto_render, (ANCHO//2 - texto_render.get_width()//2, 250 + i * 60))

    pygame.display.flip()

def juego():
    import os

    WIDTH, HEIGHT = 900, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sober Up")

    WHITE = (255, 255, 255)
    ASSETS_DIR = "Principal_Tiles"

    background = pygame.image.load(os.path.join(ASSETS_DIR, "background1.png"))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    cuchillo_WIDHT, cuchillo_HEIGHT = 30, 30
    cuchillo = pygame.image.load(os.path.join(ASSETS_DIR, "cuchillo2.png"))
    cuchillo = pygame.transform.scale(cuchillo, (cuchillo_WIDHT, cuchillo_HEIGHT))

    player_size = 30
    player_x = WIDTH // 2 - 14
    player_y = HEIGHT // 2 + 80
    player_speed = 1.8
    isKnifetaken = False

    knife_x, knife_y = 185, 155
    keys = {"left": False, "right": False, "up": False, "down": False, "h": False}
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        if isKnifetaken:
            screen.blit(cuchillo, (player_x + 2, player_y - 30))
        else:
            screen.blit(cuchillo, (knife_x, knife_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a): keys["left"] = True
                if event.key in (pygame.K_RIGHT, pygame.K_d): keys["right"] = True
                if event.key in (pygame.K_UP, pygame.K_w): keys["up"] = True
                if event.key in (pygame.K_DOWN, pygame.K_s): keys["down"] = True
                if event.key == pygame.K_h:
                    is_near_knife = (
                        player_x + player_size >= knife_x and
                        player_x <= knife_x + cuchillo_WIDHT and
                        player_y + player_size >= knife_y and
                        player_y <= knife_y + cuchillo_HEIGHT
                    )
                    if is_near_knife and not isKnifetaken:
                        isKnifetaken = True
                    elif isKnifetaken:
                        isKnifetaken = False
                        knife_x, knife_y = player_x, player_y
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a): keys["left"] = False
                if event.key in (pygame.K_RIGHT, pygame.K_d): keys["right"] = False
                if event.key in (pygame.K_UP, pygame.K_w): keys["up"] = False
                if event.key in (pygame.K_DOWN, pygame.K_s): keys["down"] = False

        ruta = os.path.join(ASSETS_DIR, "playerdown.png")
        if keys["left"] and player_x > 1:
            player_x -= player_speed
            ruta = os.path.join(ASSETS_DIR, "playerleft.png")
        if keys["right"] and player_x < WIDTH - player_size:
            player_x += player_speed
            ruta = os.path.join(ASSETS_DIR, "playerright.png")
        if keys["up"] and player_y > 1:
            player_y -= player_speed
            ruta = os.path.join(ASSETS_DIR, "playerup.png")
        if keys["down"] and player_y < HEIGHT - player_size:
            player_y += player_speed
            ruta = os.path.join(ASSETS_DIR, "playerdown.png")

        player_img = pygame.image.load(ruta)
        player_img = pygame.transform.scale(player_img, (player_size, player_size))
        screen.blit(player_img, (player_x, player_y))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def main():
    global opcion_seleccionada
    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        dibujar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[opcion_seleccionada] == "Iniciar Juego":
                        juego()
                    elif opciones[opcion_seleccionada] == "Instrucciones":
                        print("Presiona las flechas para moverte y H para tomar el cuchillo")
                    elif opciones[opcion_seleccionada] == "Salir":
                        ejecutando = False

        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()