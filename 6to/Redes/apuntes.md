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
