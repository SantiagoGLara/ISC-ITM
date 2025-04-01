import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math
import numpy as np


def init_pygame():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Transformaciones en 3D")

    return pygame.font.SysFont('Arial', 18)


def init_openGL():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)


def draw_axes():
    glBegin(GL_LINES)

    # Eje x (color rojo)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)

    # Eje y (color verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)

    # Eje z (color azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 2.0)

    glEnd()


def draw_cube():
    vertices = [
        (-0.5, -0.5, 0.5),
        (0.5, -0.5, 0.5),
        (0.5, 0.5, 0.5),
        (-0.5, 0.5, 0.5),

        (-0.5, -0.5, -0.5),
        (0.5, -0.5, -0.5),
        (0.5, 0.5, -0.5),
        (-0.5, 0.5, -0.5),
    ]

    caras = [
        (0, 1, 2, 3),  # Cara frontal
        (4, 5, 6, 7),  # Cara trasera
        (0, 4, 7, 3),  # Cara izquierda
        (1, 5, 6, 2),  # Cara derecha
        (3, 2, 6, 7),  # Cara superior
        (0, 1, 5, 4),  # Cara inferior
    ]

    colores = [
        (1.0, 0.0, 0.0, 1.0),
        (0.0, 1.0, 0.0, 1.0),
        (0.0, 0.0, 1.0, 1.0),
        (1.0, 1.0, 0.0, 1.0),
        (1.0, 0.0, 1.0, 1.0),
        (0.0, 1.0, 1.0, 1.0),
    ]

    glBegin(GL_QUADS)
    for i, cara in enumerate(caras):
        glColor4fv(colores[i])
        for vertices_idx in cara:
            glVertex3fv(vertices[vertices_idx])
    glEnd()

    glColor4f(1.0, 1.0, 1.0, 1.0)

    aristas = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]

    glBegin(GL_LINES)
    for arista in aristas:
        for vertice_idx in arista:
            glVertex3fv(vertices[vertice_idx])
    glEnd()


def draw_pyramid():
    vertices = [
        (0.0, 0.5, 0.0),
        (-0.5, -0.5, 0.5),
        (0.5, -0.5, 0.5),
        (0.5, -0.5, -0.5),
        (-0.5, -0.5, -0.5),
    ]

    caras_triangulares = [
        (0, 1, 2),
        (0, 2, 3),
        (0, 3, 4),
        (0, 4, 1),
    ]

    base = (1, 2, 3, 4)

    colores = [
        (1.0, 0.0, 0.0, 1.0),
        (0.0, 1.0, 0.0, 1.0),
        (0.0, 0.0, 1.0, 1.0),
        (1.0, 1.0, 0.0, 1.0),
        (0.5, 0.5, 0.5, 1.0),
    ]

    glBegin(GL_TRIANGLES)
    for i, cara in enumerate(caras_triangulares):
        glColor4fv(colores[i])
        for vertice_idx in cara:
            glVertex3fv(vertices[vertice_idx])
    glEnd()

    glBegin(GL_QUADS)
    glColor4fv(colores[4])
    for vertice_idx in base:
        glVertex3fv(vertices[vertice_idx])
    glEnd()

    glColor4f(1.0, 1.0, 1.0, 1.0)
    aristas = [
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (2, 3), (3, 4), (4, 1),
    ]

    glBegin(GL_LINES)
    for arista in aristas:
        for vertice_idx in arista:
            glVertex3fv(vertices[vertice_idx])
    glEnd()


def draw_sphere(radius=0.5, slices=20, stacks=20):
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    gluSphere(quadric, radius, slices, stacks)
    gluDeleteQuadric(quadric)


def render_text(font, text, position, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    width, height = text_surface.get_size()

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_DEPTH_TEST)
    glRasterPos2i(position[0], position[1])
    glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    glEnable(GL_DEPTH_TEST)

    glPopMatrix()


