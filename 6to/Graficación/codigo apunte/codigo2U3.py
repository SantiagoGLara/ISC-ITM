import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def init_pygame():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Cubo 3D")

def init_openGL():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Alfa en 1.0 en lugar de 0.1
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
def draw_cube():
    vertices = [
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1)
    ]

    caras = [
        (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 7, 3),
        (1, 5, 6, 2), (3, 2, 6, 7), (0, 1, 5, 4)
    ]

    colores = [
        (1.0, 0.0, 0.0, 1.0),  # Rojo
        (0.0, 1.0, 0.0, 1.0),  # Verde
        (0.0, 0.0, 1.0, 1.0),  # Azul
        (1.0, 1.0, 0.0, 1.0),  # Amarillo
        (1.0, 0.0, 1.0, 1.0),  # Magenta
        (0.0, 1.0, 1.0, 1.0)   # Cian
    ]

    glBegin(GL_QUADS)
    for i, cara in enumerate(caras):
        glColor4fv(colores[i])
        for vertice_idx in cara:
            glVertex3fv(vertices[vertice_idx])
    glEnd()

    glColor4f(1.0, 1.0, 1.0, 1.0)

    aristas = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    glBegin(GL_LINES)
    for arista in aristas:  #
        for vertice_idx in arista:
            glVertex3fv(vertices[vertice_idx])
    glEnd()

def main():
    init_pygame()
    init_openGL()

    rotacion_x = 0
    rotacion_y = 0
    rotacion_speed = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    rotacion_speed += 0.2
                elif event.key == pygame.K_DOWN:
                    rotacion_speed = max(0.2, rotacion_speed - 0.2)
                elif event.key == pygame.K_SPACE:
                    rotacion_speed = 0 if rotacion_speed > 0 else 1

        rotacion_x += 0.5 * rotacion_speed
        rotacion_y += 0.5 * rotacion_speed

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

        glRotatef(rotacion_x, 1, 0, 0)
        glRotatef(rotacion_y, 0, 1, 0)

        draw_cube()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()