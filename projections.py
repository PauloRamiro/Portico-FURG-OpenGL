from OpenGL.GL import *
import math

def perspective(fovy, aspect, near, far):
    """
    """
    f = (1.0 / math.tan(fovy / 2.0))
    m11 = (f / aspect)
    m22 = f
    m33 = (far + near) / (near - far)
    m34 = (2.0 * far * near) / (near - far)
    m43 = -1.0

    matrix = [
                m11, 0.0, 0.0, 0.0,
                0.0, m22, 0.0, 0.0,
                0.0, 0.0, m33, m43,
                0.0, 0.0, m34, 0.0
                ]
    
    glMultMatrixf(matrix)

def ortho(left, right, bottom, top, near, far):
    """
    """
    m11 = 2.0 / (right - left)
    m22 = 2.0 / (top - bottom)
    m33 = -2.0 / (far - near)
    m41 = -(right + left) / (right - left)
    m42 = -(top + bottom) / (top - bottom)
    m43 = -(far + near) / (far - near)
    m44 = 1.0

    matrix = [
                m11, 0.0, 0.0, 0.0,
                0.0, m22, 0.0, 0.0,
                0.0, 0.0, m33, 0.0,
                m41, m42, m43, m44
                ]

    glMultMatrixf(matrix)


def frustum(left, right, bottom, top, near, far):
        """
        """
        m11 = (2.0 * near) / (right - left)
        m22 = (2.0 * near) / (top - bottom)
        m31 = (right + left) / (right - left)
        m32 = (top + bottom) / (top - bottom)
        m33 = -(far + near) / (far - near)
        m34 = -1.0
        m43 = -(2.0 * far * near) / (far - near)

        matrix = [
                    m11, 0.0, 0.0, 0.0,
                    0.0, m22, 0.0, 0.0,
                    m31, m32, m33, m34,
                    0.0, 0.0, m43, 0.0
                 ]

        glMultMatrixf(matrix)