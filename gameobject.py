import pygame as pg

import gameobject


class GameObject:
    gameObjects: list[gameobject.GameObject] = []

    def __init__(self, rect: pg.Rect, color: pg.Color):
        self.__rect: pg.Rect = rect
        self.__color: pg.Color = color

        GameObject.gameObjects.append(self)

    def __del__(self):
        GameObject.gameObjects.remove(self)

    def draw(self, surface: pg.Surface):
        pg.draw.rect(surface, self.__color, self.__rect)

    def move_pos(self, x, y):
        self.__rect.move_ip(x, y)

    def set_pos(self, x, y):
        self.__rect.update(x, y, self.__rect.w, self.__rect.h)

    def collides_with(self, others: list[GameObject]) -> bool:
        return self.__rect.collidelist([other.__rect for other in others]) != 0


class Projectile(GameObject):
    size: int = 6
    speed: int = 2
    projectiles: list[gameobject.Projectile] = []

    def __init__(self, pos: (int, int), direction: pg.Vector2):
        super().__init__(pg.Rect(pos[0], pos[1], Projectile.size, Projectile.size))
        self.__dir: pg.Vector2 = direction
        Projectile.projectiles.append(self)

    def __del__(self):
        Projectile.projectiles.remove(self)

    def updatePos(self):
        moveBy = self.__dir * Projectile.speed
        self.move_pos(moveBy.x, moveBy.y)
