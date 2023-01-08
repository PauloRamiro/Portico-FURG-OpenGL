#coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transforms import *

'''
-> Classe para criar um cubo
* x -> coordenada em x do cubo;
* y -> coordenada em y do cubo;
* z -> coordenada em z do cubo;
* scale -> escala do objeto que será desenhado
'''
class Cube(Transforms):
    def __init__(self, x:float = 0.0, y:float = 0.0, z:float = 0.0, width:float = 1.0, heigth:float = 1.0, length:float = 1.0, scale = 1.0) -> None:
        super().__init__(x, y, z)
        
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.heigth = heigth
        self.length = length
        self.objectScale = scale
        
        self.points = [
            [((self.x + 1) * self.width * self.objectScale), ((self.y - 1) * self.heigth * self.objectScale), ((self.z - 1) * self.length * self.objectScale)],
            [((self.x + 1) * self.width * self.objectScale), ((self.y + 1) * self.heigth * self.objectScale), ((self.z - 1) * self.length * self.objectScale)],
            [((self.x - 1) * self.width * self.objectScale), ((self.y + 1) * self.heigth * self.objectScale), ((self.z - 1) * self.length * self.objectScale)],
            [((self.x - 1) * self.width * self.objectScale), ((self.y - 1) * self.heigth * self.objectScale), ((self.z - 1) * self.length * self.objectScale)],
            [((self.x + 1) * self.width * self.objectScale), ((self.y - 1) * self.heigth * self.objectScale), ((self.z + 1) * self.length * self.objectScale)],
            [((self.x + 1) * self.width * self.objectScale), ((self.y + 1) * self.heigth * self.objectScale), ((self.z + 1) * self.length * self.objectScale)],
            [((self.x - 1) * self.width * self.objectScale), ((self.y - 1) * self.heigth * self.objectScale), ((self.z + 1) * self.length * self.objectScale)],
            [((self.x - 1) * self.width * self.objectScale), ((self.y + 1) * self.heigth * self.objectScale), ((self.z + 1) * self.length * self.objectScale)],
        ]
        
        self.edges = [
            [0, 1],
            [0, 3],
            [0, 4],
            [2, 1],
            [2, 3],
            [2, 7],
            [6, 3],
            [6, 4],
            [6, 7],
            [5, 1],
            [5, 4],
            [5, 7]
        ]
        
        self.surfaces = [
            [0, 1, 2, 3],
            [3, 2, 7, 6],
            [6, 7, 5, 4],
            [4, 5, 1, 0],
            [1, 5, 7, 2],
            [4, 0, 3, 6]
        ]
        
    '''
    * Método para conectar cada ponto formando as arestas;
    ** points -> lista de pontos que serão conectados;
    ** edges -> lista que determina como cada ponto será conectado;
    '''
    def connect_points(self, points, edges) -> None:
        try:
            glBegin(GL_LINES)
            x = 0
            for edge in edges:
                for point in edge:
                    x += 1
                    glColor3fv((x, 1, 0))
                    glVertex3fv(points[point])
            glEnd()
            
        except Exception as exception:
            raise f'Cannot connect points! Exception -> {exception}'
    
    '''
    * Método para desenhar as superfícies;
    ** Lista de pontos que se conectam para formar uma superfície;
    '''  
    def create_surfaces(self, points, surfaces) -> None:
        try:
            glBegin(GL_QUADS)
            
            glColor3fv((0, 1, 0))
            
            for surface in surfaces:
                for point in surface:
                    glVertex3fv(points[point])
            
            glEnd()
        except Exception as exception:
            raise f'Cannot create surfaces! Exception -> {exception}'
    
    '''
    * Método para desenhar o cubo;
    '''
    def draw(self) -> None:
        try:
            self.create_surfaces(self.points, self.surfaces)
            
            self.connect_points(self.points, self.edges)
            
        except Exception as exception:
            raise f'Cannot draw Cube! Exception -> {exception}'