#coding: utf-8

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes.cube import *

'''
* Classe principal
'''
class Portico:
    def __init__(self) -> None:
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        self.mouse_click_x = None
        self.mouse_click_y = None
        self.mouse_is_cliked = False
        self.unit = 1
        self.cube = Cube(heigth=2)
        
        gluPerspective(45, (display[0]/display[1]), 0.1, 20.0)
        
        self.main()
    
    '''
    Método para realizar o procedimento principal
    '''
    def main(self) -> None:
        try:
            glTranslatef(0.0, 0.0, -10)
            
            self.cube.scale(1)
            
            while True:
                self.handle_events()

                # self.cube.rotate(1, 1, 1, 1)
                
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                
                self.cube.draw()
                
                pygame.display.flip()
                pygame.time.wait(10)
        except Exception as exception:
            raise Exception(f'Cannot start main! Exception -> {exception}')
            
            
    '''
    * Método para lidar com os eventos do pygame
    '''       
    def handle_events(self) -> None:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.cube.translate(x=-self.unit)
                    if event.key == pygame.K_RIGHT:
                        self.cube.translate(x=self.unit)
                        
                    if event.key == pygame.K_DOWN:
                        self.cube.translate(y=-self.unit)
                    if event.key == pygame.K_UP:
                        self.cube.translate(y=self.unit)
                        
                if event.type == pygame.MOUSEBUTTONDOWN:                   
                    if event.button == 2:
                        if not(self.mouse_is_cliked):
                            self.mouse_click_x, self.mouse_click_y = event.pos
                            self.mouse_is_cliked = True
                                
                    if event.button == 4:
                        self.cube.translate(z=self.unit)
                    if event.button == 5:
                        self.cube.translate(z=-self.unit)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_is_cliked = False
                
            if(self.mouse_is_cliked):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if(mouse_x > self.mouse_click_x):
                    self.cube.rotate(1, y=-1)
                elif(mouse_x < self.mouse_click_x):
                    self.cube.rotate(1, y=1)
                    
                if(mouse_y > self.mouse_click_x):
                    self.cube.rotate(1, x=-1)
                elif(mouse_x < self.mouse_click_x):
                    self.cube.rotate(1, x=1)
        except Exception as exception:
            raise Exception(f'Cannot handle event! Exception {exception}')
                

Portico()