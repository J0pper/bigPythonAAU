import pygame as pg

pg.init()
mainSurface: pg.surface = pg.display.set_mode((1920, 1080), pg.FULLSCREEN, vsync=1)


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
            elif event.type == pg.QUIT:
                return

        mainSurface.fill((255, 0, 0))
        pg.display.flip()



if __name__ == '__main__':
    main()
