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

### Instancia

Una instancia de una base de datos es el conjunto de estructuras de memoria y de procesos que acceden a los archivos de datos.

Cada instancia está asociada a una base de datos. Cuando se inicia una base de datos en un servidor (independientemente del tipo de computadora), se le asigna un área de memoria (SGA) y se lanza uno o más procesos. La combinación del SGA y de los procesos es lo que se llama instancia. La memoria y los procesos de una instancia gestionan los datos de la base de datos asociada de forma eficiente y sirven a uno o varios usuarios.
    Cuando se inicia una instancia el DBMS monta la base de datos. Es decir, cuando una instancia se asocia a la base de datos correspondiente, en una misma computadora pueden coexistir varias instancias simultáneamente, accediendo cada una a su propia base de datos.
    Únicamente el administrador de la base de datos puede iniciar una instancia y abrir una base de datos. Si una base de datos está abierta, entonces el administrador puede cerrarla, cuando esto ocurre, los usuarios no pueden acceder a la información que contiene.

Para que un SGBD pueda funcionar, primero se debe crear una instancia de este. La instancia está formada por tres tipos de componentes:

- Archivos
- Estructuras de memoria
- Estructuras de procesos

Funcionamiento de la memoria

La estructura de la memoria está formada por tres áreas básicas:

- SGA (Área Global del Sistema): Asignada al iniciar la instancia y es el componente fundamental de una instancia.
- PGA (Área Global de Programas): Asignada al iniciar un proceso de servidor.
- UGA (Área Global de Usuario): Asignada a cada sesión de usuario. Se localiza en la SGA si el usuario se conecta a la base de datos usando un servidor compartido, pero se ubica en la PGA si se utiliza un servidor dedicado.
## unidad 2 

### El SGA

El SGA es un área de memoria compartida que se utiliza para almacenar información de control y de datos de la instancia. Se crea cuando la instancia se levanta y se borra cuando esta se deja de usar (cuando se ha cerrado).

Es un grupo de estructuras de memoria compartida que contiene datos e información de control de una base de datos.
Varios procesos pueden acceder de forma concurrente a la misma instancia, accediendo a la información contenida en el SGA, por lo que también se llama Shared Global Area.
![SGA-Diagrama](/6to/Administracion%20Base%20de%20Datos/imagenes/SGA.png)

### Procesos en 2do plano
- `DBWR` es el DataBaseWriter, el encargado de hacer escrituras sobre las bases de datos. Una vez liberados los bloques de informacion modificados, es el encargado de actualizar esos bloques. Trabaja con los buffers, para no desgastar en exceso la memoria. Tambien es encargado de liberar los buffers, periodicamente o según se necesite transportar datos.

- `LGWR` Log, es el que tiene los registros de que se estaba haciendo operacion a operacion. Para el log, hay 3 parametros que le marcan que una operacion se haya realizado. Si se llegó a un commit, si se llenó el buffer y hay que vaciarlo para trabajar con mas informacion y si ya pasó cierto tiempo.

    idempotente: si se daña una operacion que ya estaba hecha, no afecta el resultado. Por ejemplo, si una operacion se interrumpe pero ya habia actualizado sus cambios, el redo va a tratar de volverlas a hacer, si no cuidaramos la idempotencia de la bdd, al re-hacerla pero ya estaba hecha, habría una alteracion del resultado deseado. parte de esto es lo que nos ayuda a hacer el `LGWR`
