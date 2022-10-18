import numpy as np
import time
import string
import random
import pygame

pygame.init()

x = 800
y = 600
screen = pygame.display.set_mode([x, y])

running = True

global memA, memB, memC

memA = 0
memB = 0
memC = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    time.sleep(0.025)
    randInt = np.random.randint(low=1, high=10, size=(1))
    sourceList = ['A', 'B', 'C']
    source = random.randint(0, 2)
    intrandint = int(randInt)
    mainsource = (sourceList[source], intrandint)

    print(mainsource)

    if sourceList[source] == 'A':
        #global memA
        memA = intrandint

    if sourceList[source] == 'A':
        yA = ((y - 40) - (intrandint * ((y - 40) / 10)))
        pygame.draw.line(screen, (0, 0, 0), (40, y - 40), (40, yA), width=8)
    else:
        yA = ((y - 40) - (memA * ((y - 40) / 10)))
        pygame.draw.line(screen, (0, 0, 0), (40, y - 40), (40, yA), width=8)

    pygame.display.flip()

    if sourceList[source] == 'B':
        #global memB
        memB = intrandint

    if sourceList[source] == 'B':
        yB = ((y - 40) - (intrandint * ((y - 40) / 10)))
        pygame.draw.line(screen, (0, 0, 0), (80, y - 40), (80, yB), width=8)
    else:
        yB = ((y - 40) - (memB * ((y - 40) / 10)))
        pygame.draw.line(screen, (0, 0, 0), (80, y - 40), (80, yB), width=8)

    pygame.display.flip()

pygame.quit()
