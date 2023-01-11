#coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transforms import *

'''
-> Classe para criar um paralelepípedo
* x -> coordenada em x do paralelepípedo;
* y -> coordenada em y do paralelepípedo;
* z -> coordenada em z do paralelepípedo;
* width -> tamanho da aresta em x;
* height -> tamanho da aresta em y;
* lenght -> tamanho da aresta em z;
* scale -> escala do objeto que será desenhado
'''
class Parallelepiped(Transforms):
    def __init__(self, x:float = 0.0, y:float = 0.0, z:float = 0.0, width:float = 1.0, heigth:float = 1.0, length:float = 1.0, scale = 1.0, angle = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.heigth = heigth
        self.length = length
        self.objectScale = scale
        self.angle = math.radians(angle)
        
        self.points = [
            [((self.x + (self.width * math.cos(self.angle))) * self.objectScale), ((self.y + (self.width * math.sin(self.angle))) * self.objectScale),((self.z) * self.objectScale)], #Ponto 100
            [((self.x + (self.width * math.cos(self.angle) - (self.heigth * math.sin(self.angle)))) * self.objectScale), ((self.y + (self.heigth * math.cos(self.angle) + (self.width * math.sin(self.angle)))) * self.objectScale), ((self.z) * self.objectScale)], #Ponto 110
            [((self.x - (self.heigth * math.sin(self.angle))) * self.objectScale), ((self.y + (self.heigth * math.cos(self.angle))) * self.objectScale), ((self.z) * self.objectScale)], # Ponto 010
            [((self.x) * self.objectScale), ((self.y) * self.objectScale), ((self.z) * self.objectScale)], # Ponto 000
            [((self.x + (self.width * math.cos(self.angle))) * self.objectScale), ((self.y + (self.width * math.sin(self.angle))) * self.objectScale), ((self.z + self.length) * self.objectScale)], # Ponto 101
            [((self.x + (self.width * math.cos(self.angle) - (self.heigth * math.sin(self.angle)))) * self.objectScale), ((self.y + (self.heigth * math.cos(self.angle) + (self.width * math.sin(self.angle)))) * self.objectScale), ((self.z + self.length) * self.objectScale)], # Ponto 111
            [((self.x) * self.objectScale), ((self.y) * self.objectScale), ((self.z + self.length) * self.objectScale)], # Ponto 001 
            [((self.x - (self.heigth * math.sin(self.angle))) * self.objectScale), ((self.y + (self.heigth * math.cos(self.angle))) * self.objectScale), ((self.z + self.length) * self.objectScale)], # Ponto 011
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
            
            for edge in edges:
                for point in edge:
                    glColor3fv((1, 1, 0))
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
    * Método para desenhar o paralelepípedo;
    '''
    def draw(self) -> None:
        try:
            self.create_surfaces(self.points, self.surfaces)
            
            self.connect_points(self.points, self.edges)
            
        except Exception as exception:
            raise f'Cannot draw Cube! Exception -> {exception}'