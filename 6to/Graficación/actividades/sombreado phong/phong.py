import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

pygame.init()
display = (800, 900)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption('Dodecaedro 3D Interactivo')

# Función para crear los vértices del dodecaedro
def create_dodecahedron_vertices():
    phi = (1 + math.sqrt(5)) / 2  # Razón áurea
    scale = 1.0

    # Los 20 vértices del dodecaedro
    vertices = []
    vertices.extend([(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)])
    vertices.extend([(0, 1/phi, phi), (0, 1/phi, -phi), (0, -1/phi, phi), (0, -1/phi, -phi)])
    vertices.extend([(phi, 0, 1/phi), (phi, 0, -1/phi), (-phi, 0, 1/phi), (-phi, 0, -1/phi)])
    vertices.extend([(1/phi, phi, 0), (-1/phi, phi, 0), (1/phi, -phi, 0), (-1/phi, -phi, 0)])

    # Normalizar los vértices para que estén a la misma distancia del origen
    normalized_vertices = []
    for v in vertices:
        length = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
        normalized_vertices.append((v[0]/length * scale, v[1]/length * scale, v[2]/length * scale))

    return normalized_vertices

def create_dodecahedron_faces():
    """Definir las caras del dodecaedro (cada cara es un pentágono)"""
    faces = [
        [0, 8, 10, 2, 16],
        [0, 16, 18, 4, 12],
        [12, 4, 14, 5, 13],
        [13, 5, 9, 11, 1],
        [1, 11, 3, 17, 18],
        [18, 17, 19, 6, 4],
        [14, 6, 15, 7, 5],
        [9, 7, 3, 11],
        [17, 3, 7, 15, 19],
        [19, 15, 6, 14],
        [16, 2, 10, 8, 0]
    ]

    # Completar caras incompletas
    faces[5].append(4)
    faces[8].append(9)
    faces[10].extend([19, 6])

    return faces

# Calcular normal de una cara
def calculate_normal(vertices, face):
    """Calcula la normal de una cara utilizando tres de sus vértices."""
    # Obtener tres vértices de la cara
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]

    # Calcular dos vectores en el plano de la cara
    vector1 = (v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2])
    vector2 = (v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2])

    # Producto cruz para obtener la normal
    normal = (
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    )

    # Normalizar la normal
    length = math.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)
    return (normal[0]/length, normal[1]/length, normal[2]/length)

# Configuración de OpenGL
glViewport(0, 0, display[0], display[1])
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
# Habilitar funciones necesarias de OpenGL
glEnable(GL_DEPTH_TEST)      # Prueba de profundidad
glEnable(GL_LIGHTING)        # Iluminación
glEnable(GL_LIGHT0)          # Primera fuente de luz
glEnable(GL_COLOR_MATERIAL) # Material coloreado
glShadeModel(GL_SMOOTH)      # Sombreado suave (Gouraud)

# Configurar luz
light_ambient   = [0.2, 0.2, 0.2, 1.0]
light_diffuse   = [1.0, 1.0, 1.0, 1.0]
light_specular  = [1.0, 1.0, 1.0, 1.0]
light_position  = [3.0, 3.0, 3.0, 0.0] # Último valor 0 para luz direccional
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
glLightfv(GL_LIGHT0, GL_POSITION, light_position)

# Configurar material
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

# Crear vértices y caras del dodecaedro
vertices = create_dodecahedron_vertices()
faces = create_dodecahedron_faces()

# Generar colores para las caras
face_colors = []
for i in range(len(faces)):
    # Generar colores variados para cada cara
    hue = i / len(faces)
    r = 0.5 + 0.5 * math.sin(hue * 2 * math.pi)
    g = 0.5 + 0.5 * math.sin(hue * 2 * math.pi + 2 * math.pi / 3)
    b = 0.5 + 0.5 * math.sin(hue * 2 * math.pi + 4 * math.pi / 3)
    face_colors.append((r, g, b))

# Variables para la rotación
rotation_x = 0
rotation_y = 0
rotation_z = 0
shading_mode = 0 # 0: Flat, 1: Gouraud

# Nuevas variables para la traslación y el zoom
translation_x = 0
translation_y = 0
zoom_factor = -5  # Valor inicial de zoom

# Inicialización de 'running' y 'clock'
running = True
clock = pygame.time.Clock()

# Variables para el arrastre del ratón
dragging = False
previous_mouse_pos = (0, 0)

def draw_dodecahedron():
    for i, face in enumerate(faces):
        # Calcular normal de la cara para iluminación
        normal = calculate_normal(vertices, face)

        # Usar color específico para esta cara
        glColor3fv(face_colors[i])

        # Dibujar cara como polígono
        glBegin(GL_POLYGON)
        # Para sombreado plano, una sola normal por cara
        if shading_mode == 0: # Flat shading
            glNormal3fv(normal)
        for vertex_index in face:
            # Para sombreado Gouraud, normal por vértice
            if shading_mode == 1: # Gouraud shading
                glNormal3fv(vertices[vertex_index])
            glVertex3fv(vertices[vertex_index])
        glEnd()

        # Dibujar bordes de las caras
        glColor3f(0.2, 0.2, 0.2)  # Color de los bordes
        glBegin(GL_LINE_LOOP)
        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])
        glEnd()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Cambiar modo de sombreado
                shading_mode = 1 - shading_mode
                if shading_mode == 0:
                    print("Sombreado: Plano")
                else:
                    print("Sombreado: Gouraud")
            elif event.key == pygame.K_l:
                # Cambiar posición de la luz
                light_position[0] += 0.5
                glLightfv(GL_LIGHT0, GL_POSITION, light_position)
                print(f"Luz movida a: {light_position}")
            elif event.key == pygame.K_UP:
                translation_y += 0.1
            elif event.key == pygame.K_DOWN:
                translation_y -= 0.1
            elif event.key == pygame.K_LEFT:
                translation_x -= 0.1
            elif event.key == pygame.K_RIGHT:
                translation_x += 0.1
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Para '+'
                zoom_factor += 0.5
            elif event.key == pygame.K_MINUS:
                zoom_factor -= 0.5
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                dragging = True
                previous_mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                current_mouse_pos = event.pos
                delta_x = current_mouse_pos[0] - previous_mouse_pos[0]
                delta_y = current_mouse_pos[1] - previous_mouse_pos[1]
                rotation_x += delta_y * 0.2
                rotation_y += delta_x * 0.2
                previous_mouse_pos = current_mouse_pos

    # Incrementar ángulos de rotación (automática)
    rotation_x += 0.5
    rotation_y += 0.7
    rotation_z += 0.1

    # Limpiar buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Dibujar escena
    glLoadIdentity()
    glTranslatef(translation_x, translation_y, zoom_factor)  # Aplicar traslación y zoom
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)
    glRotatef(rotation_z, 0, 0, 1)

    # Configurar la luz (puede ser movida)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Dibujar el dodecaedro
    draw_dodecahedron()

    # Actualizar pantalla y controlar FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
