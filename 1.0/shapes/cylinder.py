#coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transforms import *

class Cylinder(Transforms):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, radius:float = 1.0, heigth:float = 1.0, scale:float = 1.0) -> None:
        super().__init__(x, y, z)
        
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.heigth = heigth
        self.objectScale = scale