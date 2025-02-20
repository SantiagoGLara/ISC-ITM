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
## virtualizacion
Es la tecnica que permite representar componentes que parecen reales, aunque no existan fisicamente. Consiste en crear entornos virtuales que emulan el comportamiento de sistemas reales.
`anfitrion(host):` hardware o sistema que ofrece la virtualizacion(como virtualbox)

`Huésped(guest):` Sistema o aplicaciones que se ejecutan en el entorno virtualizado

`emulación:` simulacion de un hardware completo mediante software, permitiendo ejecutar ya sean en sistemas o aplicaciones diseñados para una arquitectura distinta, con la desventaja de que es menos eficiente

### virtualizacion asistida por hardware
utiliza caracteristicas del hardware para mejorar la eficiencia de la virtualizacion, se usa para reducir el uso de hardware fisico
### paravirtualizacion
el sistema huesped sabe que está virtualizaco y coopera con el anfitrión. No interactua con el Hardware, pero requiere acceso y modificacion del codigo fuente del sistema huésped. el proyecto XEN es un ejemplo, que permite virtualizar sistemas como linux y windows

----------- 

`Como se pueden utilizar drivers paravirtualizados para optimizar el rendimiento de los dispositivos en una maquina virtual`
Mayor eficiencia en la gestión de recursos

Los drivers paravirtualizados permiten un uso más eficiente de la CPU, memoria, red y almacenamiento, lo que beneficia el rendimiento global del host y de las VMs. Esto es crítico cuando el host ejecuta múltiples VMs.

Ejemplo práctico:

    Controladores de memoria paravirtualizada permiten al hipervisor gestionar dinámicamente la memoria de la VM, ajustando su asignación según sea necesario, lo que optimiza el uso de los recursos disponibles.


-----------
### VPS: Virtual Private Server
maquina virtual, que actúa como un servidor privado de un entorno, en este caso  de una virtualizacion. Cada VPS tiene recursos asignados de manera exclusiva como CPU, RAM y  almacenamiento, aunque comparte hardware fisico con otros VPS en el mismo anfitrión. Como utilizar nuestra maquina como servidor para jugar con otras personas.

#### caracteristicas
- INDEPENDENCIA: Cada VPS tiene su propio S.O, y puede reiniciarse de forma independiente de otras VPS en el mismo servidor
- ESCALABILIDAD: los recursos pueden ejecutarse segun las necesidades del usuario
- AISLAMIENTO: los VPS están separados, lo que significa que el rendimiento o problemas en una no afectan a los demás

#### usos comunes
- Alojamiento web para sitios que requieren mas recursos que los planes de hosting compartido
- Desarrollo y prueba de aplicaciones en entornos controlados
- Servidores de bases de datos o correo
- implementacion de rededs virtuales(VPN)

### sistemas operativos propietarios
Algún individuo o compañia retiene el derecho de autor sobre el programa, negando el acceso al codigo fuente del programa y derecho a copiarlo.
#### caracteristicas
- retencion de derechos de autor
- mayor compatibilidad de software y hardware
- control de calidad y soporte tecnico exclusivo
- Desarrollo y actualizaciones centralizadas
- Modelos de licenciamiento y costos asociados
#### ventajas
- control de calidad
- personal capacitado
- uso comun por usuarios
- software para aplicaciones especificas
- difusion de publicaciones acerca de uso y aplicacion de software
#### desventajas
- soporte ineficiente
- dependencia a proveedores
- descontinuacion de una linea de software
- cursos de aprendizaje costosos
- ilegalidad de copias sin licencia para el efecto
-----
**investigacion: empresas que usan sistemas operativos propietarios y razones para elegirlos**
- Red Hat: tiene su sistema operativo, red hat linux. Software de uso empresarial, con seguridad aumentada, certificaciones de redes,altamente adaptable: soportan implementaciones en servidores físicos, virtuales y entornos de nube híbrida. Esto lo hace ideal para empresas en crecimiento o aquellas que planean migrar a la nube. 