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
# pylint: disable=arguments-differ

import pygame as pg

from input_manager import InputManager
from box_collider import BoxCollider
from scene.camera import Camera

class Player(BoxCollider):
    """ Represents a player

    Args:
        pg (_type_): _description_
    """
    def __init__(self, screen: pg.Surface, camera: Camera) -> None:
        # reference
        self.screen = screen
        self.camera = camera
        
        # constants
        self.MOVE_SPEED = 16 # pixels per second
        
        BoxCollider.__init__(self, 16, 16, 16, 16)
    
    def _handle_inputs(self, input_manager: InputManager, delta_time: float) -> None:
        if input_manager[pg.K_w]:
            self._velocity.y = -self.MOVE_SPEED * delta_time
        elif input_manager[pg.K_s]:
            self._velocity.y = self.MOVE_SPEED * delta_time
        else:
            self._velocity.y = 0
        if input_manager[pg.K_a]:
            self._velocity.x = -self.MOVE_SPEED * delta_time
        elif input_manager[pg.K_d]:
            self._velocity.x = self.MOVE_SPEED * delta_time
        else:
            self._velocity.x = 0
    
    def update(
        self,
        input_manager: InputManager,
        delta_time: float,
        others: list[BoxCollider]
    ) -> None:
        self._handle_inputs(input_manager, delta_time)
        BoxCollider.update(self, others)
    
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
