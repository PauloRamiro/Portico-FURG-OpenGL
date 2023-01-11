import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from projections import *
from shapes import *

pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

#perspective(45, display[0]/display[1], 1, 10.0)
#ortho(-5.0, 5.0, -5.0, 5.0, 1.0, 50.0)
#frustum(-25.0, 25.0, -25.0, 25.0, 1.0, 10.0)
#gluLookAt(0,0,5,0,0,0,0,1,0)

glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
perspective(45, display[0]/display[1], 1, 10.0)
gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0) 

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
glLightfv(GL_LIGHT0, GL_POSITION,[2, 3, -1, 1])


cylinder(0.1, 1, 2, 1, 2, 20)
cylinder(0.1, 1, -1, 0, 0, 20)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    glRotatef(1, 3, 1, 1)

    pygame.display.flip()
    pygame.time.wait(10)