import pygame as pg


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
            elif event.type == pg.QUIT:
                return

        mainSurface.fill((255, 0, 0))
        move_pos()
        pg.display.flip()


def move_pos():
    keys = pg.key.get_pressed()
    direction: pg.Vector2 = pg.Vector2(-1 * int(keys[pg.K_a]) + int(keys[pg.K_d]),
                                       -1 * int(keys[pg.K_w]) + int(keys[pg.K_s]))
    print(direction)


if __name__ == '__main__':
    pg.init()
    # mainSurface: pg.surface = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    mainSurface: pg.surface = pg.display.set_mode((720, 480))

    main()
    pg.quit()
