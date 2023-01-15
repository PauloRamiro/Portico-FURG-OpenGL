#coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transforms import *
from shapes.parallelepiped import *

'''
-> Classe para criar um arco
'''
class Arc(Transforms):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, initial_angle = 0, final_angle = 180,
            radius:float = 2.0, heigth:float = 1.0, length:float = 1.0, width:float = 1.0,
            segments:int = False, scale:float = 1.0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.heigth = heigth
        self.length = length
        self.width = width
        self.objectScale = scale
        self.segments = segments
        self.initial_angle =  math.radians(initial_angle)
        self.final_angle = math.radians(final_angle)
        
    '''
    -> Método para criar um cilindro de acordo com a quantidade de segmentos
    '''
    def create_arc(self) -> None:
        try:
            if not self.segments:
                angle = 2 * math.pi / (200/self.width)
            else:
                angle = 2 * math.pi / self.segments

            count= self.initial_angle/angle - angle

            while angle*count < self.final_angle:
                segment = Parallelepiped(   x=self.radius * math.cos(count * angle) + self.x,
                                            y=self.radius * math.sin(count * angle) - self.radius + self.y, 
                                            z=self.z, 
                                            width=self.width, 
                                            length=self.length, 
                                            heigth=self.heigth, 
                                            angle=-(90-math.degrees(angle*count)))
                segment.draw()

                count+=1
        
        except Exception as exception:
            raise Exception(f'Cannot create cylinder! Exception -> {exception}')
     
    '''
    -> Método para desenhar o arco
    '''   
    def draw(self) -> None:
        try:
            
            self.create_arc()
            
        except Exception as exception:
            raise Exception(f'Cannot draw arc! Exception -> {exception}')
    
    