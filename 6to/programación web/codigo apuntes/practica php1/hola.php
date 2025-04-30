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



<!-- funciones y variables globales -->
<h1>
    <?php
        $varGlobal="mundo cruel";
        function hola(){
            global $varGlobal; //a pesar que la variable ya existe en un contexto mayor, 
                                //si le ponemos global respeta el valor que tiene afuera, a pesar que 
                                //en teoria solo existe en este entorno
            echo "Hola".$varGlobal;
        }
        hola();
    ?>
</h1>

<!-- funciones anonimas -->
<h1>
    <?php
    $area=function($radio){
        $pi=3.1415927;
        return $pi* $radio*$radio;
    };
    echo "Area de la circunferencia(radio=3.2): ".$area(3.2);
    
    ?>
</h1>
<!-- estructuras de control -->

<h1>
    <?php
    function mayor($a,$b){
        if($a>$b)
            echo "a is greather than b";
        else
            echo "a is NOT greather than b";
    }
    mayor(5,6);
    ?>

    <!-- opcion B -->
     

    <!-- opcion C -->
</h1>

<!-- switch -->


<!-- while -->
 <h1>
    <?php
    $i=1;
    while($i<10){
        echo " ,",$i;
        $i++;
    }
    ?>
</h1>
<!-- for -->
 

<!-- foreach -->
 <h1>
    <?php
    echo "<br> for normal: ";
    $miArreglo=array(9,8,7,6,5,4,3,2,1);
    for($i=0;$i<count($miArreglo);$i++)
        echo $i."=".$miArreglo[$i],", ";

    echo "<br> foreach: "; 
    foreach($miArreglo as $i=>$elemento)
        echo $i."=".$elemento.", ";
    ?>
</h1>

<!-- include y require -->
 