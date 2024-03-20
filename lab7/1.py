import pygame
from datetime import datetime

pygame.init()
W, H = 600, 500
screen = pygame.display.set_mode((W, H))
done = False
clock = pygame.time.Clock()
white = (255, 255, 255)

pygame.display.set_caption("Clock")

mickey = pygame.image.load("c:\\Users\\Администратор\\Downloads\\mainclock.png")
rightarm = pygame.image.load("c:\\Users\\Администратор\\Downloads\\rightarm.png")
leftarm = pygame.image.load("c:\\Users\\Администратор\\Downloads\\leftarm.png")

mickey2 = pygame.transform.scale(mickey, (600, 400))
ra = pygame.transform.scale(rightarm, (600, 600))
la = pygame.transform.scale(leftarm, (40, 450))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)
    m = mickey2.get_rect(center=(W//2, H//2))
    screen.blit(mickey2, m)
    t = datetime.now()
    sec_angle = -(t.second * 6)
    min_angle = -(t.minute * 6 + t.second * 0.1)

    rotated_ra = pygame.transform.rotate(ra, min_angle)
    rotated_la = pygame.transform.rotate(la, sec_angle)

    ra_rect = rotated_ra.get_rect(center=(W//2, H//2))
    la_rect = rotated_la.get_rect(center=(W//2, H//2))

    screen.blit(rotated_ra, ra_rect)
    screen.blit(rotated_la, la_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()