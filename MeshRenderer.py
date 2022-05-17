from OpenGL.GL import *
from OpenGL.GLU import *
import maca_constants
import color_constants

def MacaMesh():

    for face in maca_constants.faces:
        if(len(face) == 3):
            glBegin(GL_TRIANGLES)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[1])
                glVertex3fv(maca_constants.vertices[vertex])
            glEnd()
        if(len(face) == 4):
            glBegin(GL_QUADS)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[x])
                glVertex3fv(maca_constants.vertices[vertex])
            glEnd()

    glBegin(GL_LINES)
    for edge in maca_constants.edges:
        for vertex in edge:
            glVertex3fv(maca_constants.vertices[vertex])
    glEnd() 