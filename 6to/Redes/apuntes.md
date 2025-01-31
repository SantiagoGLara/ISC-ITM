# Redes

## recapitulación:

### módulo 5:
ipv4 son direcciones de 32 bits(4 octetos), se muestran en binario pero regularmente las vemos en decimal como por ejemplo 192.168.10.10 (poner valor en binario), mientras que las ipv6 son de 128 bits, representadas en hexadecimal.

direcciones ipv4 y binarios

para que un router pueda comunicar 2 dispositivos/redes deben de ser diferentes

![redes](/6to/Redes/imagenes/img1.png)
Como en ese ejemplo, el router comunica a 2 redes con distintas ip, en este caso con el tercer octeto diferente
![redes1](/6to/Redes/imagenes/img2.png)
o en este, que comunica a 3 redes con una diferencia antes del ::64

ipv6 se maneja en hextetos(16) de bits, representados en hexadecimal

### módulo 6

#### capa de transporte (capa 4)
Se encarga de segmentar la información, por medio de 2 posibles protocolos: udp(cada segmento se le llama datagrama) y tcp(? (a cada parte se le llama segmento).

**protocolo TCP**  
El protocolo de control de transporte, orientado a la transmisión, consta de 3 partes. Puede haber retransmisiones, por si llega mal al destino, lo que hace que sea confiable hasta este protocolo. Les otorga un número de secuencia, lo que permite que aunque cada segmento se llegase a mandar en desorden, en el destino se reordena (igual en capa 4). También si llega dañado un segmento, se solicita que se reenvíe únicamente el necesario.

**protocolo udp**

#### capa de red (capa 3)
Única capa en la que se le llaman paquetes a la información, los routers trabajan con IP’s, se encarga de asignarle al paquete la ip a la que se destina y de la cual viene.

#### capa de enlace de datos (capa 2)
Su propósito es enlazar las direcciones MAC, que son direcciones únicas de una tarjeta de red, así sean del mismo modelo la dirección es única. La información en esta capa (CAPA 2) son llamados TRAMA. Esta capa es la responsable de comunicar entre tarjetas de interfaz de red (NIC).  
Permite que tramas superiores accedan a los medios  
Acepta los datos de la capa 3(ipv4 o 6) y los encapsula en tramas  
Controla cómo se intercambian, colocan y reciben.  
Recibe datos  
Realiza detección de errores y rechaza tramas dañadas  

Si por alguna razón no conoce la MAC adress de destino, con el protocolo ADP, donde el router le pregunta a todos los dispositivos quien es con el que se quiere comunicar, que se identifique con su MAC adress.

Esta capa prepara los datos de red para la red física, necesita saber cómo está conectada la capa física desde antes de prepararlos
##### Provisión de acceso a los medios
Cada entorno de red que los paquetes encuentran cuando viajan desde un host local hasta un host remoto puede tener características diferentes. Por ejemplo, una LAN Ethernet generalmente consta de muchos hosts que compiten por el acceso en el medio de red. La subcapa MAC resuelve esto. Con los enlaces serie, el método de acceso sólo puede consistir en una conexión directa entre solo dos dispositivos, generalmente dos routers. Por lo tanto, no requieren las técnicas empleadas por la subcapa MAC IEEE 802.

Las interfaces del router encapsulan el paquete en la trama apropiada. Se utiliza un método adecuado de control de acceso a los medios para acceder a cada enlace. En cualquier intercambio de paquetes de capas de red, puede haber muchas transiciones de medios y capa de enlace de datos.

En cada salto a lo largo de la ruta, un router realiza las siguientes funciones de Capa 2:

1. Aceptan una trama proveniente de un medio.
2. Desencapsulan la trama.
3. Vuelven a encapsular el paquete en una trama nueva.
4. Reenvían la nueva trama adecuada al medio de ese segmento de la red física.

# completar hasta el 6.2
#### topologias
topologia fisica: identifica las conexiones fisicas que interconectan n cantidad de dispositivos.<br>
<br>
topologia logica: tambien conocido como direccionamiento logico, es la forma en la que una red transfiere tramas al nodo siguiente, identifica las conexiones virtuales mediante interfaces de dispositivo mediante esquemas de direccionamiento IP de capa 3.<br>

##### topologias WAN
forma de conectar multiples conexiones LAN, una o muchas redes locales. Por ejemplo, toda la instalacion del tecnologico de morelia es una red local, toda la forma en la que se distribuyen sus redes es local, y si quisiera establecer 

offtopic(?): las VPN[Virtual Private Network] nos aseguran las redes e info encriptando, es como un tunel entre redes a traves de la nube, aunque alguien capture en medio del viaje, no sabe que dice. De esta forma se puede conectar de forma segura 2 LAN(UNA WAN) "sin necesidad de un provedor"(suponiendo que fuere viable hacer la instalacion en largas distancia)

existen varias formas de hacer estas conexiones:
- punto a punto: dos dispositivos directamente![malla](/6to/Redes/imagenes/PTP.png)
- estrella: muchos dispositivos interconectados por medio de uno central![estrella](/6to/Redes/imagenes/ESTRELLA.png)
- malla: todos conectados con todos, la mas optima pero mas costosa ![malla](/6to/Redes/imagenes/MALLA.png)

##### topologias LAN

##### Comunicacion FullDuplex y HalfDuplex
###### verificar que nuestra tarjeta de red no esté en halfDuplex, productor de posible lentitud
para hacer eso, tenemos que seguir la siguiente ruta:
![ruta](/6to/Redes/imagenes/ruta.png)
y en las opciones de la izquierda


en este caso, hay que procurar que la tarjeta siempre este configurada siempre en autonegociacion, pues si está fija en uno aunque sea full duplex, haria incompatible la comunicacion
#### metodos de control de acceso
##### acceso basado en la contencion
en estas redes todos los dispositivos/nodos operan en semiduplex, compitiendo por quien usa el medio. solo hay un proceso si mas de un dispositivo tranmite al mismo tiepo

##### acceso controlado

#### acceso por contencion

HUB: miniswitch, que en realidad es el switch antiguo. Es un repetidor de bits, es decir que lo que entraba por uno de sus lados se reenviaba a todos los demás, por eso en el se usaban los metodos de control donde solo uno mandaba. Con este se hacian las redes antiguas

### trama de enlace de datos

**COMPLETAR**
existen puertos de origen (desde el 1024, que antes de eso la pc los destina a otra cosa) y de destino (como los sitios web, que si es http es 80 o https 443)