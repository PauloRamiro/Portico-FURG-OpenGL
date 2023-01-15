#coding: utf-8

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes.parallelepiped import *
from shapes.cylinder import *
from shapes.arc import *
from transforms import Transforms as T

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
        
        self.guarita = Parallelepiped(x=-1.75, z=0, width=3.5,length= -6 , heigth=2.5, angle=0)
        self.guarita_p_e_f = Parallelepiped(x=-1.75, width=-.75,length= -0.3 , heigth=2.5, angle=0)
        self.guarita_p_d_f = Parallelepiped(x=1.75, width=.75,length= -0.3 , heigth=2.5, angle=0)
        self.guarita_p_e_t = Parallelepiped(x=-1.75, z=-6, width=-.75,length= 0.3 , heigth=2.5, angle=0)
        self.guarita_p_d_t = Parallelepiped(x=1.75, z=-6, width=.75,length= 0.3 , heigth=2.5, angle=0)
        self.teto_guarita = Parallelepiped(x=-2.5, y = 2.5, width=5,length=-6 , heigth=1, angle=0)
        
        self.pilar_esquerdo_frente = Cylinder(x=-10.5, radius=.1, heigth=5)
        self.pilar_direito_frente = Cylinder(x=10.5, radius=.1, heigth=5)
        self.pilar_esquerdo_meio = Cylinder(x=-10.5, z=-5, radius=.1, heigth=5)
        self.pilar_direito_meio = Cylinder(x=10.5, z=-5, radius=.1, heigth=5)
        self.pilar_esquerdo_tras = Cylinder(x=-10.5, z=-10, radius=.1, heigth=5)
        self.pilar_direito_tras = Cylinder(x=10.5, z=-10, radius=.1, heigth=5)
        
        self.viga_a_e_1 = Parallelepiped(x=-10.40, y = 5, z=-0.05, width = 2.95,length=0.08 , heigth=0.08, angle=115)
        self.viga_a_e_2 = Parallelepiped(x=-10.40, y = 5, z=-0.05, width = 3.05,length=0.08 , heigth=0.08, angle=97.5)
        self.viga_a_e_3 = Parallelepiped(x=-10.40, y = 5, z=-0.05, width = 3.85,length=0.08 , heigth=0.08, angle=70)
        self.viga_a_e_4 = Parallelepiped(x=-10.40, y = 5, z=-0.05, width = 3.55,length=0.08 , heigth=0.08, angle=45)
        
        self.viga_a_d_1 = Parallelepiped(x=10.60, y = 5, z=-0.05, width = 2.95,length=0.08 , heigth=0.08, angle=65)
        self.viga_a_d_2 = Parallelepiped(x=10.60, y = 5, z=-0.05, width = 3.05,length=0.08 , heigth=0.08, angle=82.5)
        self.viga_a_d_3 = Parallelepiped(x=10.60, y = 5, z=-0.05, width = 3.85,length=0.08 , heigth=0.08, angle=110)
        self.viga_a_d_4 = Parallelepiped(x=10.60, y = 5, z=-0.05, width = 3.55,length=0.08 , heigth=0.08, angle=135)
        
        self.viga_p_f = Parallelepiped(x= 0, y = 7.47, z=-0.05, width = 0.08 , length=0.08 , heigth=2.5)
        self.viga_p_e_f = Parallelepiped(x=-7.92, y = 7.47, z=-0.05, width = 7.92,length=0.08 , heigth=0.08)
        self.viga_p_d_f = Parallelepiped(x= 0, y = 7.47, z=-0.05, width = 8.08 , length=0.08 , heigth=0.08)
        
        self.coluna_s_e_f = Parallelepiped(x=-7.92, y = 7.47, z=-0.05, width = 0.08, length=0.08, heigth=1.5)
        self.coluna_s_d_f = Parallelepiped(x=7.92, y = 7.47, z=-0.05, width = 0.08, length=0.08, heigth=1.5)

        self.test = Arc(x=0, y=10, initial_angle=65, final_angle=115, radius = 30, width=.5, heigth=.08, length=.08)
        self.test1 = Arc(x=-2.08, y=7.7, initial_angle=47.5, final_angle=65.5, radius = 30, width=.4, heigth=.08, length=.08)
        self.test2 = Arc(x=-2.1, y=7.1, initial_angle=49, final_angle=65, radius = 30, width=.4, heigth=.08, length=.08)
        self.test3 = Arc(x=-2.1, y=7.1, initial_angle=49, final_angle=65, radius = 30, width=.08, heigth=.55, length=.08, segments = 360)
        
        
        gluPerspective(90, (display[0]/display[1]), 0.1, 100.0)
        
        self.main()
    
    '''
    Método para realizar o procedimento principal
    '''
    def main(self) -> None:
        try:
            # glLoadIdentity()
            # glTranslatef(0.0, 0.0, -15)
            gluLookAt(0, 0, 15, 0, 0, 0, 0, 1, 0)
            
            #self.Parallelepiped.scale(1)
            
            # self.cylender.scale(2)
            
            while True:
                self.handle_events()

                # self.Parallelepiped.rotate(1, 1, 1, 1)
                
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                glEnable(GL_LIGHT0)
                glEnable(GL_LIGHTING)

                glEnable(GL_DEPTH_TEST)
                glDepthFunc(GL_LEQUAL)
                glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

                glShadeModel(GL_SMOOTH)

                glEnable(GL_COLOR_MATERIAL)
                glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
                glEnable(GL_TEXTURE_2D)
                specReflection = [0.5, 0.5, 0.5, 0.5]
                glMaterialfv(GL_FRONT, GL_SPECULAR, specReflection)
                glMateriali(GL_FRONT, GL_SHININESS, 30)
                glLightfv(GL_LIGHT0, GL_POSITION,[8, 10, -5, 10])
                
                self.guarita.draw()
                self.guarita_p_e_f.draw()
                self.guarita_p_d_f.draw()
                self.guarita_p_e_t.draw()
                self.guarita_p_d_t.draw()
                self.teto_guarita.draw()
                
                self.pilar_esquerdo_frente.draw()
                self.pilar_direito_frente.draw()
                self.pilar_esquerdo_meio.draw()
                self.pilar_direito_meio.draw()
                self.pilar_esquerdo_tras.draw()
                self.pilar_direito_tras.draw()
                
                self.viga_a_e_1.draw()
                self.viga_a_e_2.draw()
                self.viga_a_e_3.draw()
                self.viga_a_e_4.draw()
                
                self.viga_a_d_1.draw()
                self.viga_a_d_2.draw()
                self.viga_a_d_3.draw()
                self.viga_a_d_4.draw()
                
                self.viga_p_f.draw()
                self.viga_p_e_f.draw()
                self.viga_p_d_f.draw()
                
                self.coluna_s_d_f.draw()
                self.coluna_s_e_f.draw()

                self.test.draw()
                self.test1.draw()
                self.test2.draw()
                self.test3.draw()
                
                
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
                        self.guarita.translate(x=-self.unit)
                    if event.key == pygame.K_RIGHT:
                        self.guarita.translate(x=self.unit)
                        
                    if event.key == pygame.K_DOWN:
                        self.guarita.translate(y=-self.unit)
                    if event.key == pygame.K_UP:
                        self.guarita.translate(y=self.unit)
                        
                if event.type == pygame.MOUSEBUTTONDOWN:                   
                    if event.button == 2:
                        if not(self.mouse_is_cliked):
                            self.mouse_click_x, self.mouse_click_y = event.pos
                            self.mouse_is_cliked = True
                                
                    if event.button == 4:
                        self.guarita.translate(z=self.unit)
                    if event.button == 5:
                        self.guarita.translate(z=-self.unit)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_is_cliked = False
                
            if(self.mouse_is_cliked):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if(mouse_x > self.mouse_click_x):
                    self.guarita.rotate(1, y=-1)
                elif(mouse_x < self.mouse_click_x):
                    self.guarita.rotate(1, y=1)
                    
                if(mouse_y > self.mouse_click_x):
                    self.guarita.rotate(1, x=-1)
                elif(mouse_x < self.mouse_click_x):
                    self.guarita.rotate(1, x=1)
        except Exception as exception:
            raise Exception(f'Cannot handle event! Exception {exception}')
                

Portico()