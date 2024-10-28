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

# third-party
import pygame as pg

class Camera(pg.Vector2):
    """ Represents the camera in the game with a point
    """
    def __init__(self, position: pg.Vector2, screen_size: list, track_speed: float) -> None:
        """
        Args:
            position (pg.Vector2): The initial position of the camera
            screen_size (list): The size of the screen, this is used to center the camera
            track_speed (float): The camera travels track_speed percent of distance each frame
        """
        # constants
        self.OFFSET_X = screen_size[0] // 2
        self.OFFSET_Y = screen_size[1] // 2
        self.TRACK_SPEED = track_speed
        
        # initialization
        super().__init__(*position)

    def track(self, delta_time: float, target: pg.Vector2) -> None:
        """ Makes the camera move towards a point

        Args:
            target (pg.Vector2): The point to move the camera to
        """
        self.x += ((target.x - self.OFFSET_X) - self.x) * self.TRACK_SPEED * delta_time
        self.y += ((target.y - self.OFFSET_Y) - self.y) * self.TRACK_SPEED * delta_time