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

class Camera(pg.Vector2):
    """ Represents the camera in the game with a point
    """
    def __init__(self, position: pg.Vector2, screen_size) -> None:
        self.offset_x = screen_size[0] // 2
        self.offset_y = screen_size[1] // 2
        super().__init__(*position)

    def track(self, target: pg.Vector2) -> None:
        """ Makes the camera move towards a point

        Args:
            target (pg.Vector2): The point to move the camera to
        """
        self.x += ((target.x - self.offset_x) - self.x) / 20
        self.y += ((target.y - self.offset_y) - self.y) / 20