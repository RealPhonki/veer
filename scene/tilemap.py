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

from math import floor, ceil

import pygame as pg

from physics.box_collider import BoxCollider
from scene.camera import Camera

class TileMap:
    """ Represents the map
    """
    def __init__(self, screen: pg.Surface, camera: Camera) -> None:
        # reference
        self.screen = screen
        self.camera = camera
        
        self.TILESIZE = 16
        self.SIZE = self.WIDTH, self.HEIGHT = [20, 10]
        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
    
    def collides(self, other: BoxCollider) -> pg.Rect:
        """ Checks if a BoxCollider is colliding with a block

        Args:
            other (BoxCollider): The BoxCollider to check collision with

        Returns:
            bool: The collision result
        """
        # parse tile index of box collider
        tile_x = floor(other.x / self.TILESIZE)
        tile_y = floor(other.y / self.TILESIZE)
        tile_width = ceil((other.x + other.width) / self.TILESIZE) - tile_x
        tile_height = ceil((other.y + other.height) / self.TILESIZE) - tile_y
        
        # if the collider is out of bounds then return nothing
        if tile_x + tile_width < 0 or tile_y + tile_height < 0:
            return None
        if tile_x > self.WIDTH or tile_y > self.HEIGHT:
            return None
        
        # clamp the tile index
        if tile_x < 0:
            tile_width += tile_x
            tile_x = 0
        if tile_y < 0:
            tile_height += tile_y
            tile_y = 0
        tile_width = min(tile_width, self.WIDTH - tile_x)
        tile_height = min(tile_height, self.HEIGHT - tile_y)
        
        # debug
        pg.draw.rect(self.screen, (255, 0, 0), [
            tile_x*self.TILESIZE - self.camera.x,
            tile_y*self.TILESIZE - self.camera.y,
            tile_width*self.TILESIZE,
            tile_height*self.TILESIZE
        ], 2)
        
        # return collided tiles
        for y in range(tile_y, tile_y + tile_height):
            for x in range(tile_x, tile_x + tile_width):
                if self.map[y][x] == 1:
                    return pg.Rect(x*self.TILESIZE, y*self.TILESIZE, self.TILESIZE, self.TILESIZE)
        return None
    
    def render(self) -> None:
        """ Renders the map to the screen
        """
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 0:
                    continue
                pg.draw.rect(self.screen, (155, 155, 155), [
                    x * self.TILESIZE - self.camera.x,
                    y * self.TILESIZE - self.camera.y,
                    self.TILESIZE,
                    self.TILESIZE,
                ])