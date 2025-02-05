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
-----
**Query interesante:**
![nice query](/6to/Administracion%20Base%20de%20Datos/imagenes/image.png)
el insert esta interesante, jala la columna editorial de la tabla libros y la inserta en la tabla editoriales