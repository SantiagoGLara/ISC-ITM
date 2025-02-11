# Administración de Bases de Datos

## clase 1: conceptos
El dato es la unidad más básica de algo. Una representación (cualificación o cualificación de algo más) que unida a un concepto representa información.

5 características de los datos:
- contextualizado (los datos se procesan con un propósito, que debe ser congruente)
- categorizado (interpretación que lo categoriza)
- calculable
- corrigiendo (depurar datos inconsistentes)
- condensando (juntar de forma precisa)

## clase 2: sistema de información
Hay que buscar el uso objetivo y sin sesgo de los datos.

Para que una base de datos conforme correctamente un sistema, tiene que estar estructurada (un nombre y una edad están asociadas en un registro que es una persona, por ejemplo), interrelacionada (los datos están relacionados para apoyar el contexto, como por ejemplo Pedro está relacionado en un grupo de la materia A). También debe de tener las propiedades ACID. ![ACID](/6to/Administracion%20Base%20de%20Datos/imagenes/0_EEwTVYq-vxJZx-Tn.png)

Y tenemos que procurar que no haya redundancias de datos nocivas (dos registros del mismo individuo que se contradigan, tomando en cuenta que hay redundancias que ayudan, como un respaldo de registros).

Los sistemas son incorporados por usuarios, aplicación (no funge directamente como parte del sistema), Sistemas Gestores de Bases de Datos (nexo entre la aplicación y el sistema), una base de datos, metadatos.
![sistema](/6to/Administracion%20Base%20de%20Datos/imagenes/Screenshot%202025-01-29%20162523.png)

En toda base de datos hay que incorporar metadatos, o más bien, van intrínsecos a ella. Los metadatos son características que le damos a la base de datos para ayudar al contexto, como que una variable sea entera, que no pueda ser nula, que no sea menos que 0; los metadatos regularmente/deberían de ser autodescriptivos, en su contexto se explican a sí mismos.

También tienen usuarios, de tipo externo e interno. Los externos son los usuarios finales, que usan la aplicación y por tanto dan uso de nuestra BDD, pero sin la necesidad de conocer en absoluto como se desenvuelve nuestro sistema; mientras que los internos son los que desarrollan el sistema y por tanto saben cómo funciona total o parcialmente.

Hardware: limita la capacidad del sistema.

Administrador de base de datos, quien coordina cómo funciona la base de datos y asegura que el diseño de la base de datos sea óptimo.

La base de datos debe de estar jerarquizada, jerarquía garantizada por el SGBD, y además debe de estar disponible todo momento que se le requiera. También debe de ser eficiente, es decir, que sin abusar del consumo de recursos de acceso a los datos de forma rápida.

También el sistema debe incluir procesos que nos ayuden al análisis de los datos, que en conjunto con todo lo anteriormente mencionado nos ayudan al propósito final del sistema, proporcionarnos y/o contenernos información de manera correcta.

## clase 3 SQL
para poder administrar una base de datos, necesitamos comunicarnos con el SGBD a través de SQL, con sus 3 sublenguajes:
- DML:Data Modification Lenguaje. sirve para manipular/manejar los registros, desde consultarlos, crearlos, actualizarlos y/o eliminarlos
    - SELECT
    - INSERT
    - DELETE
    - UPDATE
- DCL: Data Control Lenguaje. Sirve para administrar como y que pueden hacer los distintos roles de la base de datos
    - GRANT
    - REVOKE
- DDL:

Para que una base de datos sea considerado buena, debe de tener ciertas características que el SGBD nos da para mantenerlas
- Consistencia: todos los valores deben de ser consistentes, no deben contradecirse(que para ello, debe estar bien diseñada), para ello el SGBD nos otorga el CONTROL DE CONCURRENCIA
    - Control de concurrencia: evita que operaciones de diversos usuarios que traten de modifcar el mismo valor causen conflictos, a través de marcas de tiempo para cada operacion, estableciendo diferencias a veces imperceptibles de tiempo entre una y otra, lo que le da tiempo de actuar al gestor para actualizar el registro de la primera operacion y actuar en consecuencia de los nuevos datos en la siguiente operacion.
    - Bloqueo: cuando una operacion está siendo ejecutada, limita que otra pueda modificar el mismo dato hasta que esta termina.
    - sistema de recuperación: que si por algun fallo imprevisto(no tan letal, como un apagón) tiene sistemas que ayudan a manipular las transacciones que se quedaron a medias
        - REDO: re-hace la operacion que no se terminó de llevar a cabo SI ES QUE PUEDE, si no puede pasa a la siguiente fase "UNDO"
        - UNDO: des-hace la operacion que no se pudo llevar a cabo, como si nunca se hubiera llevado a cabo la transaccion.
