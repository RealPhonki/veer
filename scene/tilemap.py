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
# pylint: disable=no-name-in-module

# standard
from math import floor, ceil
import json

# third-party
import pygame as pg

# project
from image_loader import ImageLoader

from physics.box_collider import BoxCollider
from scene.camera import Camera

class TileMap:
    """ Represents the map
    """
    def __init__(self, screen: pg.Surface, camera: Camera, json_data: str) -> None:
        # reference
        self.screen = screen
        self.camera = camera
        
        # constants
        self.DATA = self.load_data(json_data)
        
        self.SPRITES = ImageLoader.load(self.DATA["image_path"])
        
        self.TILE_SIZE = self.DATA["tile_size"]
        self.SIZE = self.WIDTH, self.HEIGHT = self.DATA["map_size"]
        
        self.LEVELS = self.DATA["levels"]
        
        # attributes
        self.map = self.LEVELS["1"]
        
    def load_data(self, data_path: str) -> None:
        """ Loads the player data from a json file

        Args:
            data_path (str): Represents the path to a json file
        """
        with open(data_path, encoding="utf-8") as f:
            return json.load(f)
    
    def collides(self, other: BoxCollider, ignore: list) -> pg.Rect:
        """ Checks if a BoxCollider is colliding with a block

        Args:
            other (BoxCollider): The BoxCollider to check collision with

        Returns:
            bool: The collision result
        """
        # parse tile index of box collider
        tile_x = floor(other.x / self.TILE_SIZE)
        tile_y = floor(other.y / self.TILE_SIZE)
        tile_width = ceil((other.x + other.width) / self.TILE_SIZE) - tile_x
        tile_height = ceil((other.y + other.height) / self.TILE_SIZE) - tile_y
        
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
        
        # return collided tiles
        for y in range(tile_y, tile_y + tile_height):
            for x in range(tile_x, tile_x + tile_width):
                if self.map[y][x] != "0":
                    return pg.Rect(
                        x * self.TILE_SIZE,
                        y * self.TILE_SIZE,
                        self.TILE_SIZE,
                        self.TILE_SIZE
                    )
        return None
    
    def render(self) -> None:
        """ Renders the map to the screen
        """
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == "0":
                    continue
                elif tile == "b":
                    pg.draw.rect(self.screen, (0, 0, 255), [
                        x * self.TILE_SIZE - self.camera.x,
                        y * self.TILE_SIZE - self.camera.y,
                        self.TILE_SIZE,
                        self.TILE_SIZE
                    ])
                elif tile == "p":
                    pg.draw.rect(self.screen, (255, 0, 0), [
                        x * self.TILE_SIZE - self.camera.x,
                        y * self.TILE_SIZE - self.camera.y,
                        self.TILE_SIZE,
                        self.TILE_SIZE
                    ])
                else:
                    self.screen.blit(self.SPRITES[tile], [
                        x * self.TILE_SIZE - self.camera.x,
                        y * self.TILE_SIZE - self.camera.y
                    ])