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

los switches guardan las MAC en su tabla de MAC ADRESS

ARP es un protocolo para comunicarse con MAC adress que aunque desconocida, el switch le "pregunta" al resto de los dispositivos quien tiene la ip solicitada, quien la tiene se la proporciona al switch y este facilita la comunicacion. A partir de ahi, el switch almacena la MAC adress que está conectada en el puerto del dispositivo que respondió su MAC ADRESS. Este tipo de comunicacion es por origen

-----

![red](/6to/Redes/imagenes/image.png)
aqui podemos apreciar una red, donde el cable azul es un cable de consola

**nota: como en el caso de 10.10.10.2/24, el /24 nos dice antes de empezar esos numeros los 24 bits anteriores a la dicha son los de la red, osea que son 255.255.255, es una nomenclatura para ahorrar espacio**
![red](/6to/Redes/imagenes/config%20ip.png)

podemos apreciar la DEFAULT GATEWAY es la ip que nos asigna el router a todos los dispositivos para comunicarnos con otros dispositivos ajenos a la misma red, por lo que es la que usan nuestros dispositivos para internet, en este caso (regresando a la imagen de la red) del router a la izquierda tienen la DEFAULT GATEWAY 10.10.10.1/24, que  es con la que se comunican a la red de la derecha, con DEFAULT GATEWAY 20.20.20.20.1/24

#### como comunicar la PC1 con la PC0
![pt1](/6to/Redes/imagenes/x.png)
![alt text](/6to/Redes/imagenes/image-1.png)
nos dice que en la capa 3, la pc1 lo que sabe. src(origen): la ip de la computadora que manda el ping

**nota:3 tipos de mensaje en telecom:**

**- unicast**

**- broadcast**

**- completar**
![alt text](/6to/Redes/imagenes/image-2.png)
podemos apreciar lo primero que pasa cuando se intenta hacer comunicacion entre 2 dispositivos dentro de la misma red y que nunca antes se ha hecho(el switch y la pc1 desconocen la MAC Adress de la PC0), ahi en la capa 2 como no sabe HACE EL PROTOCOLO ARP, para conocer la MAC Adress. primero hace todo el protocolo antes de tirar el ping
![alt text](/6to/Redes/imagenes/image-3.png)
aqui podemos ver que despues de ejecutar la primera parte de arp, el paquete avanzó al switch 0 y como el paquete avanzó de origen pc1 al switch, el switch ya conoce la MAC ADRESS de la pc1, pero le falta preguntar a los dispositivos que no son PC1 de quien tiene la mac address de la ip a la que la pc1 se quiere comunicar(tirar ping/simple package). Como en este caso aun no esta configurada la conexion del router a la red de la izquierda, solo tiene un dispositivo al que preguntarle, al router de la derecha
![alt text](/6to/Redes/imagenes/image-4.png)
de hecho, como se ve en esta imagen, si le preguntamos a la pc0 cuales mac adress conoce, no conoce ninguna, pues nunca se ha comunicado con el switch, por lo tanto tampoco con la pc1
![alt text](/6to/Redes/imagenes/image-5.png)
en el siguiente paso, el paquete llega al pc0

COMPLETAR

----
configurando router o para que establezca conexion, asignandole una ip al switch que tiene conectado por el puerto gigabit0/1
![alt text](/6to/Redes/imagenes/image-6.png)
![alt text](/6to/Redes/imagenes/image-7.png)
y los leds de la izquierda se prenden

![alt text](/6to/Redes/imagenes/image-8.png)
y se hace lo mismo con la interface de la derecha, que es la interface gigabitEthernet 0/1 del router
![alt text](/6to/Redes/imagenes/image-9.png)

ahora, configuramos la VirtualLan del switch desde la pc 1(aprovechando que lo conectamos por el cable de consola)
![alt text](/6to/Redes/imagenes/image-10.png)

en la siguiente imagen, previamente conectamos la computadora con el router y le configuramos password en el login y enable al switch, pero ademas nos permitira conectarnos de la pc al router sin necesidad de que se conecte directamente con cable de consola
![alt text](/6to/Redes/imagenes/image-11.png)
ahora, con el cable desconectado y siguiendo la ruta (en la pc) de desktop>SSH/TELNET>TELNET y en telnet escribimos la ip a la que nos queremos comunicar, en este caso 10.10.10.1, que nos dirigue al router.
![alt text](/6to/Redes/imagenes/image-12.png)
y apreciamos, que nos dejo acceder al router desde la pc0 sin necesidad de tener conectado un cable consola
![alt text](/6to/Redes/imagenes/image-13.png)

-----

el router aprende IP's en la tabla de routeo, cuando se le asigna una ip a alguna de sus interfaces y encendemos la intefaz las almacena en dichas tablas. Si apagamos la interfaz, el router deja de conocer dicha ip