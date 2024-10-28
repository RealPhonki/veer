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

class CollisionManager:
    """ Stores collision information """
    top = False
    right = False
    bottom = False
    left = False
    
    def reset(self) -> None:
        """ Resets the collision information """
        self.top = False
        self.right = False
        self.bottom = False
        self.left = False
    