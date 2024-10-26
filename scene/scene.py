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

import pygame as pg

from input_manager import InputManager
from scene.tilemap import TileMap
from scene.camera import Camera
from scene.entities.player import Player

class Scene:
    """ Handles all actors in the game
    """
    def __init__(self, screen: pg.Surface) -> None:
        # reference
        self.screen = screen
        
        # attributes
        self.camera = Camera((0, 0), self.screen.get_size())
        self.tile_map = TileMap(self.screen, self.camera)
        self.player = Player(self.screen, self.camera)
        self.player.set_gravity(pg.Vector2(0, 0))
    
    def update(self, input_manager: InputManager, delta_time: float) -> None:
        """ Updates all actors in the scene

        Args:
            input_manager (InputManager): The inputs
            delta_time (float): The delta time
        """
        self.camera.track(self.player)
        self.player.update(input_manager, delta_time, [self.tile_map])
    
    def render(self) -> None:
        """ Renders all actors in the scene to the screen
        """
        self.tile_map.render()
        self.player.render()