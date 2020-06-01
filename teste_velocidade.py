import pygame
import ctypes
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
user32 = ctypes.windll.user32

#1366 768- tamanho da minha tela
sizeX = user32.GetSystemMetrics(0)
sizeY = user32.GetSystemMetrics(1) # tirando um pedaço que ultrapassa a tela

size = sizeX,sizeY
screen = pygame.display.set_mode(size)
#print(sizeY)
#print(sizeX)

x = int(sizeX/2)
y = int(sizeY/2)

inicio = 25

nextX = x - inicio 
nextY = y - inicio 
print(nextX)
print(nextY)

#nome da janela
pygame.display.set_caption("Calibração")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

i = 1
py = 0
px = 0

# como o relógio do pygame trabalha
# em milissegundos, dividimos por 1000
# para manter os 100 pixels por segundo
velocity_x = 0.1

# criamos uma instância do relógio
clock = pygame.time.Clock()

# -------- Main Program Loop -----------

while done == False:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)
    # chamamos o tick do relógio para 30 fps
    # e armazenamos o delta de tempo
    dt = clock.tick(30)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    px += velocity_x * dt

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [px, py, 50, 50])

    pygame.display.flip()