- `CKPT: `Es el checkpoint, un punto a donde regresar en caso de tragedia, de sincronizacion para actualizar las cabeceras de los datos, limpiar buffers y volver a empezar. Recordando, todos los datos tienen una cabecera que nos habla de su estátus, el CKPT se encarga de actualizar esta.
- `SMON: `System Monitor. Se encarga de realizar las actualizaciones necesarias es recuperar la base de datos, el que cuando algo que no se termina de registrar en la bdd, lo registra. Se activa cada cierto tiempo para verificar que todo esté en orden
- `PMON: `Process Monitor, registra las operaciones no realizadas de una transaccion y regresa la BDD a un estado consistente, liberando datos bloqueados / semimodificados en transacciones fallidas. Se podría decir que es el que hace el ROLLBACK; de igual manera que el SMON despierta cada cierto tiempo
- `ARC` archivado, ayuda a archivar los datos de cada usuario, como tal no participa tan de manera tan activa como el DBWR, pero si es necesario le apoya, subyugado a él.
- `MMON: `Monitor de manejabilidad, se encarga de controlar las tareas relacionadas con AWR. 
- `AWR: `Area de Volcado para las Estadisticas monitoriea las operaciones realizadas y va generando estadisticas para que sean monitoreadas.
- `CJQ: `Coordinador de Cola de Trabajos(QUERY JOB COORDINATOR). Cualquier requerimiento de los usuarios necesita un trabajo, así que se le asigna un orden. Tambien se necesita manejar su prioridad, aplazar los que no se puedan hacer, etc. Toda esta coordinacion la maneja el CJQS

### DATAFILE & TABLESPACE
DataFile es el espacio fisico donde se almacenan los datos, y Tablespace es el espacio logico donde accedemos a estos datos, un tablespace puede estar dividio en multiples datafiles

principales TableSpaces:
- `System:`
- `Sysaux:` espacio de contenido auxiliar de las bases de datos, en teoria ni si quiera el administrador debe acceder a este tablespace
- `user1:` espacio para todas las bases de datos, tanto de usuarios como el administrador. En este caso, es comun ver que se crean diversos TableSpaces similares a este, en bases de datos grandes o cuando tenemos bases de datos distribuidas tambien se recomienda distribuir tambien los tablespaces
- `temp:` datos de uso temporal, para guardar datos de procesos que requieren un apoyo, un espacio de almacenamiento temporal para que los procesos tengan acceso rapido a la informacion. Persé los usuarios no modificamos este espacio, si no que es el mismo gestor con los procesos que llevamos a cabo
- `UNDO:` Espacio para cuando ejecutamos espacios transaccionales, espacio donde se queda lo que hay que recuperar. Inclusive, sirve para recuperar los datos que incluso se pierden, ademas que ayuda a monitorear las transacciones; y puede ademas tener subUndo para diversas tareas especificas. Depende el gestor de bases de datos, puede hacer que `undo` sea un tableSpace o un segmento dentro de todos los TableSpaces

un TableSpace puede tener varios segmentos, cada segmento está relacionado con tablas e indices. Podemos tener segmentos de usuario, segmentos de datos, segmentos de indice Y segmento de LOB. Y a su vez, un segmento puede tener multiples extensiones. Por ejemplo: yo creo una tabla, a esa tabla se le asigna un segmento disponible, segmento cuyo espacio predeterminado 10mb, y llega un momento en el que la tabla llena el espacio del tableSpace, ahí es cuando se usa una `extensión`. En este caso aunque logicamente hacemos una extension que todo queda junto, fisicamente lo mas probable es que no queden contiguos, aunque tambien lleva su cierta organizacion para evitar la FRAGMENTACION. Podemos añadir extensiones del mismo tamaño del mismo segmento original o fragmento de.

----

`LOB: Large Objects, son objetos que no se pueden dividir, objetos grandes. Por ejemplo imagenes, porque no los podemos dividir.` Una tabla por más registros que tenga no se considera un large object, porque puede 'dividirse' por cada uno de sus registros, es decir, la podemos ver por sus multiples registros pequeños. 

---
Una extesión puede contener varios bloques, cuyo espacio tiene que ser multiplos de 4K, es decir, multiplos de los bloques fisicos de nuestro disco duro. 
### bloque:
los bloque se conforman de diversas partes, pero sigue la siguiente estructuras
![alt text](/6to/Administracion%20Base%20de%20Datos/imagenes/estructura%20bloque.png)