def create_transformation_matriz(translation, rotation, scale):
    rx = math.radians(rotation[0])
    ry = math.radians(rotation[1])
    rz = math.radians(rotation[2])

    rot_x = np.array([
        [1, 0, 0, 0],
        [0, math.cos(rx), -math.sin(rx), 0],
        [0, math.sin(rx), math.cos(rx), 0],
        [0, 0, 0, 1]
    ])

    rot_y = np.array([
        [math.cos(ry), 0, math.sin(ry), 0],
        [0, 1, 0, 0],
        [-math.sin(ry), 0, math.cos(ry), 0],
        [0, 0, 0, 1]
    ])

    rot_z = np.array([
        [math.cos(rz), -math.sin(rz), 0, 0],
        [math.sin(rz), math.cos(rz), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    scale_matriz = np.array([
        [scale[0], 0, 0, 0],
        [0, scale[1], 0, 0],
        [0, 0, scale[2], 0],
        [0, 0, 0, 1]
    ])

    trans_matriz = np.array([
        [1, 0, 0, translation[0]],
        [0, 1, 0, translation[1]],
        [0, 0, 1, translation[2]],
        [0, 0, 0, 1]
    ])

    rot_matriz = np.matmul(np.matmul(rot_z, rot_y), rot_x)

    return np.matmul(np.matmul(trans_matriz, rot_matriz), scale_matriz)


def main():
    font = init_pygame()
    init_openGL()

    object_type = 2

    translation = [0.0, 0.0, 0.0]
    rotation = [0.0, 0.0, 0.0]
    scale = [1.0, 1.0, 1.0]

    auto_rotation = False
    rotation_speed = 1.0
    show_matrix = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    auto_rotation = not auto_rotation
                elif event.key == pygame.K_TAB:
                    object_type = (object_type + 1) % 3
                elif event.key == pygame.K_m:
                    show_matrix = not show_matrix
                elif event.key == pygame.K_r:
                    translation = [0.0, 0.0, 0.0]
                    rotation = [0.0, 0.0, 0.0]
                    scale = [1.0, 1.0, 1.0]
                elif event.key == pygame.K_w:
                    translation[1] += 0.1
                elif event.key == pygame.K_s:
                    translation[1] -= 0.1
                elif event.key == pygame.K_a:
                    translation[0] -= 0.1
                elif event.key == pygame.K_d:
                    translation[0] += 0.1
                elif event.key == pygame.K_q:
                    translation[2] += 0.1
                elif event.key == pygame.K_e:
                    translation[2] -= 0.1
                elif event.key == pygame.K_u:
                    rotation[0] += 10.0
                elif event.key == pygame.K_j:
                    rotation[0] -= 10.0
                elif event.key == pygame.K_i:
                    rotation[1] += 10.0
                elif event.key == pygame.K_k:
                    rotation[1] -= 10.0
                elif event.key == pygame.K_o:
                    rotation[2] += 10.0
                elif event.key == pygame.K_l:
                    rotation[2] -= 10.0
                elif event.key == pygame.K_z:
                    scale = [s + 0.1 for s in scale]
                elif event.key == pygame.K_x:
                    scale = [max(0.1, s - 0.1) for s in scale]
                elif event.key == pygame.K_c:
                    scale[0] += 0.1
                elif event.key == pygame.K_v:
                    scale[1] += 0.1
                elif event.key == pygame.K_b:
                    scale[2] += 0.1
                elif event.key == pygame.K_n:
                    scale[0] = max(0.1, scale[0] - 0.1)
                elif event.key == pygame.K_g:
                    scale[1] = max(0.1, scale[1] - 0.1)
                elif event.key == pygame.K_h:
                    scale[2] = max(0.1, scale[2] - 0.1)

        if auto_rotation:
            rotation[0] += 0.5 * rotation_speed
            rotation[1] += 0.8 * rotation_speed
            rotation[2] += 0.3 * rotation_speed

        # Limpiar la pantalla y el buffer de profundidad
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Posicionar la cámara
        gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)

        # Dibujar los ejes de coordenadas
        draw_axes()

        # Crear matriz de transformación
        transform = create_transformation_matriz(translation, rotation, scale)
        transform_gl = transform.T.flatten()

        glPushMatrix()
        glMultMatrixf(transform_gl)

        # Dibujar el objeto seleccionado
        if object_type == 0:
            draw_cube()
        elif object_type == 1:
            draw_pyramid()
        else:
            draw_sphere()

        glPopMatrix()

        # Mostrar información en pantalla
        info_text = [
            f"Objeto: {'Cubo' if object_type == 0 else 'Pirámide' if object_type == 1 else 'Esfera'} (TAB para cambiar)",
            f"Traslación: X={translation[0]:.1f}, Y={translation[1]:.1f}, Z={translation[2]:.1f} (WASDQE)",
            f"Rotación: X={rotation[0]:.1f}, Y={rotation[1]:.1f}, Z={rotation[2]:.1f} (UIOJKL)",
            f"Escala: X={scale[0]:.1f}, Y={scale[1]:.1f}, Z={scale[2]:.1f} (ZXCVBN/GH)",
            f"Rotación automática: {'Activada' if auto_rotation else 'Desactivada'} (ESPACIO)",
            "Presiona R para resetear transformaciones",
            "Presiona M para mostrar/ocultar matriz",
            "Presiona ESC para salir"
        ]

        for i, text in enumerate(info_text):
            render_text(font, text, (10, 10 + i * 20))

        # Mostrar matriz de transformación si está activada
        if show_matrix:
            matrix_text = [
                "Matriz de transformación:",
                f"[{transform[0, 0]:.2f}, {transform[0, 1]:.2f}, {transform[0, 2]:.2f}, {transform[0, 3]:.2f}]",
                f"[{transform[1, 0]:.2f}, {transform[1, 1]:.2f}, {transform[1, 2]:.2f}, {transform[1, 3]:.2f}]",
                f"[{transform[2, 0]:.2f}, {transform[2, 1]:.2f}, {transform[2, 2]:.2f}, {transform[2, 3]:.2f}]",
                f"[{transform[3, 0]:.2f}, {transform[3, 1]:.2f}, {transform[3, 2]:.2f}, {transform[3, 3]:.2f}]"
            ]

            for i, text in enumerate(matrix_text):
                render_text(font, text, (10, 200 + i * 20))

        # Actualizar la pantalla
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()