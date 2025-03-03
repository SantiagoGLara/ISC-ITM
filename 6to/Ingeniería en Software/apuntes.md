# Ingeniería de Software
#### DevOps: área que gestiona el desarrollo operativo
#### Producción: etapa final, para el uso público
#### QA: Quality Assurance, aseguramiento de calidad
#### Dev: desarrollo, develop.

### roles SCRUM:
PO<br>
PM<br>
SM<br>
Es importante hacer minutas del proyecto, donde se constatan acuerdos, fechas de entrega de objetivos, etc.
## análisis del requerimiento
### NOM IEE830
Norma para las SRS(Software Requeriment Specification), es una norma que nos ayuda a estandarizar la definicion de requisitos, que nos ayuda en el analisis(hablando en terminos de la PRIMERA fase de vida dentro del ciclo de vida de una app)

#### PARTES DE LA NOM IEE830
como parte de esto, la nom IEEE830 nos aporta una estructura que debe de llevar el documento 
1. INTRODUCCION
    - propuesta
    - alcance
    - definicion
    - referencia
    - Visión General
2. *POR COMPLETAR*

### Instrumentos de recoleccion de datos
- entrevistas
    - estructurada: la entrevista sigue un orden fijo
    - semiestructurada: tiene orden previamente establecido pero segun se desarrolle la entrevista puede cambiar o añadir preguntas
- fuentes primarias: ir directamente al lugar de interes para analizarlo "personalmente", aunque es mala como metodo inicial
- fuentes secundarias: libros, revistas, etc.

`kickoff`: primera entrevista con el cliente, por decirlo asi una "patada inicial" de reconocimiento

### caracteristicas ideales de un objetivo
- deberá ser simple
- deberá iniciar con uno(maximo 2) verbos en infinitivo, ej: implementar, diseñar, crear.

### notas de las partes de un SRS (IEEE 830)
![Documento IEEE830](/6to/Ingeniería%20en%20Software/Referencias/IEEE830_esp.pdf)

**propostio**

proposito del documento, no del proyecto

**2.4 Restricciones**

respecto a las politicas, reglas basicas como por ejemplo el CLE, que se considera finalizado un curso de ingles hasta que acaba sus 5 semestre de ingles.

**2.5 suposiciones y dependencias**

presupociones acerca de factores que pudieran afectar el proceso "originalmente" planeado, por ejemplo, si diseñamos un login en base a CURPS, pero sabemos que no el 100% de la poblacion destino del programa cuenta con una, podemos incluir un formulario para ahi mismo registrarlo en el organismo correspondiente, ahorrandonos tiempo y problemas.

**3 Requisitos especificos**

requisitos a nivel de detalle suficiente como para permitir a los diseñadores diseñar un sistema que satisfaga los requisitos(lo necesario, lo pedido. No hay que sobrepasarse), generalmente perceptibles al usuario.

**4 Apendices**
puede contener todo tipo de informa
cion relevante para la ERS pero que propiamente no pertenecen a la ERS, como formatos de entrada/salida(BPMN, Diagram de componentes,derama de contexto, etc), resultados de analisis de costos, restriccciones acerca del lenguaje de programación.

### trazabilidad de requisitos
Asociacion de un requisito con otros requisitos y las diferentes instancias de los artefactos(diversos productos tangibles/intangibles obtenidos durante el proceso de desarrollo, como documentos, diagramas, SRS, Evaluaciones, etc).

#### Matriz de trazabilidad de requisitos
tipo de documento que contiene los requisitos, en el que se destacan 2 opciones diferentes y se comparan con sus especificiaciones
#### tipos de trazabilidad
1. `trazabilidad directa:`garantiza que todos los requisitos estén vinculados a sus correspondientes casos de diseño y prueba. Se centra en pasar de los requisitos al producto finla,  cuidando que se cumplan los requisitos durante la fase de diseño y prueba, es decir, cuidar que el requisito se cumpla
2. `Trazabilidad hacia atrás:`
3. `trazabilidad hacia ambos lados:` 

**imagen**
**imagen realzacion de pruebas**

es importante trazar y probar los requisitos, si no lo hacemos nuestro producto puede llegar a ser nuo
**imagen matrzi de trazabilidad**

### Despripción de proceso actuales o modelado de negocios
Sirve para modelar los procesos del software, y aunque incorrecto, muchas veces terminamos modelando procesos de la empresa donde trabajamos.
#### diferencias
- `PROCESO:` serie de tareas o actividades interrelacionadas para un fin
- `Analisis de proceso:` comprender el proceso y medir los resultados del como alcanzar el objetivo
- `Modelado:` el trazar el proceso
### Proceso de Desarrollo de Software
### Modelado de negocios

------
detección de problema->analisis

### lenguaje UML
lenguaje estandar para representar y especificar/documentar los elementos que se aunan conforma a POO, es de proposito general, libre y es un estándar

#### diagramas de comportamiento
##### CASOS DE USO 
pwemite realizar especificaciones de alcances funcionales del programa. Es para plazmar las acciones de los actores de la empresa
consta de:
- actores: humano, el sistema, temporizadores o dispositivos.
- casos de uso: acciones de los actores, representados con ovalos. la relacion entre eso y un actor es una `ASOSIACION`, se hace la asosiacion con una linea.
- sistema.
###### relaciones
- asosiación: 
- include: parte "externa" al codigo que tiene que llevar forzosamente, como cuando cargamos un documento. Llamamos una validacón incluida forzosamente
- extends: incluir una situacón pero no es obligatoria, puede ser que no en todas las ejecuciones se realice. Por ejemplo en un sistema puedes llamar un sistema de ayuda, está en determinada ventana, puede ser que la solicite o no.


`documentacion no entregable al cliente:` entrevistas, focus group, diagramas de contextos

### propuesta de proyecto(projecto charter, propuestas de proyecto, plan de proyecto, Acta de proyecto)
objetivo
mapa de tiempos(roadmap) con tiempos estimados
diagrama de gant
presupuesto
analisis de viablidad

objetivo: el cliente firma de acuerdo

### matriz traza
req
descripcion de req
version 
prioridad
objetivo
entregables
diseño
desarrollo 
responsable
prioridad
autor
requisitos asociados
precondicion