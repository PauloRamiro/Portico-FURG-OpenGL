from OpenGL.GL import *
import math

def scale(x, y, z):
    """
    """
    m11 = x
    m22 = y
    m33 = z
    m44 = 1
    matrix = [
                m11, 0.0, 0.0, 0.0,
                0.0, m22, 0.0, 0.0,
                0.0, 0.0, m33, 0.0,
                0.0, 0.0, 0.0, m44
            ]


    glMultMatrixf(matrix)

def translate(x, y, z):
    """
    """
    m11 = 1.0
    m22 = 1.0
    m33 = 1.0
    m41 = x
    m42 = y
    m43 = z
    m44 = 1.0

    matrix = [
                m11, 0.0, 0.0, 0.0,
                0.0, m22, 0.0, 0.0,
                0.0, 0.0, m33, 0.0,
                m41, m42, m43, m44
                ]

    glMultMatrixf(matrix)  

def rotate(angle, x, y, z):
    """
    """
    c = math.cos(angle)
    s = math.sin(angle)

    m11 = x * x * (1 - c) + c
    m12 = x * y * (1 - c) - z * s
    m13 = x * z * (1 - c) + y * s
    m21 = y * x * (1 - c) + z * s
    m22 = y * y * (1 - c) + c
    m23 = y * z * (1 - c) - x * s
    m31 = x * z * (1 - c) - y * s
    m32 = y * z * (1 - c) + x * s
    m33 = z * z * (1 - c) + c
    m44 = 1.0

    matrix = [
                m11, m12, m13, 0.0,
                m21, m22, m23, 0.0,
                m31, m32, m33, 0.0,
                0.0, 0.0, 0.0, m44
                ]
    
    glMultMatrixf(matrix)