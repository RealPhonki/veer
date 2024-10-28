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

# third-party
import pygame as pg

# project
from input_manager import InputManager
from scene.tilemap import TileMap
from scene.camera import Camera
from scene.entities.player import Player

class Scene:
    """ Handles all actors in the game
    """
    def __init__(self, screen: pg.Surface, input_manager: InputManager) -> None:
        # reference
        self.screen = screen
        
        # game
        self.camera = Camera((0, 0), self.screen.get_size(), track_speed=0.5)
        self.tile_map = TileMap(self.screen, self.camera, json_data="data/tilemap.json")
        
        # entities
        self.player1 = Player(
            screen = self.screen,
            camera = self.camera,
            input_manager = input_manager,
            json_data = "data/player1.json",
            spawn_position = (0, 0)
        )
        self.player2 = Player(
            screen = self.screen,
            camera = self.camera,
            input_manager = input_manager,
            json_data = "data/player2.json",
            spawn_position = (16, 0)
        )
    
    def update(self, delta_time: float) -> None:
        """ Updates all actors in the scene

        Args:
            input_manager (InputManager): The inputs
            delta_time (float): The delta time
        """
        # follow player with camera
        if self.player1.x > self.player2.x:
            tracked_player = self.player1
        else:
            tracked_player = self.player2
            
        self.camera.track(delta_time, tracked_player)
        
        # update players
        self.player1.update(delta_time, [self.tile_map])
        self.player2.update(delta_time, [self.tile_map])
    
    def render(self) -> None:
        """ Renders all actors in the scene to the screen
        """
        self.tile_map.render()
        self.player1.render()
        self.player2.render()