from OpenGL.GL import *
from transformations import *
import math

def cylinder(radius, height, x, y, z, num_seg):
    count = 0
    angle = 2 * math.pi / num_seg

    top_x = x; top_y = height/2; top_z = z
    bottom_x = x; bottom_y = -height/2; bottom_z = z

    glBegin(GL_TRIANGLES)
    while count < num_seg:
        p0_x = radius * math.cos(count * angle)+x
        p0_y = 0
        p0_z = radius * math.sin(count * angle)+z

        p1_x = radius * math.cos((count+1) * angle)+x
        p1_y = 0
        p1_z = radius * math.sin((count+1) * angle)+z

        glNormal3fv((0, 1, 0))
        glVertex3fv((top_x, top_y, top_z))
        glVertex3fv((p0_x, top_y, p0_z))
        glVertex3fv((p1_x, top_y, p1_z))

        glNormal3fv((p0_x/radius, 0, p0_z/radius))
        glVertex3fv((p0_x, top_y, p0_z))
        glNormal3fv((p0_x/radius, 0, p0_z/radius))
        glVertex3fv((p0_x, bottom_y, p0_z))
        glNormal3fv((p1_x/radius, 0, p1_z/radius))
        glVertex3fv((p1_x, top_y, p1_z))

        glNormal3fv((p1_x/radius, 0, p1_z/radius))
        glVertex3fv((p1_x, top_y, p1_z))
        glNormal3fv((p0_x/radius, 0, p0_z/radius))
        glVertex3fv((p0_x, bottom_y, p0_z))
        glNormal3fv((p1_x/radius, 0, p1_z/radius))
        glVertex3fv((p1_x, bottom_y, p1_z))

        glNormal3fv((0, -1, 0))
        glVertex3fv((bottom_x, bottom_y, bottom_z))
        glVertex3fv((p0_x, bottom_y, p0_z))
        glVertex3fv((p1_x, bottom_y, p1_z))

        count += 1
    glEnd()
    

    