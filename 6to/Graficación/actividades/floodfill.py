import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys

# Configuración inicial
pygame.init()
display_width, display_height = 800, 600
try:
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Práctica de Iluminación en OpenGL')
    print("Ventana OpenGL creada correctamente")
except pygame.error as e:
    print(f"Error al crear ventana OpenGL: {e}")
    sys.exit(1)

# Configurar la perspectiva
glViewport(0, 0, display_width, display_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display_width / display_height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -5)

# Habilitar prueba de profundidad y luz
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glClearColor(0.0, 0.0, 0.0, 1.0)

# Definir materiales
def set_material(ambient, diffuse, specular, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

# Configurar luces
def setup_lights():
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 0.0, 1.0, 1.0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.0, 1.0, 0.0, 1.0])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.0, 1.0, 0.0, 1.0])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.5)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.1)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.01)
    glEnable(GL_LIGHT2)
    glLightfv(GL_LIGHT2, GL_POSITION, [-1.0, -1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT2, GL_DIFFUSE, [1.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT2, GL_SPECULAR, [1.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, [1.0, 1.0, -1.0])
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 45.0)
    glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 2.0)

# Dibuja una esfera
def draw_sphere(radius=1.0, slices=32, stacks=32):
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluSphere(quadric, radius, slices, stacks)
    gluDeleteQuadric(quadric)

# Dibuja un cubo
def draw_cube(side=1.0):
    s = side / 2.0
    faces = [
        ([0.0, 0.0, 1.0], [(-s, -s, s), (s, -s, s), (s, s, s), (-s, s, s)]),
        ([0.0, 0.0, -1.0], [(-s, -s, -s), (-s, s, -s), (s, s, -s), (s, -s, -s)]),
        ([0.0, 1.0, 0.0], [(-s, s, -s), (-s, s, s), (s, s, s), (s, s, -s)]),
        ([0.0, -1.0, 0.0], [(-s, -s, -s), (s, -s, -s), (s, -s, s), (-s, -s, s)]),
        ([1.0, 0.0, 0.0], [(s, -s, -s), (s, s, -s), (s, s, s), (s, -s, s)]),
        ([-1.0, 0.0, 0.0], [(-s, -s, -s), (-s, -s, s), (-s, s, s), (-s, s, -s)])
    ]
    for normal, vertices in faces:
        glBegin(GL_QUADS)
        glNormal3fv(normal)
        for v in vertices:
            glVertex3fv(v)
        glEnd()

# Variables
angle = 0.0
light_pos_angle = 0.0
rotation_speed = 1.0
rotation_axis = [0.5, 1.0, 0.0]
ellipse_angle = 0.0
ellipse_radius_x = 1.5
ellipse_radius_y = 0.75
active_lights = [True, True, True]
current_object = 0
current_material = 0

materials = [
    ([0.1, 0.0, 0.0, 1.0], [0.7, 0.0, 0.0, 1.0], [0.7, 0.6, 0.6, 1.0], 32.0),
    ([0.24, 0.20, 0.075, 1.0], [0.75, 0.61, 0.23, 1.0], [0.63, 0.56, 0.37, 1.0], 51.2),
    ([0.0, 0.0, 0.1, 1.0], [0.0, 0.0, 0.7, 1.0], [0.1, 0.1, 0.3, 1.0], 10.0),
    ([0.0215, 0.1745, 0.0215, 1.0], [0.07568, 0.61424, 0.07568, 1.0], [0.633, 0.727811, 0.633, 1.0], 76.8)
]

setup_lights()

print("Controles:")
print("- Teclas 1, 2, 3: Activar/desactivar luces")
print("- ESPACIO: Cambiar entre esfera y cubo")
print("- M: Cambiar material")
print("- Flechas ← → ↑ ↓: Cambiar dirección de rotación")
print("- Teclas + y -: Aumentar/disminuir velocidad de rotación")
print("- ESC: Salir")

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                active_lights[0] = not active_lights[0]
                glEnable(GL_LIGHT0) if active_lights[0] else glDisable(GL_LIGHT0)
                print("Luz direccional " + ("ACTIVADA" if active_lights[0] else "DESACTIVADA"))
            elif event.key == pygame.K_2:
                active_lights[1] = not active_lights[1]
                glEnable(GL_LIGHT1) if active_lights[1] else glDisable(GL_LIGHT1)
                print("Luz puntual " + ("ACTIVADA" if active_lights[1] else "DESACTIVADA"))
            elif event.key == pygame.K_3:
                active_lights[2] = not active_lights[2]
                glEnable(GL_LIGHT2) if active_lights[2] else glDisable(GL_LIGHT2)
                print("Luz focal " + ("ACTIVADA" if active_lights[2] else "DESACTIVADA"))
            elif event.key == pygame.K_SPACE:
                current_object = (current_object + 1) % 2
                print(f"Objeto actual: {'Esfera' if current_object == 0 else 'Cubo'}")
            elif event.key == pygame.K_m:
                current_material = (current_material + 1) % len(materials)
                material_names = ["Plástico rojo", "Metal dorado", "Goma azul", "Esmeralda"]
                print(f"Material actual: {material_names[current_material]}")
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                rotation_speed += 0.5
                print(f"Velocidad de rotación: {rotation_speed}")
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                rotation_speed = max(0.1, rotation_speed - 0.5)
                print(f"Velocidad de rotación: {rotation_speed}")
            elif event.key == pygame.K_LEFT:
                rotation_axis = [0.0, 1.0, 0.0]
                print("Giro: Izquierda a derecha")
            elif event.key == pygame.K_RIGHT:
                rotation_axis = [0.0, -1.0, 0.0]
                print("Giro: Derecha a izquierda")
            elif event.key == pygame.K_UP:
                rotation_axis = [1.0, 0.0, 0.0]
                print("Giro: Abajo a arriba")
            elif event.key == pygame.K_DOWN:
                rotation_axis = [-1.0, 0.0, 0.0]
                print("Giro: Arriba a abajo")

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Movimiento elíptico
    ellipse_angle += 0.01
    ellipse_x = ellipse_radius_x * math.cos(ellipse_angle)
    ellipse_y = ellipse_radius_y * math.sin(ellipse_angle)
    glTranslatef(ellipse_x, ellipse_y, -5.0)

    # Luz puntual en movimiento circular
    light_pos_angle += 0.01
    x = 2.0 * math.sin(light_pos_angle)
    z = 2.0 * math.cos(light_pos_angle)
    glLightfv(GL_LIGHT1, GL_POSITION, [x, 0.0, z, 1.0])

    # Rotar figura
    glRotatef(angle, *rotation_axis)
    angle += rotation_speed

    # Aplicar material
    set_material(*materials[current_material])

    # Dibujar objeto
    draw_sphere(1.0, 32, 32) if current_object == 0 else draw_cube(2.0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Fin del programa")