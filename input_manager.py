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
from typing import Callable

key_code = int
key_state = bool

class InputManager(dict):
    """ This class manages pygame inputs
    - Index this class like a dictionary to get or set a key's value
    - Bind functions to this class to call them once; on the frame that the key is pressed

    Args:
        dict: Inherits from python dictionary
    """
    def __init__(self) -> None:
        self.pressed = {}
        self.__listeners = {}
    
    def bind(self, listener: Callable[[key_code, key_state], any], key: key_code) -> None:
        """ Binds a function to a keydown event

        Args:
            listener (Callable): The function to be called,
            must take the key and the key state as parameters
            key (key_code): The key to bind the function to
            - reference: www.pygame.org/docs/ref/key.html
        """
        if listener not in self.__listeners:
            if key in self.__listeners:
                self.__listeners[key].append(listener)
            else:
                self.__listeners[key] = [listener]
    
    def _call(self, key: key_code, value: key_state) -> None:
        for listener in self.__listeners.get(key, []):
            listener(key, value)
    
    def __setitem__(self, key: key_code, value: key_state) -> None:
        if key in self:
            self._call(key, value)
            super().__setitem__(key, value)
        
    def __getitem__(self, key: key_code) -> key_state:
        if key not in self:
            super().__setitem__(key, False)
        return super().__getitem__(key)