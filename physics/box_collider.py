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

from typing import Self

import pygame as pg

from physics.colllision_manager import CollisionManager

class BoxCollider():
    """ Handles collision of a box-shaped entity
    """
    def __init__(self, ignore_collision: list[str], x: float, y: float, width: int, height: int) -> None:
        # settings
        self._IGNORE_COLLISION = ignore_collision
        self._gravity = pg.Vector2(0, 2)
        self._air_friction = 0.03
        self._ground_friction = 0.5
        
        # attributes
        self._hitbox = [x, y, width, height]
        self._velocity = pg.Vector2(0, 0)
        self.collisions = CollisionManager()
        self.friction = 0

    @property
    def position(self) -> pg.Vector2:
        """ The position of the collider """
        return pg.Vector2(self._hitbox[0], self._hitbox[1])
    
    @position.setter
    def position(self, value: pg.Vector2 | tuple) -> None:
        self.x, self.y = value
    
    @property
    def x(self) -> float:
        """ The x-component of the collider """
        return self._hitbox[0]
    
    @x.setter
    def x(self, value: float) -> None:
        self._hitbox[0] = value
    
    @property
    def y(self) -> float:
        """ The y-component of the collider """
        return self._hitbox[1]
    
    @y.setter
    def y(self, value: float) -> None:
        self._hitbox[1] = value
    
    @property
    def width(self) -> float:
        """ The width of the collider """
        return self._hitbox[2]
    
    @width.setter
    def width(self, value: float) -> None:
        self._hitbox[2] = value
    
    @property
    def height(self) -> float:
        """ The height of the collider """
        return self._hitbox[3]
    
    @height.setter
    def height(self, value: float) -> None:
        self._hitbox[3] = value
    
    @property
    def right(self) -> float:
        """ The x value representing the right of the collider """
        return self.x + self.width
    
    @right.setter
    def right(self, value: float) -> None:
        self._hitbox[0] = value - self.width
    
    @property
    def left(self) -> float:
        """ The x value representing the left of the collider """
        return self.x - self.width
    
    @left.setter
    def left(self, value: float) -> None:
        self._hitbox[0] = value
    
    @property
    def top(self) -> float:
        """ The y value representing the top of the collider """
        return self.y - self.height
    
    @top.setter
    def top(self, value: float) -> None:
        self._hitbox[1] = value
    
    @property
    def bottom(self) -> float:
        """ The y value representing the bottom of the collider """
        return self.y + self.height
    
    @bottom.setter
    def bottom(self, value: float) -> None:
        self._hitbox[1] = value - self.height
    
    def apply_velocity(self, others: list[Self]) -> None:
        """ Applies the velocity to the rigid body and gets collisions

        Args:
            others (list[Self]): The other objects to collide with
        """
        self.collisions.reset()
        
        self.x += self._velocity.x
        for other in others:
            collision = other.collides(self, self._IGNORE_COLLISION)
            if not collision:
                continue
            
            if self._velocity.x > 0:
                self.right = collision.left
                self.collisions.right = True
            elif self._velocity.x < 0:
                self.left = collision.right
                self.collisions.left = True
            
            self._velocity.x = 0
        
        self.y += self._velocity.y
        for other in others:
            collision = other.collides(self, self._IGNORE_COLLISION)
            if not collision:
                continue
            
            if self._velocity.y > 0:
                self.bottom = collision.top
                self.collisions.bottom = True
            elif self._velocity.y < 0:
                self.top = collision.bottom
                self.collisions.top = True
            
            self._velocity.y = 0
    
    def update(self, delta_time: float, others: list[Self]) -> None:
        """ Moves the collider based on its velocity

        Args:
            others (list[Self]): The other objects to collide with
        """
        self._velocity.x += self._gravity.x * delta_time
        self._velocity.y += self._gravity.y * delta_time
        
        self.apply_velocity(others)
            
        if self.collisions.bottom:
            self.friction = self._ground_friction
        else:
            self.friction *= self._air_friction
            
        self._velocity *= 1 - self.friction