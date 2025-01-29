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
