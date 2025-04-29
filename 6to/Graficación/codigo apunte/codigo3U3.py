import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math
import numpy as np

# dimensiones del cubo exterior
OUTER_CUBE_SIZE = 4.0

# dimensiones del cubo interior
INNER_CUBE_SIZE = 0.8

# Posición actual del cubo interior
inner_cube_pos = [0.0, 0.0, 0.0]

# Velocidad del cubo interior
velocity = [0.05, 0.03, 0.04]

# Variables para controlar la rotación de la cámara
angle_x = 0.0
angle_y = 0.0
distance = 12.0

# Colores del cubo interior y exterior
outer_cube_color = [0.2, 0.2, 0.8, 0.3]
inner_cube_color = [0.9, 0.2, 0.2, 1.0]

def draw_cube(size, color):
    vertices = (
        (-size, -size, -size),
        ( size, -size, -size),
        ( size,  size, -size),
        (-size,  size, -size),
        (-size, -size,  size),
        ( size, -size,  size),
        ( size,  size,  size),
        (-size,  size,  size),
    )

    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    )

    surfaces = (
        (0, 1, 2, 3), # Cara trasera
        (4, 5, 6, 7), # Cara frontal
        (0, 3, 7, 4), # Cara izquierda
        (1, 2, 6, 5), # Cara derecha
        (0, 1, 5, 4), # Cara inferior
        (3, 2, 6, 7)  # Cara superior
    )

    normals = (
        ( 0,  0, -1), # Cara trasera
        ( 0,  0,  1), # Cara frontal
        (-1,  0,  0), # Cara izquierda
        ( 1,  0,  0), # Cara derecha
        ( 0, -1,  0), # Cara inferior
        ( 0,  1,  0)  # Cara superior
    )

    # Establecer color
    glColor4fv(color)

    # Activar el modo de líneas para el cubo exterior
    if color == outer_cube_color:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # Dibujar cada superficie del cubo
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glNormal3fv(normals[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Restaurar el modo de polígono
    if color == outer_cube_color:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

def update_cube_position():
    global inner_cube_pos, velocity, inner_cube_color

    # Actualizar la posición del cubo interior
    inner_cube_pos[0] += velocity[0]
    inner_cube_pos[1] += velocity[1]
    inner_cube_pos[2] += velocity[2]

    # Calcular límites de colisión
    boundary_x = OUTER_CUBE_SIZE - INNER_CUBE_SIZE
    boundary_y = OUTER_CUBE_SIZE - INNER_CUBE_SIZE
    boundary_z = OUTER_CUBE_SIZE - INNER_CUBE_SIZE

    # Verificar colisión con los bordes del cubo exterior
    if inner_cube_pos[0] <= -boundary_x or inner_cube_pos[0] >= boundary_x:
        velocity[0] *= -1
        inner_cube_color = [random.random(), random.random(), random.random(), 1.0]
    if inner_cube_pos[1] <= -boundary_y or inner_cube_pos[1] >= boundary_y:
        velocity[1] *= -1
        inner_cube_color = [random.random(), random.random(), random.random(), 1.0]
    if inner_cube_pos[2] <= -boundary_z or inner_cube_pos[2] >= boundary_z:
        velocity[2] *= -1
        inner_cube_color = [random.random(), random.random(), random.random(), 1.0]

def main():
    global angle_x, angle_y, distance

    # Inicializar Pygame
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Cubo Rebotando en PyOpenGL")

    # Configurar perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Configurar iluminación
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Configurar luz
    ambient_light = [0.1, 0.1, 0.1, 1.0]
    diffuse_light = [0.7, 0.7, 0.7, 1.0]
    specular_light = [1.0, 1.0, 1.0, 1.0]
    position = [1.0, 1.0, 1.0, 0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)
    glLightfv(GL_LIGHT0, GL_POSITION, position)

    # Habilitar transparencia
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Variables para el control del mouse
    last_mouse_pos = None
    mouse_button_down = False

    # Bucle principal
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Control de teclado
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS or event.key == pygame.K_EQUALS:
                    distance -= 0.5
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    distance += 0.5

            # Control de mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo
                    mouse_button_down = True
                    last_mouse_pos = pygame.mouse.get_pos()
                elif event.button == 3:  # Botón derecho
                    mouse_button_down = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_button_down = False

            elif event.type == pygame.MOUSEMOTION and mouse_button_down:
                mouse_pos = pygame.mouse.get_pos()
                if last_mouse_pos is not None:
                    delta_x = mouse_pos[0] - last_mouse_pos[0]
                    delta_y = mouse_pos[1] - last_mouse_pos[1]
                    angle_y += delta_x * 0.01
                    angle_x += delta_y * 0.01

                    # Limitar el ángulo vertical
                    if angle_x > 1.5:
                        angle_x = 1.5
                    elif angle_x < -1.5:
                        angle_x = -1.5

                last_mouse_pos = mouse_pos

        # Actualizar la posición del cubo
        update_cube_position()

        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Resetear vista
        glLoadIdentity()

        # Posicionar la cámara
        camera_x = distance * math.sin(angle_y) * math.cos(angle_x)
        camera_y = distance * math.sin(angle_x)
        camera_z = distance * math.cos(angle_y) * math.cos(angle_x)
        gluLookAt(camera_x, camera_y, camera_z, 0, 0, 0, 0, 1, 0)

        # Dibujar el cubo exterior
        draw_cube(OUTER_CUBE_SIZE, outer_cube_color)

        # Dibujar el cubo interior (móvil)
        glPushMatrix()
        glTranslatef(inner_cube_pos[0], inner_cube_pos[1], inner_cube_pos[2])
        draw_cube(INNER_CUBE_SIZE, inner_cube_color)
        glPopMatrix()

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)  # Limitar a 60 FPS

    # Finalizar Pygame (moved outside the loop)
    pygame.quit()

if __name__ == "__main__":
    main()