![alt text](/6to/Administracion%20Base%20de%20Datos/imagenes/extension%20de%20bloques.png)

### OLAP Y OLTP
El procesamiento analítico en línea (OLAP) y el procesamiento de transacciones en línea (OLTP) son dos diferentes sistemas de procesamiento de datos que ayudan a almacenar y analizar datos empresariales de manera muy distinta. 

El OLAP combina y agrupa los datos para que pueda analizarlos desde diferentes puntos de vista, puede recopilar y almacenar datos de muy diversas fuentes, como sitios web, aplicaciones, medidores inteligentes y sistemas internos. 

Mientras que el OLTP almacena y actualiza grandes volúmenes de datos transaccionales de manera confiable y eficiente. Las bases de datos de OLTP pueden ser uno de los diferentes orígenes de datos para un sistema de OLAP.

#### Importancia del OLAP

El procesamiento analítico en línea (OLAP) ayuda a las organizaciones a procesar y beneficiarse de una cantidad cada vez mayor de información digital. Algunos de los beneficios de OLAP son los siguientes. 

#### Toma de decisiones acertadas
Las empresas utilizan OLAP para tomar decisiones rápidas y precisas a fin de mantenerse competitivas en una economía acelerada. Hacer consultas analíticas en bases de datos relacionales consume mucho tiempo porque necesita buscar en varias tablas de datos. En cambio, los sistemas OLAP procesan e integran previamente los datos para que se puedan generar los informes analíticos empresariales más rápido y cuando sea necesario.

#### No requiere conocimientos técnicos

Los sistemas OLAP facilitan el análisis de datos complejos para los analistas empresariales sin conocimientos técnicos. Los directivos de la empresa pueden realizar cálculos analíticos complejos y generar informes gerenciales sin tener que aprender a operar las bases de datos.

#### Vista de datos integrada
OLAP proporciona una visión unificada de las distintas unidades empresariales. Los administradores y tomadores de decisiones pueden ver el panorama general y resolver los problemas de manera efectiva. Pueden llevar a cabo análisis hipotéticos, que anticipen el impacto de las decisiones tomadas por un departamento sobre las otras áreas de la empresa.

#### Similitudes entre el OLAP y el OLTP

Tanto el procesamiento analítico en línea (OLAP) como el procesamiento de transacciones en línea (OLTP) son sistemas de administración de bases de datos que almacenan y procesan grandes volúmenes de datos. Ambos necesitan una infraestructura de TI eficiente y confiable para funcionar sin problemas. Pueden utilizarse tanto para consultar datos existentes como para almacenar datos nuevos. Ambos respaldan la toma de decisiones basada en los datos de una organización.

La mayoría de las empresas utilizan los sistemas de OLTP y OLAP juntos para cumplir con sus necesidades de inteligencia empresarial. Diferencias entre el OLAP y el OLTP El propósito principal del procesamiento analítico en línea (OLAP) es analizar los datos agregados, mientras que el propósito principal del procesamiento de transacciones en línea (OLTP) es procesar las transacciones de bases de datos.

Los sistemas de OLAP se utilizan para generar informes, realizar análisis de datos complejos e identificar tendencias. Por el contrario, los sistemas de OLTP se utilizan para procesar pedidos, actualizar el inventario y administrar las cuentas de los clientes. Por lo cual, se consideran las siguientes características específicas para cada caso: 

#### Formato de datos
Los sistemas de OLAP utilizan modelos de datos multidimensionales, para poder ver los mismos datos desde diferentes ángulos. Las bases de datos de OLAP almacenan los datos en formato de hipercubo, donde cada dimensión representa un atributo diferente. Cada celda del cubo representa un valor o una medida para la intersección de todas las dimensiones.

Por el contrario, los sistemas de OLTP utilizan una base de datos relacional para organizar los datos en tablas. Cada fila de la tabla representa una instancia de una entidad y cada columna representa un atributo de la entidad.

