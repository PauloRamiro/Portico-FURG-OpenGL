#coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transforms import *

'''
-> Classe para criar um cilindro
'''
class Cylinder(Transforms):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, radius:float = 1.0, heigth:float = 1.0, segments:int = 20, scale:float = 1.0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.heigth = heigth
        self.objectScale = scale
        self.segments = segments
        
    '''
    -> Método para criar um cilindro de acordo com a quantidade de segmentos
    '''
    def create_cylinder(self) -> None:
        try:
            count = 0
            angle = 2 * math.pi / self.segments
            top_x = self.x
            top_y = self.y + self.heigth
            top_z = self.z
            bottom_x = self.x
            bottom_y = self.y
            bottom_z = self.z
            glBegin(GL_TRIANGLES)
            
            while count < self.segments:
                glColor3fv((1, 1, 1))
                
                p0_x = self.radius * math.cos(count * angle) + self.x
                p0_z = self.radius * math.sin(count * angle) + self.z
                p1_x = self.radius * math.cos((count + 1) * angle) + self.x
                p1_z = self.radius * math.sin((count + 1) * angle) + self.z

                glNormal3fv((0, 1, 0))
                glVertex3fv((top_x, top_y, top_z))
                glVertex3fv((p0_x, top_y, p0_z))
                glVertex3fv((p1_x, top_y, p1_z))

                glNormal3fv(((p0_x-self.x)/self.radius, 0, (p0_z-self.z)/self.radius))
                glVertex3fv((p0_x, top_y, p0_z))
                glNormal3fv(((p0_x-self.x)/self.radius, 0, (p0_z-self.z)/self.radius))
                glVertex3fv((p0_x, bottom_y, p0_z))
                glNormal3fv((p1_x/self.radius, 0, p1_z/self.radius))
                glVertex3fv((p1_x, top_y, p1_z))

                glNormal3fv(((p1_x-self.x)/self.radius, 0, (p1_z-self.z)/self.radius))
                glVertex3fv((p1_x, top_y, p1_z))
                glNormal3fv(((p0_x-self.x)/self.radius, 0, (p0_z-self.z)/self.radius))
                glVertex3fv((p0_x, bottom_y, p0_z))
                glNormal3fv(((p1_x-self.x)/self.radius, 0, (p1_z-self.z)/self.radius))
                glVertex3fv((p1_x, bottom_y, p1_z))

                glNormal3fv((0, -1, 0))
                glVertex3fv((bottom_x, bottom_y, bottom_z))
                glVertex3fv((p0_x, bottom_y, p0_z))
                glVertex3fv((p1_x, bottom_y, p1_z))

                count += 1
            
            glEnd()
        
        except Exception as exception:
            raise Exception(f'Cannot create cylinder! Exception -> {exception}')
     
    '''
    -> Método para desenhar o cilindro
    '''   
    def draw(self) -> None:
        try:
            
            self.create_cylinder()
            
        except Exception as exception:
            raise Exception(f'Cannot draw cylinder! Exception -> {exception}')
    
    