- Seguridad: solo deben acceser los autorizados a los datos
    - proteger de datos: no permite que quien no deba tener acceso a los datos o a ciertos datos lo tenga, evitando 2 consultarlos. Para preservar la INTEGRIDAD y CONFIDENCIALIDAD de los datos.
        - mal manejo
        - intrusión
    - Trigger: alerta que pone el administrador de base de datos sobre una accion en una tabla, que en seguridad se utiliza para que cuando se haga una accion sobre una tabla lo anota en un registro(aunque tambien se utliza en otros ambitos, como para modificar datos que dependan de otros, para que sean consistentes.)
    - Alerta: mensajes enviados en caso de alguna situacion alarmante, ya sea asignada por un trigger o por lo que veremos despues, el sistema de monitoreo
    - Monitoreo: sistema que revisa y nos brinda informacion de diversas maneras sobre posibles parametros que pudieren afectar de manera critica la base de datos, como almacenamiento, por poner un ejemplo. Este sistema puede activar alertas
- Disponibilidad: que todo el tiempo podamos acceder a la base de datos, de manera eficiente
## Administrador de Base de Datos
ABD: Experto en varias áreas, como: sistemas de información, diseño y operaciones de una b.d, sgbd, se anticipa a los problemas.

Es el elemento más crítico, protege la CID de la b.d, monitorea y tiene respaldo (plan de contingencia). Actualiza o checa cambios de las aplicaciones y la b.d, obtiene y carga datos masivos, limpia los datos (duplicidades, inconsistencias, etc.), relaciones humanas.

Como abd debes proteger(o minimizar daños) la bd de los usuarios internos y externos o ante ataques, debe checar las capacidades de su equipo de computo.

el administrador de bases de datos necesita establecer indicadores o parametros a monitorear segun la base de datos.

Tambien debe de ser alguien continuamente actualizado, estar al tanto de las nuevas tecnologias como en cualquier área, para que no quede obsoleto.

El administrador de base de datos es tambien responsable de preservar la eficiencia de la base de datos, ademas de tener bien reconocida la capacidad de la base de datos, para saber si es capaz de escalar al alcance de las necesidades.

Otra herramienta para preservar los datos en una base de datos es implementar una herramienta de duplicación, que cuando se procesa un dato se procesa doble. Con el fin de no perderlos, pero a la vez puede complicar, pues amplía la necesidad de almacenamiento, lo que consigo amplia la necesidad de mantenimiento de los dispositivos de almacenamiento, lo que nos abre la posibilidad de acceder a `herramientas en la nube`
### caracterisiticas de un buen administrador de base de datos
Primero que nada, debe de conocer con amplitud la organizacion para la que trabaja, como funciona y que necesita. Debe de saber como mantener los niveles de estabilidad, disponibilidad, eficiencia y escalabilidad. Inclusive, dependiendo del giro de la empresa, tener conocimiento en temas de negocios para que las soluciones que brindemos con la base de datos y sus procesamientos de datos sean fieles a la necesidad que intentamos cubrir.

-----

**Query interesante:**
![nice query](/6to/Administracion%20Base%20de%20Datos/imagenes/image.png)
el insert esta interesante, jala la columna editorial de la tabla libros y la inserta en la tabla editoriales

----

## La nube
se refiere a la entrega de servicios informáticos a través de Internet. En lugar de almacenar datos o ejecutar aplicaciones en servidores locales o computadoras personales, la nube permite acceder a recursos, como almacenamiento, bases de datos, servidores, software y análisis, de manera remota y bajo demanda.

Características principales de la nube:
1. Acceso bajo demanda: Los usuarios pueden acceder a los recursos cuando los necesiten, sin intervención humana directa del proveedor.

2. Escalabilidad: Los recursos pueden ajustarse rápidamente para satisfacer las necesidades cambiantes.

3. Pago por uso: Solo se paga por los recursos que se utilizan, lo que permite optimizar costos.

4. Acceso desde cualquier lugar: Los servicios en la nube están disponibles a través de Internet, lo que permite el acceso desde cualquier dispositivo conectado.

5. Recursos compartidos: Los proveedores de la nube utilizan infraestructuras compartidas para ofrecer servicios a múltiples clientes de manera eficiente.

para fines de un administrador de base de datos vale la pena valorar los riesgos de establecer una base de datos en la nube contra hacerlo localmente, por sus bondades. inclusive, dado el caso, podria ser conveniente hasta segmentarla.
### firewall
proteccion, una barrera de seguridad antes de conectarse a nuestra base de datos. Inclusive pueden haber varios consecutivos. Se le llama zona "desmilitarizada" se llaman zonas aisladas de otras que para navegar entre ella no lleva seguridad, zonas simplemente visibles. Por ejemplo, una pagina de ventas en linea como mercado libre, su zona desmilitarizada es cuando enseña todos sus productos, pero por ejemplo para hacer inserciones o hacer nuevos usuarios, vendedores si necesita más seguridad.

----
definiciones:

BigData:

DataWareHouse:

`Un SGBD es autocontenido cuando:` no necesita herramientas ajenas a él mismo para ejecutarse

### Que tomar en cuenta a la hora de seleccionar un nuevo Gesto de Base de Datos?