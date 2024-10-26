# pylint: disable=trailing-whitespace
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=no-member
# sylint: disable=missing-final-newline
# pylint: disable=attribute-defined-outside-init
# pylint: disable=consider-using-enumerate
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=import-error

import pygame as pg

from input_manager import InputManager
from scene.scene import Scene

class App:
    """ Is the highest level of abstraction for the program"""
    def __init__(self) -> None:
        # constants
        self.FPS = 80
        self.B_RES = self.B_WIDTH, self.B_HEIGHT = (300, 240)
        self.RES = self.WIDTH, self.HEIGHT = (1000, 800)
        
        # attributes
        self.buffer = pg.Surface(self.B_RES)
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        
        self.input_manager = InputManager()
        self.scene = Scene(self.buffer)
        
        self.delta_time = 0
    
    def handle_events(self) -> None:
        """ Loops through all pygame events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                self.input_manager[event.key] = True
            if event.type == pg.KEYUP:
                self.input_manager[event.key] = False
    
    def update(self) -> None:
        """ Updates the program """    
        # clear the screen
        self.buffer.fill((0, 0, 0))
        
        self.delta_time = self.clock.get_fps() / 1000
        
        self.scene.update(self.input_manager, self.delta_time)
    
    def render(self) -> None:
        """ Renders the program """
        
        # render the scene to the buffer
        self.scene.render()
        
        # scale the buffer to the screen and draw it to the screen
        self.screen.blit(pg.transform.scale(self.buffer, self.RES))
        
        self.clock.tick(self.FPS)
        pg.display.set_caption(str(self.clock.get_fps()))
        pg.display.update()
    
    def run(self) -> None:
        """ Is the main loop for the program """
        while True:
            self.handle_events()
            self.update()
            self.render()

if __name__ == '__main__':
    app = App()
    app.run()
