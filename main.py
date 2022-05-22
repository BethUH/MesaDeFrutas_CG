from OpenGL.GL import *
from OpenGL.GLU import *

import pygame

from pygame.locals import *
from MeshRenderer import MacaMesh, BananaMesh, MamaoMesh, MelanciaMesh, LaranjaMesh

def main():
    pygame.init()
    display = (720, 720)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)
    glTranslatef(0.0, 0.0, -160)
    glRotatef(-90, 2, 0, 0)

main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            glTranslatef(-1,0,0)
        if event.key == pygame.K_RIGHT:
            glTranslatef(1,0,0)
        if event.key == pygame.K_UP:
            glTranslatef(0,1,0)
        if event.key == pygame.K_DOWN:
            glTranslatef(0,-1,0)
    if event.type == MOUSEWHEEL:
        if event.y > 0:
            glTranslatef(0,0,0.5)
        if event.y < 0:
            glTranslatef(0,0,-0.5)
            
    glRotatef(1, 3, -10, -45)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    #MacaMesh()
    #BananaMesh()
    #MamaoMesh()
    #MelanciaMesh()
    LaranjaMesh()
    
    pygame.display.flip()
    pygame.time.wait(10)

