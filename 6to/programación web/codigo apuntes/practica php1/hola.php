<h1>
    <?php
    if(isset($_GET['nombre'])&&isset($_GET['origen']))
        echo "Hola".$_GET['nombre']." eres de ".$_GET['origen'];
    elseif(isset($_GET['nombre']))
        echo "Hola".$_GET['nombre']." NO SE DE DONDE ERES";
    else 
        echo "hola no se tu nombre";
    ?>
</h1>
<!-- podemos hacer otra version, que si no existe uno asigne otro -->
<h1>
    <?php
    $cadena=$_GET['nombre']??"no se tu nombre";
    echo "Hola ".$cadena;
    ?>
</h1>
<h1>
    <?php
    echo "Hola ".($_GET['nombre ']??"no se tu nombre");
    ?>
</h1>
<!-- con operador ternario -->

<!-- uso de funciones -->


<!-- uso de funciones, paso por referencia -->
 <h1>
    <?php
    function imprime(&$nombre){
        echo "hola ".$nombre."<br>";
        $nombre='María'
        imprime
    }

</h1>