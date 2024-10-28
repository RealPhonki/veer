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
import json

# third party
from pygame.key import key_code
import pygame as pg

# project
from input_manager import InputManager
from image_loader import ImageLoader

from physics.box_collider import BoxCollider
from scene.camera import Camera

class Player(BoxCollider):
    """ Represents a player

    Args:
        pg (_type_): _description_
    """
    def __init__(
        self,
        screen: pg.Surface,
        camera: Camera, 
        input_manager: InputManager,
        json_data: str,
        spawn_position: pg.Vector2
    ) -> None:
        # reference
        self.screen = screen
        self.camera = camera
        self.input_manager = input_manager
        
        # constants
        self.DATA = self.load_data(json_data)
        
        self.SPRITES = ImageLoader.load(self.DATA["image_path"])
        
        self.KEYBINDS = {action: key_code(key) for (action, key) in self.DATA["key_binds"].items()}
        
        self.MOVE_SPEED = self.DATA["move_speed"]
        self.JUMP_FORCE = self.DATA["jump_force"]
        
        # attributes
        self.current_sprite = self.SPRITES["idle"]
        
        # initalization
        BoxCollider.__init__(self, self.DATA["ignore_collision"], *spawn_position, *self.DATA["hitbox_size"])
        
    def load_data(self, data_path: str) -> None:
        """ Loads the player data from a json file

        Args:
            data_path (str): Represents the path to a json file
        """
        with open(data_path, encoding="utf-8") as f:
            return json.load(f)
    
    def _handle_inputs(self, delta_time: float) -> None:
        if self.input_manager[self.KEYBINDS["jump"]] and self.collisions.bottom:
            self._velocity.y = -self.JUMP_FORCE
            
        if self.input_manager[self.KEYBINDS["left"]]:
            self._velocity.x -= self.MOVE_SPEED * delta_time * self.friction
            
        if self.input_manager[self.KEYBINDS["right"]]:
            self._velocity.x += self.MOVE_SPEED * delta_time * self.friction
    
    def update(self, delta_time: float, others: list[BoxCollider]) -> None:
        self._handle_inputs(delta_time)
        BoxCollider.update(self, delta_time, others)
        
        if self.collisions.bottom:
            self.double_jump_ready = True
    
    def render(self) -> None:
        """ Renders the player to a surface

        Args:
            screen (pg.surface): The surface to render the player to
        """
        self.screen.blit(self.current_sprite, (self.x - self.camera.x, self.y - self.camera.y))