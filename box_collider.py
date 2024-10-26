# pylint: disable=trailing-whitespace
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=no-member
# pylint: disable=missing-final-newline
# pylint: disable=attribute-defined-outside-init
# pylint: disable=consider-using-enumerate
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=import-error
# pylint: disable=missing-function-docstring

from typing import Self

import pygame as pg

class BoxCollider:
    """ Handles collision of a box-shaped entity
    """
    def __init__(self, x: float, y: float, width: int, height: int) -> None:
        self._hitbox = [x, y, width, height]
        self._velocity = pg.Vector2(0, 0)
        self._gravity = pg.Vector2(0, 0)
    
    @property
    def position(self) -> pg.Vector2:
        return pg.Vector2(self._hitbox[0], self._hitbox[1])
    
    @position.setter
    def position(self, value: pg.Vector2 | tuple) -> None:
        self.x, self.y = value
    
    @property
    def x(self) -> float:
        return self._hitbox[0]
    
    @x.setter
    def x(self, value: float) -> None:
        self._hitbox[0] = value
    
    @property
    def y(self) -> float:
        return self._hitbox[1]
    
    @y.setter
    def y(self, value: float) -> None:
        self._hitbox[1] = value
    
    @property
    def width(self) -> float:
        return self._hitbox[2]
    
    @width.setter
    def width(self, value: float) -> None:
        self._hitbox[2] = value
    
    @property
    def height(self) -> float:
        return self._hitbox[3]
    
    @height.setter
    def height(self, value: float) -> None:
        self._hitbox[3] = value
    
    @property
    def right(self) -> float:
        return self.x + self.width
    
    @right.setter
    def right(self, value: float) -> None:
        self._hitbox[0] = value - self.width
    
    @property
    def left(self) -> float:
        return self.x - self.width
    
    @left.setter
    def left(self, value: float) -> None:
        self._hitbox[0] = value
    
    @property
    def top(self) -> float:
        return self.y - self.height
    
    @top.setter
    def top(self, value: float) -> None:
        self._hitbox[1] = value
    
    @property
    def bottom(self) -> float:
        return self.y + self.height
    
    @bottom.setter
    def bottom(self, value: float) -> None:
        self._hitbox[1] = value - self.height
    
    def set_gravity(self, gravity: pg.Vector2) -> None:
        self._gravity = gravity
    
    def update(self, others: list[Self]) -> None:
        self._velocity += self._gravity
        
        self.x += self._velocity.x
        for other in others:
            collision = other.collides(self)
            if not collision:
                continue
            
            if self._velocity.x > 0:
                self.right = collision.left
            elif self._velocity.x < 0:
                self.left = collision.right
            
            self._velocity.x = 0
        
        self.y += self._velocity.y
        for other in others:
            collision = other.collides(self)
            if not collision:
                continue
            
            if self._velocity.y > 0:
                self.bottom = collision.top
            elif self._velocity.y < 0:
                self.top = collision.bottom
            
            self._velocity.y = 0