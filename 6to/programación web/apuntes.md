
# Programacion web
<h2> evaluacion(5 unidades)
1. asistenica 10%
2. practicas 10%
3. tareas 10%
4. evaluacion 70%

**70% DEL FINAL**

--------------

1. estructura html 20%
2. apariencia(css) 20%
3. validacion 20%
4. acceso a datos(PHP) 20%
5. servicios web 20%

**30% del final**

##  Glosario de etiquetas
tabla:
```html
<table style="background-color: red">
    <tr>
        <td>
            perro
        </td>
        <td>
            gato
        </td>
        <td>
            perico
        </td>
    </tr>
</table>
``` 
formatos de parrafo
```html
    <p>Para parrafos largos, sangria automatica. Se ajusta a su contenedor</p>
    <pre>para mostrar texto de forma literal</pre>
    <span>parrafo sin sangria automatica, se ajusta al contenido</span>
```
div
```html
<div class="hola">
    contenedor por excelencia haahaha, agrega salto de linea por defecto
<div>
```
![span y parrafos](/ISC-ITM/6to/programación%20web/imagenes/parrafospan.png)
## introduccion
`aplicacion web:` aplicacion que para ejecutarla lo hacemos a través de un navegador web

`navegador`: entorno que brinda herramientas para correr una pagina web

`Documento HTML:`Es un archivo que cumple con ciertas caracteristicas  que permiten estructurar los contenidos que vamos a visualizar en el navegador

`web:`un servicio más de internet, al que accedemos por medio del navegador. El navegador le pide recursos al servidor

`etiqueta:`identificador de contenidos, util para estructurar el documento,darle forma. Se encierran entre los simbolos "<>", algunas son simples y otras compuestas.

La forma de identificar a las compuestas que tienen un inicio y un final, es decir que primero inician como `<body>` y cierran `</body>`

hay etiquetas que se adaptan al contenido que tienen en y otras que se adaptan al contenedor

## arquitectura de las aplicaciones web
responde  auna arquitectura de cliente-servidor, el cliente solicita(navegador) y el servidor provee
![cliente-servidor img](https://edgarbc.wordpress.com/wp-content/uploads/2014/02/501f9-cliente-servidor.png)
Componentes de la arquitectura web:
- Navegador, el cliente
- Servidor web o servidor de aplicaciones (proveedor)
- Pagina web (recursos web)(.html,.doc,.pdf,etc)
- Protocolo TCP/IP, como se van a transportar los datos por internet
- DNS: Domain Name System, libreta de direcciones. El proceso en el que transforma el nombre con el que nos referimos a una pagina en una ip real
- HTTP: protocolo transferencia de hypertexto, como se comunica el cliente y servidor `TCP/IP es como se transportan, HTTP el "lenguaje en el que se comunican"`
- Aplicacion web: una forma de acceder a los datos/recursos.
### protocolo DNS
nosotros mandamos una direccion, como www.google.com, pero esa no es una forma de acceder perse a la pagina. Cada pagina tiene una ubicacion especifica, una `IP real`. La forma de acceder a esta ip asociada es el DNS.

Las direcciones DNS son pues en realidad, direcciones IP.
![DNS](/ISC-ITM/6to/programación%20web/imagenes/WhatsApp%20Image%202025-02-10%20at%2011.47.31_5006897f.jpg)

### URN, URI Y URL
![URN-URI-URL](https://odiseageek.es/assets/2021/06/ogx43rq.png)
POR EJEMPLO: 

URL:

https://dsc.itmorelia.edu.mx/web/documentos/asignaturas
![url](/ISC-ITM/6to/programación%20web/imagenes/image.png)

URI: 

https://dsc.itmorelia.edu.mx/web/documentos/asignaturas/AE055ProgramacionWeb.pdf
![uri](/ISC-ITM/6to/programación%20web/imagenes/image2.png)

### Lenguajes 
#### Del lado del cliente
HTML, CSS Y JAVASCRIPT
#### LADO DEL SERVIDOR
PHP, ruby, java, pyhton, etc.

## unidad 2

### selectores
es el identificador del elemento que queremos modificar del hmtl en css, por ejemplo *, .root, .Principal,etc.
```css
*{
           font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        label{
            display: grid;
        }
        .Principal{
            top: 15%;
            left: 30%;
            width: 30rem;
            height: 80%;
            position: absolute;
            margin: 0 auto;
            background-color: #fffaf0;
            /* left: 5%; */
            border-radius: 5px;
        }
        .Principal h1{
            color: #360A9B;
        }
        .botones{
            position: absolute;
            margin: 0 auto;
            left:35%;
        }
        body{
            background: #360A9B;
            display: flex;
            justify-content: center;
            align-items: center;
        }
```
### modelo de caja
#### modelo de caja tradicional


## unidad 3: LENGUAJES DEL LADO DEL CLIENTE
recordando que el lenguaje del lado del cliente es javascript, y del lado del servidor puede ser php, python, perl...

HTML es la estructura de la pagina, css es el diseño y javascript de las funcionalidades
### introduccion a javascript
es un lenguaje de programacion capaz de manipular los ele,emtps HTML y sus propiedades CSS de manera dinamica, es decir, construye etiquetas y reglas de estilo dependiendo de la informacion que el usuario proporciona. Al igual que java, no necesita compilacion, si no que usa un INTERPRETE; en java se utiliza una maquina virtual, el javascript se utiliza el **NAVEGADOR**

### atributos asociados al mouse
- onclick: responde al evento
- onmousedown: responde al evento
- onmouseup: responde al evento
- onmouseenter: responde al evento
- onmouseleave: responde al evento
- onmouseover: responde al evento
- onmouseout: responde al evento
- onmousemove: responde al evento
- onwheel: responde al evento
### atributos asociados al teclado:
- onkeypress:responde al evento keypress, al presionar una tecla
- onkeydown:responde al evento kewydown
- onkeyup:responde al evento cuando se activa un elemento y se libera una tecla
- onload:responde al evento
- onunload:responde al evento

