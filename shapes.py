from OpenGL.GL import *
from transformations import *
import math

def cylinder(radius, height, x, y, z, num_seg):
    translate(x,y,z)
    count = 0
    angle = 2 * math.pi / num_seg

    top_x = 0; top_y = height/2; top_z = 0
    bottom_x = 0; bottom_y = -height/2; bottom_z = 0

    glBegin(GL_TRIANGLES)
    while count < num_seg:
        p0_x = radius * math.cos(count * angle)
        p0_y = 0
        p0_z = radius * math.sin(count * angle)

        p1_x = radius * math.cos((count+1) * angle)
        p1_y = 0
        p1_z = radius * math.sin((count+1) * angle)

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
    

    