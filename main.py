import pygame

pygame.init()

width = 1000
height = 800
screen = pygame.display.set_mode((width,height))

player = pygame.Rect((300,250,50,50))

lets_continue = True

while lets_continue:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (130,180,200), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
          player.move_ip(0, -1)

    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
          player.move_ip(0, 1)
          
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
          player.move_ip(1, 0)
          
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
          player.move_ip(-1, 0)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and key[pygame.K_w]:
          player.move_ip(0, -10)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and key[pygame.K_s]:
          player.move_ip(0, 10)
 
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and key[pygame.K_d]:
          player.move_ip(10, 0)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and key[pygame.K_a]:
          player.move_ip(-10, 0)

    for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                  lets_continue = False
    pygame.display.update()

pygame.quit()