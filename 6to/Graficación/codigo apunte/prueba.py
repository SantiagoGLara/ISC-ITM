
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math
import numpy as np

# Dimensiones del cubo exterior
OUTER_CUBE_SIZE = 4.0

# Dimensiones del cubo interior (móvil)
INNER_CUBE_SIZE = 0.8

# Posiciones de los cubos interiores
inner_cubes = [[0.0, 0.0, 0.0]]

# Velocidades individuales de cada cubo
velocities = [[0.05, 0.03, 0.04]]

# Colores individuales de cada cubo
inner_colors = [[0.9, 0.2, 0.2, 1.0]]

# Variables para controlar la rotación de la cámara
angle_x = 0.0
angle_y = 0.0
distance = 12.0

# Rotación automática (izquierda/derecha)
rotation_speed = 0.0
ROTATION_MIN = -0.03
ROTATION_MAX = 0.03
ROTATION_STEP = 0.005

# Colores del cubo exterior
outer_cube_color = [0.2, 0.2, 0.8, 0.3]

# Función para dibujar un cubo con el color especificado
def draw_cube(size, color):
    vertices = (
        (-size, -size, -size),
        (size, -size, -size),
        (size, size, -size),
        (-size, size, -size),
        (-size, -size, size),
        (size, -size, size),
        (size, size, size),
        (-size, size, size)
    )

    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )

    surfaces = (
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (0, 3, 7, 4),
        (1, 2, 6, 5),
        (0, 1, 5, 4),
        (3, 2, 6, 7)
    )

    normals = (
        (0, 0, -1),
        (0, 0, 1),
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0)
    )

    glColor4fv(color)

    if color == outer_cube_color:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glNormal3fv(normals[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    if color == outer_cube_color:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

def update_cube_positions():
    boundary = OUTER_CUBE_SIZE - INNER_CUBE_SIZE

    for i in range(len(inner_cubes)):
        for j in range(3):
            inner_cubes[i][j] += velocities[i][j]

            if abs(inner_cubes[i][j]) > boundary:
                velocities[i][j] = -velocities[i][j]
                inner_colors[i] = [random.random(), random.random(), random.random(), 1.0]

def main():
    global angle_x, angle_y, distance, rotation_speed

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Cubo Rebotando en PyOpenGL")

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    ambient_light = [0.3, 0.3, 0.3, 1.0]
    diffuse_light = [0.7, 0.7, 0.7, 1.0]
    specular_light = [1.0, 1.0, 1.0, 1.0]
    position = [1.0, 1.0, 1.0, 0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)
    glLightfv(GL_LIGHT0, GL_POSITION, position)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    last_mouse_pos = None
    mouse_button_down = False

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    distance -= 0.5
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    distance += 0.5
                elif event.key == pygame.K_UP:
                    inner_cubes.append([0.0, 0.0, 0.0])
                    velocities.append([random.uniform(-0.05, 0.05) for _ in range(3)])
                    inner_colors.append([random.random(), random.random(), random.random(), 1.0])
                elif event.key == pygame.K_DOWN:
                    if len(inner_cubes) > 1:
                        inner_cubes.pop()
                        velocities.pop()
                        inner_colors.pop()
                elif event.key == pygame.K_LEFT:
                    rotation_speed = max(ROTATION_MIN, rotation_speed - ROTATION_STEP)
                elif event.key == pygame.K_RIGHT:
                    rotation_speed = min(ROTATION_MAX, rotation_speed + ROTATION_STEP)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_button_down = True
                    last_mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_button_down = False
            elif event.type == pygame.MOUSEMOTION and mouse_button_down:
                mouse_pos = pygame.mouse.get_pos()
                if last_mouse_pos:
                    delta_x = mouse_pos[0] - last_mouse_pos[0]
                    delta_y = mouse_pos[1] - last_mouse_pos[1]
                    angle_y += delta_x * 0.01
                    angle_x += delta_y * 0.01
                    angle_x = max(min(angle_x, 1.5), -1.5)
                    last_mouse_pos = mouse_pos

        # Rotación automática
        angle_y += rotation_speed

        update_cube_positions()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        camera_x = distance * math.sin(angle_y) * math.cos(angle_x)
        camera_y = distance * math.sin(angle_x)
        camera_z = distance * math.cos(angle_y) * math.cos(angle_x)
        gluLookAt(camera_x, camera_y, camera_z, 0, 0, 0, 0, 1, 0)

        draw_cube(OUTER_CUBE_SIZE, outer_cube_color)

        for i, pos in enumerate(inner_cubes):
            glPushMatrix()
            glTranslatef(*pos)
            draw_cube(INNER_CUBE_SIZE, inner_colors[i])
            glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()