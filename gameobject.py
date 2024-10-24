import pygame as pg


class GameObject:
    gameObjects: list['GameObject'] = []

    def __init__(self, pos: (float, float), size: (float, float), color: pg.Color):
        self.__pos: tuple[float, float] = pos
        self.__size: tuple[float, float] = size
        self.__color: pg.Color = color

        GameObject.gameObjects.append(self)

    def __del__(self):
        GameObject.gameObjects.remove(self)

    def _get_rect(self) -> pg.Rect:
        return pg.Rect(*self.__pos, *self.__size)

    def draw(self, surface: pg.Surface):
        pg.draw.rect(surface, self.__color, self._get_rect())
        # print(self.__rect)

    def move_pos(self, x, y):
        self.__pos = self.__pos[0] + x, self.__pos[1] + y

    def set_pos(self, x, y):
        self.__pos = (x, y)

    def collides_with(self, others: list['GameObject']) -> bool:
        return pg.Rect.collidelist(self._get_rect(), [other._get_rect() for other in others]) != 0


class Projectile(GameObject):
    size: float = 6
    speed: float = 2
    projectiles: list['Projectile'] = []

    def __init__(self, pos: (int, int), direction: pg.Vector2):
        super().__init__(pos, (Projectile.size, Projectile.size), pg.Color(255, 0, 0))
        self.__dir: pg.Vector2 = direction
        Projectile.projectiles.append(self)

    def __del__(self):
        Projectile.projectiles.remove(self)

    def update_pos(self):
        moveBy = self.__dir * Projectile.speed
        self.move_pos(moveBy.x, moveBy.y)


class Player(GameObject):
    size: float = 10
    speed: float = 0.5

    def __init__(self, pos: (int, int)):
        super().__init__(pos, (Player.size, Player.size), pg.Color(0, 0, 255))
        self.__dir: pg.Vector2 = pg.Vector2(0, 0)
        self.update_dir()


    def update_dir(self):
        keys = pg.key.get_pressed()
        self.__dir: pg.Vector2 = pg.Vector2(-1 * int(keys[pg.K_a]) + int(keys[pg.K_d]),
                                            -1 * int(keys[pg.K_w]) + int(keys[pg.K_s]))

    def update_pos(self):
        self.update_dir()
        moveBy = self.__dir * Player.speed
        self.move_pos(moveBy.x, moveBy.y)
