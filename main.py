from OpenGL.GL import *
from OpenGL.GLU import *

import pygame

from pygame.locals import * 
from MeshRenderer import MacaMesh, BananaMesh, MamaoMesh, MelanciaMesh, LaranjaMesh, MesaMesh

fruta = 0

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
    
    frutas = [MacaMesh(), BananaMesh(), MamaoMesh(), MelanciaMesh(), LaranjaMesh()]
            
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            glTranslatef(-1,0,0)
        if event.key == pygame.K_RIGHT:
            glTranslatef(1,0,0)
        if event.key == pygame.K_UP:
            fruta -= 1
        if event.key == pygame.K_DOWN:
            fruta += 1
        if event.key == pygame.K_f:
            fruta += 1
            
    if event.type == MOUSEWHEEL:
        if event.y > 0:
            glTranslatef(0,0,0.5)
        if event.y < 0:
            glTranslatef(0,0,-0.5)
            
    glRotatef(1, 3, -10, -45)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    if (fruta%len(frutas) == 0):
        MacaMesh()
    if (fruta%len(frutas) == 1):
        BananaMesh()
    if (fruta%len(frutas) == 2):
        MamaoMesh()
    if (fruta%len(frutas) == 3):
        MelanciaMesh()
    if (fruta%len(frutas) == 4):
        LaranjaMesh()
    glPopMatrix()
        
    
    pygame.display.flip()
    pygame.time.wait(10)

