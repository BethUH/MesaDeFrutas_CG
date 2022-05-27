from OpenGL.GL import *
from OpenGL.GLU import *

import pygame

from pygame.locals import * 
from MeshRenderer import MacaMesh, BananaMesh, MamaoMesh, MelanciaMesh, LaranjaMesh, MesaMesh

fruta = 0
rotation = 0

def main():
    pygame.init()
    display = (720, 720)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)
    glTranslatef(0.0, 0.0, -300)
    glRotatef(-90, 2, 0, 0)
    
    global frutas
    frutas = [MacaMesh(), BananaMesh(), MamaoMesh(), MelanciaMesh(), LaranjaMesh()]


main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_KP4:
            glTranslatef(-4,0,0)
        if event.key == pygame.K_KP6:
            glTranslatef(4,0,0)
        if event.key == pygame.K_UP:
            fruta -= 1
        if event.key == pygame.K_DOWN:
            fruta += 1
        if event.key == pygame.K_KP8:
            glTranslatef(0,0,-4)
        if event.key == pygame.K_KP2:
            glTranslatef(0,0,4)
        if event.key == pygame.K_KP1:
            glRotatef(10,0,0,-4)
        if event.key == pygame.K_KP3:
            glRotatef(10,0,0, 4)
        
            
    if event.type == MOUSEWHEEL:
        if event.y > 0:
            glTranslatef(0,0,0.5)
        if event.y < 0:
            glTranslatef(0,0,-0.5)
            
    
    #glRotatef(1, 3, -10, -45)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    glPushMatrix() #Inicializando a matriz das frutas
    glRotatef(rotation, 3, -10, -45)
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
    
    
    glRotatef(-90,1,0,0)
    glTranslatef(0,110,0)
    glScalef(2,2,2)
    MesaMesh()
    
    glPopMatrix()
    
    rotation += 1
        
    
    pygame.display.flip()
    pygame.time.wait(10)

