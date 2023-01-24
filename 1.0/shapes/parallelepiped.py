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
    def __init__(self, x:float = 0.0, y:float = 0.0, z:float = 0.0, width:float = 1.0, heigth:float = 1.0, length:float = 1.0, scale = 1.0, angle = 0, color = 'white', color_border='white') -> None:
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.heigth = heigth
        self.length = length
        self.objectScale = scale
        self.angle = math.radians(angle)
        self.color = color
        self.color_border = color_border
        self.colors = {
            'white': (1.0, 1.0, 1.0, 1.0),
            'red': (1.0, 0.0, 0.0, 1.0),
            'green': (0.0, 1.0, 0.0, 1.0),
            'brown': (78/255, 31/255, 8/255, 1),
            'green_transparent': (0.0, 1.0, 0.0, .5),
            'blue': (0.0, 0.0, 1.0, 1.0),
            'yellow': (1.0, 1.0, 0.0, 1.0)
            
        }
        
        self.colors_border = {
            'white': (1.0, 1.0, 1.0),
            'red': (1.0, 0.0, 0.0),
            'green': (0.0, 1.0, 0.0),
            'brown': (70/255, 35/255, 10/255),
            'green_transparent': (0.0, 1.0, 0.0),
            'blue': (0.0, 0.0, 1.0),
            'yellow': (1.0, 1.0, 0.0)
        }
        
        x_0 = ((self.x + (self.width * math.cos(self.angle))) * self.objectScale)
        y_0 = ((self.y + (self.width * math.sin(self.angle))) * self.objectScale)
        z_0 = ((self.z) * self.objectScale)
        
        x_1 = ((self.x + (self.width * math.cos(self.angle) - (self.heigth * math.sin(self.angle)))) * self.objectScale)
        y_1 = ((self.y + (self.heigth * math.cos(self.angle) + (self.width * math.sin(self.angle)))) * self.objectScale)
        z_1 = ((self.z) * self.objectScale)
        
        x_2 = ((self.x - (self.heigth * math.sin(self.angle))) * self.objectScale)
        y_2 = ((self.y + (self.heigth * math.cos(self.angle))) * self.objectScale)
        z_2 = ((self.z) * self.objectScale)
        
        x_3 = ((self.x) * self.objectScale)
        y_3 = ((self.y) * self.objectScale)
        z_3 = ((self.z) * self.objectScale)
        
        x_4 = ((self.x + (self.width * math.cos(self.angle))) * self.objectScale)
        y_4 = ((self.y + (self.width * math.sin(self.angle))) * self.objectScale)
        z_4 = ((self.z + self.length) * self.objectScale)
        
        x_5 = ((self.x + (self.width * math.cos(self.angle) - (self.heigth * math.sin(self.angle)))) * self.objectScale)
        y_5 = ((self.y + (self.heigth * math.cos(self.angle) + (self.width * math.sin(self.angle)))) * self.objectScale)
        z_5 = ((self.z + self.length) * self.objectScale)
        
        x_6 = ((self.x) * self.objectScale)
        y_6 = ((self.y) * self.objectScale)
        z_6 = ((self.z + self.length) * self.objectScale)
        
        x_7 = ((self.x - (self.heigth * math.sin(self.angle))) * self.objectScale)
        y_7 = ((self.y + (self.heigth * math.cos(self.angle))) * self.objectScale)
        z_7 = ((self.z + self.length) * self.objectScale)
        
        self.points = [
            [x_0, y_0, z_0], #Ponto 100
            [x_1, y_1, z_1], #Ponto 110
            [x_2, y_2, z_2], # Ponto 010
            [x_3, y_3, z_3], # Ponto 000
            [x_4, y_4, z_4], # Ponto 101
            [x_5, y_5, z_5], # Ponto 111
            [x_6, y_6, z_6], # Ponto 001 
            [x_7, y_7, z_7], # Ponto 011
        ]
        
        self.normals = [
            [self.width/2, self.heigth/2, 1],
            [- 1, self.heigth/2, self.length/2],
            [self.width/2, self.heigth/2, -1],
            [1, self.heigth/2, self.length/2],
            [self.width/2, 1, self.length/2],
            [self.width/2, - 1, self.length/2],
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
                    glColor3fv(self.colors_border[self.color_border])
                    glVertex3fv(points[point])
            glEnd()
            
        except Exception as exception:
            raise f'Cannot connect points! Exception -> {exception}'
    
    '''
    * Método para desenhar as superfícies;
    ** Lista de pontos que se conectam para formar uma superfície;
    '''  
    def create_surfaces(self, points, surfaces, normals) -> None:
        try:
            glBegin(GL_QUADS)
            
            glColor4fv(self.colors[self.color])
            
            for surface in surfaces:
                glNormal3fv(normals[surfaces.index(surface)])
                for point in surface:
                    # print(f'Point -> {point}. Surface -> {surface}.')
                    glVertex3fv(points[point])
            
            glEnd()
        except Exception as exception:
            raise f'Cannot create surfaces! Exception -> {exception}'
    
    '''
    * Método para desenhar o paralelepípedo;
    '''
    def draw(self) -> None:
        try:
            self.create_surfaces(self.points, self.surfaces, self.normals)
            
            self.connect_points(self.points, self.edges)
            
        except Exception as exception:
            raise f'Cannot draw Cube! Exception -> {exception}'