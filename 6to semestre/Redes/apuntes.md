# Redes - Recapitulación

## Módulo 5

### Direcciones IPv4
Las direcciones IPv4 son de **32 bits** (4 octetos). Aunque estas direcciones se representan en **binario**, comúnmente las vemos en **decimal**. Un ejemplo de dirección IPv4 es `192.168.10.10` (esta dirección tiene un valor en binario que se podría calcular).

### Direcciones IPv6
Por otro lado, las direcciones IPv6 son de **128 bits** y se representan en **hexadecimal**. Estas direcciones se manejan en **hextetos** (16 bits por hexteto), lo que permite una representación más compacta y eficiente.

### Comunicación entre Redes
Para que un router pueda comunicar dos dispositivos o redes, estas deben ser diferentes. Un ejemplo sería un router que comunica dos redes con direcciones IP diferentes, como cuando el tercer octeto de la dirección cambia.

En el caso de IPv6, un router puede comunicar tres redes con diferencias antes del `::64`, mostrando cómo se manejan las redes con distintas configuraciones de direcciones.

---

## Módulo 6

### Capa de Transporte (Capa 4)
La **Capa de Transporte** se encarga de segmentar la información para su transmisión. Los protocolos que operan en esta capa son el **UDP** y el **TCP**. En UDP, cada segmento se llama **datagrama**, mientras que en TCP, cada segmento se llama **segmento**.

#### Protocolo TCP
El **Protocolo TCP** es un protocolo de control de transporte orientado a la transmisión. Este protocolo consta de tres partes principales y se caracteriza por ser confiable, ya que puede hacer retransmisiones en caso de que los datos lleguen de manera incorrecta. Además, TCP asigna un **número de secuencia** a cada segmento, lo que permite que los segmentos, aunque lleguen desordenados, puedan ser reorganizados en el destino. Si algún segmento llega dañado, solo se solicita el reenvío del segmento necesario.

### Capa de Red (Capa 3)
La **Capa de Red** es la única capa en la que la información se denomina **paquetes**. Los **routers** son los encargados de trabajar con las direcciones IP, asignando tanto la IP de origen como la IP de destino a cada paquete de datos.

### Capa de Enlace de Datos (Capa 2)
La **Capa de Enlace de Datos** tiene como objetivo enlazar las direcciones **MAC**, que son únicas para cada tarjeta de red, independientemente de que sean del mismo modelo. La información que se maneja en esta capa se llama **trama**. 

El propósito de esta capa es facilitar la comunicación entre las tarjetas de interfaz de red (**NICs**). Además, permite que las tramas provenientes de capas superiores accedan a los medios de transmisión. La capa 2 también se encarga de la **detección de errores**, rechazando las tramas que resulten dañadas.

#### subcapas de la capa de enlace de datos
##### subacapa LLC(control de enlace logico)
se encarga de ver que tipo de protocolo de red, que generalmente es un paquete IPv4 o IPv6 y agrega informacion de control de capa 2 para ayudar a entregar el paquete al destino tenemos en la capa anterior se rige por el estandar LLC-IEEE 802.2, como quien dice ve hacia arriba
##### subcapa MAC(Subcapa de acceso de al medio)
se encarga de ver el medio de la capa fisica. para el adaptador ethernet se rige por IEE 902.3, por WLAN  IEEE 902.11 y para WPAN 802**CHECAR NETACAD TABLA**.<br>
la subcapa MAC proporciona encapsulacion de datos:
- delimitacion de tramas: el proceso de entramado proporciona delimitadores que se usan para identificar el tipo de bits que componen una trama, proporcionan sincronizacion entre los nodos de transmision y de recepcion
- direccionamiento: proporciona direccion de origen y destino para transportar la tram de la capa 2 entre dispositivos en el mismo medio compartido
- deteccion de errores
la subcapa MAC tambien otorga acceso a medios, lo que permite que varios dispositivos se comuniquen por un medio compartido(semiduplex, que solo uno puede enviar o recibir). Las comunicaciones de FullDuplex(ambos pueden enviar y recibir datos simultaneamente) no requieren control de acceso. Algo curioso que pasa es que por errores, entre equipo y equipo(de conexion a conexion) en la vida cotidiana, puede ser que la tarjeta del dispositivo o el puerto del switch se configura como halfDuplex, lo que realentiza la red y puede dar muchos problemas

#### provision de acceso a los medios (6.1.3)
hacer apunte subtema.


#### Protocolo ARP
Si el router no conoce la dirección MAC de destino, utiliza el **protocolo ARP**. A través de este protocolo, el router envía una solicitud a todos los dispositivos para que se identifiquen con su dirección MAC, permitiendo así establecer la comunicación correcta entre los dispositivos.

