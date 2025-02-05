# Taller Sistemas Operativos

## Propósito General

### Servidores
El propósito de los **servidores** es ofrecer servicios a otros dispositivos o usuarios, generalmente a través de una red. Están diseñados para manejar múltiples solicitudes simultáneas y proporcionar recursos compartidos de manera eficiente.

### Sistemas Embebidos
Los **sistemas embebidos** están diseñados para realizar una tarea específica dentro de un dispositivo. Generalmente, tienen un enfoque en el rendimiento y la eficiencia, con recursos limitados y un control más directo sobre el hardware.

---

## Estructura Genérica de un Sistema Operativo

### Capa de Hardware
La **capa de hardware** es la capa más baja del sistema operativo. Esta capa incluye los componentes físicos del sistema, como la CPU, la memoria, los dispositivos de entrada y salida, etc. El sistema operativo depende de esta capa para interactuar con los recursos físicos.

### Núcleo (Kernel)
El **núcleo** es el corazón del sistema operativo. Su función principal es gestionar los recursos de la computadora, como la memoria, los procesos y los dispositivos de entrada/salida. Actúa como intermediario entre el hardware y las aplicaciones, asegurando que las aplicaciones puedan utilizar los recursos de manera eficiente sin interferir entre sí.

### Espacio de Usuario
El **espacio de usuario** es donde se ejecutan las aplicaciones que usa el usuario final. Este espacio garantiza la **estabilidad y seguridad del sistema**, ya que las aplicaciones no pueden acceder directamente a los recursos del sistema sin pasar por el núcleo. Además, mediante **interfaces gráficas**, el sistema operativo interactúa con el usuario, ofreciendo una experiencia amigable y controlada.

### proceso y multiprogramacion
programa: entidad pasiva, lista de instrucciones
proceso: entidad activa resultado de ejecutar un programa
relacion: un programa ejecuta multiples procesos
#### proceso en un sistema multiprogramacion
el proceso es la imagen en memoria de un programa junto con suestado de ejecución. Una tarea es menor compleja, no tiene interrupciones ni cambios de estado, mientras que el proceso puede ser interrumpido y gestionado dinamicamente
##### ilusion de simultaneidad
gracias a la multiprogramacion, el sistema hace la ilusion de que hay varios procesos se ejecutan a la vez, pero en realidad es uno detras de otro. Solo los que4 tienen un procesador asignado están realmente ejecutandose, los demas están esperando ya que no tienen aun recursos asignados.
#### ciclo de vida de un proceso
- nuevo: creado no ejecutado
- listo: esperando asignacion de procesador
- ejecución: instrucciones siendo procesadas
- bloqueado: esperando evento externo
- zombie: finalizado pero el SO aun no lo limpia
- terminado: proceso completamente eliminado