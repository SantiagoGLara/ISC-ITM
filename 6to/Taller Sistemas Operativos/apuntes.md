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
