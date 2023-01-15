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
    

def create_arc(self) -> None:
        try:
            count = 0
            angle = 2 * math.pi / self.segments
            top_x = self.x
            top_z = self.z + self.heigth
            top_y = self.y
            bottom_x = self.x
            bottom_y = self.y
            bottom_z = self.z
            glBegin(GL_TRIANGLES)
            
            while count < self.segments:
                glColor3fv((0, 1, 1))
                
                p0_x = self.radius * math.cos(count * angle) + self.x
                p0_y = self.radius * math.sin(count * angle) + self.y
                p1_x = self.radius * math.cos((count + 1) * angle) + self.x
                p1_y = self.radius * math.sin((count + 1) * angle) + self.y

                glNormal3fv((0, 1, 0))
                glVertex3fv((top_x, top_y, top_z))
                glVertex3fv((p0_x, p0_y, top_z))
                glVertex3fv((p1_x,  p1_y, top_z))

                glNormal3fv((p0_x/self.radius, p0_y/self.radius, 0))
                glVertex3fv((p0_x, p0_y, top_z))
                glNormal3fv((p0_x/self.radius, p0_y/self.radius, 0))
                glVertex3fv((p0_x,p0_y,  bottom_z))
                glNormal3fv((p1_x/self.radius, p1_y/self.radius, 0))
                glVertex3fv((p1_x, p1_y, top_z))

                glNormal3fv((p1_x/self.radius, 0, p1_y/self.radius))
                glVertex3fv((p1_x, p1_y, top_z))
                glNormal3fv((p0_x/self.radius, p0_y/self.radius, 0))
                glVertex3fv((p0_x, p0_y, bottom_z))
                glNormal3fv((p1_x/self.radius, 0, p1_y/self.radius))
                glVertex3fv((p1_x, p1_y,  bottom_z))

                glNormal3fv((0, -1, 0))
                glVertex3fv((bottom_x, bottom_y, bottom_z))
                glVertex3fv((p0_x, p0_y, bottom_z))
                glVertex3fv((p1_x, p1_y, bottom_z))

                count += 1
            
            glEnd()