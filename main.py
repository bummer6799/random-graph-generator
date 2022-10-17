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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    time.sleep(0.5)
    randInt = np.random.randint(low=1, high=10, size=(1))
    sourceList = ['A', 'B', 'C']
    source = random.randint(0, 2)
    print(sourceList[source], randInt)

    intrandint = int(randInt)

    y1 = ((y-40)-(intrandint*((y-40)/10)))

    pygame.draw.line(screen, (0,0,0), (40, y-40), (40, y1), width=8)

    pygame.display.flip()

pygame.quit()

