from OpenGL.GL import *
from OpenGL.GLU import *
import maca_constants
import banana_constants
import mamao_constants
import melancia_constants
import laranja_constants
import mesa_constants 
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
    
def BananaMesh():

    for face in banana_constants.faces:
        if(len(face) == 3):
            glBegin(GL_TRIANGLES)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[1])
                glVertex3fv(banana_constants.vertices[vertex])
            glEnd()
        if(len(face) == 4):
            glBegin(GL_QUADS)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[x])
                glVertex3fv(banana_constants.vertices[vertex])
            glEnd()

    glBegin(GL_LINES)
    for edge in banana_constants.edges:
        for vertex in edge:
            glVertex3fv(banana_constants.vertices[vertex])
    glEnd() 
    
def MamaoMesh():

    for face in mamao_constants.faces:
        if(len(face) == 3):
            glBegin(GL_TRIANGLES)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[1])
                glVertex3fv(mamao_constants.vertices[vertex])
            glEnd()
        if(len(face) == 4):
            glBegin(GL_QUADS)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[x])
                glVertex3fv(mamao_constants.vertices[vertex])
            glEnd()

    glBegin(GL_LINES)
    for edge in mamao_constants.edges:
        for vertex in edge:
            glVertex3fv(mamao_constants.vertices[vertex])
    glEnd()
    
def MelanciaMesh():

    for face in melancia_constants.faces:
        if(len(face) == 3):
            glBegin(GL_TRIANGLES)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[1])
                glVertex3fv(melancia_constants.vertices[vertex])
            glEnd()
        if(len(face) == 4):
            glBegin(GL_QUADS)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[x])
                glVertex3fv(melancia_constants.vertices[vertex])
            glEnd()

    glBegin(GL_LINES)
    for edge in melancia_constants.edges:
        for vertex in edge:
            glVertex3fv(melancia_constants.vertices[vertex])
    glEnd()
    
def LaranjaMesh():

    for face in laranja_constants.faces:
        if(len(face) == 3):
            glBegin(GL_TRIANGLES)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[1])
                glVertex3fv(laranja_constants.vertices[vertex])
            glEnd()
        if(len(face) == 4):
            glBegin(GL_QUADS)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[x])
                glVertex3fv(laranja_constants.vertices[vertex])
            glEnd()

    glBegin(GL_LINES)
    for edge in laranja_constants.edges:
        for vertex in edge:
            glVertex3fv(laranja_constants.vertices[vertex])
    glEnd()
    
def MesaMesh():

    for face in mesa_constants.faces:
        if(len(face) == 3):
            glBegin(GL_TRIANGLES)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[1])
                glVertex3fv(mesa_constants.vertices[vertex])
            glEnd()
        if(len(face) == 4):
            glBegin(GL_QUADS)
            x = 0
            for vertex in face:
                x += 1
                glColor3fv(color_constants.colors[x])
                glVertex3fv(mesa_constants.vertices[vertex])
            glEnd()

    glBegin(GL_LINES)
    for edge in mesa_constants.edges:
        for vertex in edge:
            glVertex3fv(mesa_constants.vertices[vertex])
    glEnd()