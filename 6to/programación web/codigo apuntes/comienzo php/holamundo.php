<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <pre>
    <?php
    $miArreglo=array(1,2,3.141516,'hola','x');
    var_dump($miArreglo);#debo dinero a gente mala
    print_r($miArreglo);
        $var = "Hola mundo";
        $var = "Andrés";
    const PI=3.1415927;
    define('CERO',0);
    $diametro=16;
    if($diametro>CERO)
    echo "El area es:  ".PI*$diametro*$diametro/4;
    ?>
    </pre>
    <h1> 
    <?php
    if(isset($_GET['nombre']))
        echo "Hola ".$_GET['nombre']."  bienvenido" ;
    else
        echo "No se tu nombre"
    
    ?>
    </h1>

</body>
</html>