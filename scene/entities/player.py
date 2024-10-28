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
from physics.box_collider import BoxCollider
from scene.camera import Camera

class Player(BoxCollider):
    """ Represents a player

    Args:
        pg (_type_): _description_
    """
    def __init__(self, screen: pg.Surface, camera: Camera, input_manager: InputManager) -> None:
        # reference
        self.screen = screen
        self.camera = camera
        self.input_manager = input_manager
        
        # constants
        self.MOVE_SPEED = 32
        self.JUMP_FORCE = 3
        
        # attributes
        self.double_jump_ready = False
        
        # initalization
        BoxCollider.__init__(self, 16, 16, 16, 16)
        
        self.input_manager.bind(self.jump, pg.K_w)
    
    def jump(self, _: pg.key, key_state: bool) -> None:
        """ Makes the player jump """
        if not key_state:
            return
        if self.collisions.bottom:
            self._velocity.y = -self.JUMP_FORCE
        elif self.double_jump_ready:
            self._velocity.y = -self.JUMP_FORCE
            self.double_jump_ready = False
            self.friction = 0.7
    
    def _handle_inputs(self, delta_time: float) -> None:
        if self.input_manager[pg.K_a]:
            self._velocity.x -= self.MOVE_SPEED * delta_time * self.friction
        if self.input_manager[pg.K_d]:
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
        pg.draw.rect(self.screen, (255, 255, 255), [
            self.x - self.camera.x,
            self.y - self.camera.y,
            16,
            16,
        ])