#### Arquitectura de datos
La arquitectura de las bases de datos de OLAP prioriza la lectura de datos sobre las operaciones de
escritura de datos. Puede realizar consultas complejas de forma rápida y eficiente en grandes volúmenes de datos. La disponibilidad no es un aspecto de alta prioridad, ya que el principal caso de uso son los análisis. 

Por otro lado, la arquitectura de las bases de datos de OLTP prioriza las operaciones de escritura de datos. Está dirigida para atender un gran volumen de operaciones que requieren actualizar datos transaccionales sin comprometer la integridad de la base de datos.

Por ejemplo, si varios clientes compran el mismo artículo al mismo tiempo, el sistema de OLTP puede actualizar los niveles de existencias con precisión. Además, el sistema priorizará cronológicamente a los clientes si el artículo es el último en existencias. La disponibilidad es una prioridad alta, por lo general, se logra mediante múltiples copias de seguridad de datos.
#### Rendimiento
Los tiempos de procesamiento del OLAP pueden requerir de varios minutos e incluso de horas según el tipo y el volumen de datos que se analicen. Para actualizar una base de datos de OLAP, se procesan periódicamente grandes lotes de datos que se cargan una sola vez al sistema. La frecuencia de actualización dedatos puede ser diaria, semanal o incluso mensual.

Por el contrario, los tiempos de procesamiento del OLTP se miden en milisegundos. Las bases de datos de OLTP administran las actualizaciones de las bases de datos en tiempo real. Las actualizaciones son rápidas, breves y constantes. Se emplea un procesamiento de flujos en lugar del procesamiento por lotes.
#### Requisitos
Los sistemas de OLAP actúan como un almacén de datos centralizado (Data Warehouse) y extraen datos de múltiples almacenamientos, bases de datos
relacionales y otros sistemas. Los requisitos de almacenamiento van desde terabytes (TB) hasta petabytes (PB). Las lecturas de datos también pueden requerir un uso intensivo de recursos de computación y necesitar servidores de alto rendimiento.

Por otro lado, puede medir los requisitos de almacenamiento del OLTP en gigabytes (GB). Las bases de datos de OLTP también se pueden limpiar una vez que los datos se pasan a un almacenamiento de datos de OLAP relacionado. Los requisitos de computación de los sistemas de OLTP también son altos.

#### Ejemplo de las diferencias entre el OLAP y el OLTP
Considere el caso de una gran cadena minorista que opera cientos de tiendas a lo largo de todo el país. Esta empresa tiene una enorme base de datos que hace un seguimiento de las ventas, el inventario, los datos de los clientes y proveedores. 

La empresa utiliza un sistema de OLTP para procesar las ventas en tiempo real, Cada tienda está conectada a la base de datos central, que actualiza los niveles de inventario en tiempo real a medida que se venden los productos, también usa la tecnología de OLTP para administrar las operaciones en las cuentas de los clientes, como registrar los puntos de fidelidad, actualizar la información de los pagos y procesar las devoluciones. 

Por otro lado, la empresa utiliza un sistema de OLAP para analizar los datos recopilados por el sistema de OLTP. Los analistas financieros de la empresa pueden utilizar el OLAP para generar informes sobre las tendencias de ventas, los niveles de inventario, la demografía de los clientes y otras métricas. Realizan consultas complejas sobre grandes volúmenes de datos históricos para identificar patrones y tendencias que puedan servir para tomar decisiones empresariales. Identifican los productos populares por temporada y utilizan la información para optimizar los presupuestos de inventario.
El procesamiento analítico en línea (OLAP) y el procesamiento de transacciones en línea (OLTP) son dos sistemas de procesamiento de datos diferentes diseñados para propósitos distintos. El sistema de OLAP está dirigido hacia el análisis de datos e informes complejos, mientras que el sistema de OLTP está orientado para el procesamiento transaccional y las actualizaciones en tiempo real.

