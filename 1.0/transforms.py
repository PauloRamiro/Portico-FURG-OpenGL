#coding: utf-8
from OpenGL.GL import *
import math

''' 
-> Classe para realizar as transformações em um objeto.
* x -> coordenada em x do objeto;
* y -> coordenada em y do objeto;
* z -> coordenada em z do objeto;
'''
class Transforms:
    def __init__(self, x:float = 0.0, y:float = 0.0, z:float = 0.0) -> None:
        self.transformX = x
        self.transformY = y
        self.transformZ = z
    
    '''
    -> Método para alterar a escala de um objeto.
    * scale -> nova escala do objeto;
    '''
    def scale(self, scale: float = 1.0) -> None:
        x = self.transformX if self.transformX > 0 else 1
        y = self.transformX if self.transformY > 0 else 1
        z = self.transformX if self.transformZ > 0 else 1
        try:
            matrix = [
                [x * scale, 0.0, 0.0, 0.0],
                [0.0, y * scale, 0.0, 0.0],
                [0.0, 0.0, z * scale, 0.0],
                [0.0, 0.0, 0.0,       1.0]
            ]
            
            glMultMatrixf(matrix)
        except Exception as exception:
            raise f'Cannot scale object! Exception -> {exception}'
    
    '''
    -> Método para transladar um objeto.
    * x -> valor que será transladado no eixo X;
    * y -> valor que será transladado no eixo Y;
    * z -> valor que será transladado no eixo Z;
    '''
    def translate(self, x:float = 0.0, y:float = 0.0, z:float = 0.0) -> None:
        try:
            matrix = [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [x, y, z, 1.0]
            ]
            
            glMultMatrixf(matrix)
        except Exception as exception:
            raise Exception(f'Cannot translate object! Exception -> {exception}')
        
    '''
    -> Método para rotacionar um objeto.
    * angle -> angulo que será rotacionado em graus;
    * x -> valor que será rotacionado no eixo x;
    * y -> valor que será rotacionado no eixo y;
    * z -> valor que será rotacionado no eixo z;
    '''
    def rotate(self, angle: float, x:float = 0.0, y:float = 0.0, z:float = 0.0) -> None:
        try:
            self.translate();
            
            radians = math.radians(angle)
            cosine = math.cos(radians)
            sine = math.sin(radians)
            
            m11 = x * x * (1 - cosine) + cosine
            m12 = x * y * (1 - cosine) - z * sine
            m13 = x * z * (1 - cosine) + y * sine
            m21 = y * x * (1 - cosine) + z * sine
            m22 = y * y * (1 - cosine) + cosine
            m23 = y * z * (1 - cosine) - x * sine
            m31 = x * z * (1 - cosine) - y * sine
            m32 = y * z * (1 - cosine) + x * sine
            m33 = z * z * (1 - cosine) + cosine

            matrix = [
                    m11, m12, m13, 0.0,
                    m21, m22, m23, 0.0,
                    m31, m32, m33, 0.0,
                    0.0, 0.0, 0.0, 1.0
                    ]
        
            glMultMatrixf(matrix)
        except Exception as exception:
            raise Exception(f'Cannot rotate object! Exeption -> {exception}')
        