import pygame as pg
import time
from gameobject import Projectile, Player
import random
from gameobject import Projectile, GameObject


def get_projectile_params() -> ((float, float), pg.Vector2):
    direction = random.randint(1, 4)

    match direction:
        case 1:
            direction = pg.Vector2(1, 0)

        case 2:
            direction = pg.Vector2(0, 1)

        case 3:
            direction = pg.Vector2(-1, 0)

        case 4:
            direction = pg.Vector2(0, -1)

    xPos = 0
    yPos = 0

    if direction.x == 1:
        xPos = -20

    elif direction.x == -1:
        xPos = mainSurface.get_size()[0] + 20

    else:
        xPos = random.randrange(10, mainSurface.get_size()[0] - 10)

    if direction.y == 1:
        yPos = -20

    elif direction.y == -1:
        yPos = mainSurface.get_size()[1] + 20

    else:
        yPos = random.randrange(10, mainSurface.get_size()[1] - 10)

    return (xPos, yPos), direction


def main():
    Projectile(*get_projectile_params())
    player = Player(pg.Vector2(*mainSurface.get_size()) / 2)
    startTime = time.time()
    prevTime = startTime
    spawnerTimer = 0

    while True:
        deltaTime = time.time() - prevTime
        prevTime = time.time()
        spawnerTimer += deltaTime
        time.sleep(0.01)

        if spawnerTimer > 5 / ((time.time() - startTime) / 4):
            spawnerTimer = 0
            Projectile(*get_projectile_params())

        Projectile.speed = (25 + 2 * (time.time() - startTime)) * deltaTime

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
            elif event.type == pg.QUIT:
                return

        player.update_pos()
        for proj in Projectile.projectiles:
            proj.update_pos()

        # Rendering step
        mainSurface.fill((0, 255, 0))
        player.draw(mainSurface)
        for obj in GameObject.gameObjects:
            obj.draw(mainSurface)

        pg.display.flip()


if __name__ == '__main__':
    pg.init()
    # mainSurface: pg.surface = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    mainSurface: pg.surface = pg.display.set_mode((720, 480))

    main()
    pg.quit()