Entender las diferencias entre estos sistemas puede ser de ayuda para tomar decisiones informadas sobre qué sistema satisface mejor sus necesidades. En muchos casos, una combinación de ambos sistemas puede ser la mejor solución para las empresas que requieren tanto el procesamiento de transacciones como el análisis de datos. En última instancia, elegir el sistema correcto depende de las necesidades específicas de su empresa, lo que incluye el volumen de datos, la complejidad de las consultas, el tiempo de respuesta, la escalabilidad y el costo.

![OLAP vs. OLTP](/6to/Administracion%20Base%20de%20Datos/imagenes/OLAPvsOLTP.png)

normalmente OLAP lo usan mucho analistas de mercado, financieros. Les sirve mucho para basarse en supuestos, para hacer simulaciones para tratar de predecir lo que va a pasar.

### SMON, PMON Y LGWR
procesos en segundo plano basicos 

SMON: system monitor
PMON: Process Monitor
LGWR: Log writer

### estados para iniciar una instancia

startup>nomount>mount>open

en startup es el estado en el que comienza a arrancar el servidor, despues en nomount se prepara la instancia de la bdd(sin usarla), para que en mount inicie la instancia y se monte la base de datos, para que quede en el estado OPEN

#### nomount
aqui es donde se crean los archivos PFILE(parametros legibles/registrados en un archivo de texto, donde los cambios se realizan hasta que se reinicie el sistema) y SPFILE(server parameter file, archivo binario. los cambios se hacen en cuanto los ejecutamos), que son archivos de parametros, donde se crean variables con las que tienen metricas para ajustar el servidor, entonces en el nomount se leen esos archivos y estos son los que configuran el SGA(system global area, para la instancia)

#### mount
aqui se crean los control file, donde se definen los datafile y tablespaces. En este estado unicamente el administrador tiene acceso a la base de datos.

----

STARTUP NO MOUNT

ALTER DATABASE MOUNT/OPEN

#### shutdown
hay 4 tipos de shutdown que nos da el sistema, diferenciadas con como trata las instancias(usuarios) activos
- normal: no se admitirán nuevas conexiones a la bd, pero mantiene las conexiones actualez hasta que se desconecten los usuarios. Cuando se cierra la ultima conexion, la BDD pasa al estado CLOSED, establece un checkpoint y se vacian los buffers y se registra en disco lo que quede en memoria.
- inmediate: no se aceptan nuevas conexiones, las conexiones actuales se cierran inmediatamente, cancelando las transacciones en curso con un rollback
- transactional: mantiene abiertas unicamente las sesiones con transacciones en transcurso y espera a que terminen. Cuando un usuario ya no tiene transacciones activas le cierra las sesión.
- abort
### TRANSACT SQL
Lenguaje estructurado por lotes(coleccion de instrucciones)

----
programacion batch: programacion donde se ejecuta un conjunto de instrucciones, sin interaccion. Unicamente se espera que se ejecute con o sin éxito.

----

en el transactSQL podemos añadir varios lotes a un conjunto, divididos por un GO. Aunque estos no funcionan como las transacciones por si solos, si una instruccion falla el lote sigue corriendo, si queremos que actúe como transaccion tenemos que encerrar los lotes entre `BEGIN` Y `END`.

tambien se pueden declarar variables, generalmente al inicio porque son variables que usaremos duarante la ejecucion. La instruccion para usarlas es `DECLARE @variable TIPO= VALOR`

tipos de datos
- int 
- nvarchar(maneja caracteres unicode, para evitar fallos devido a escrituras con caracteres raros)
    - ejemplo de declaracion: `SET @nom N'Juan'`
    - ejemplo uso: 
        - `SELECT @nom=nombre FROM ...`
        - `SELECT @nom AS nombre...`  <!--devuelve los valores de la variable -->
        
estructuras
- IF ... IS NULL
- ELSE
- SET @nivel=
    - CASE WHEN ..... THEN 'valor'
    -      WHEN ..... THEN
    -      ELSE...
    - END;
 

