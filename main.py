import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

w, h = 700, 500
window = pygame.display.set_mode((w, h), pygame.RESIZABLE)

image = pygame.transform.scale(pygame.image.load("assets/background2.png"), (w,h))

class Player:
    def __init__(self, x, y, w, h, image):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = pygame.transform.scale(pygame.image.load(image), (20, 20))

    def hitbox(self):
        return pygame.rect.Rect(self.x, self.y, 20 , 20)

    def move(self, ):
        keys = pygame.key.get_pressed()
        x, y = self.x, self.y
        if keys[pygame.K_UP] | keys[pygame.K_w]:
            y -= 2
        elif keys[pygame.K_DOWN] | keys[pygame.K_s]:
            y += 2
        elif keys[pygame.K_LEFT] | keys[pygame.K_a]:
            x -= 2
        elif keys[pygame.K_RIGHT] | keys[pygame.K_d]:
            x += 2

        if (
                image.get_at((x, y)) == (255, 255, 255) and
                image.get_at((x + self.w, y)) == (255, 255, 255) and
                image.get_at((x, y + self.h)) == (255, 255, 255) and
                image.get_at((x + self.w, y + self.h)) == (255, 255, 255)
        ):
            self.x, self.y = x, y

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

player = Player(543, 80, 20, 20, "assets/player.png")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()



    window.blit(image, (0, 0))
    player.move()
    player.draw(window)
    pygame.display.update()
    clock.tick(FPS)