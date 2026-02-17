import java.util.Scanner;
public class problemas2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        double precio= sc.nextDouble();
        double descuento=sc.nextDouble();
        System.out.println("el precio total es: "+precio_total(precio,descuento));
        sc.close();

        String mayor=(precio==0)?"cero":(precio<0)?"negativo":"positivo";
        System.out.println(mayor);
    }
    public static double  iva(double precio){
        double iva = 1.16;
        return precio*iva;
    }
    public static double descuento(double porcentaje, double cantidad){
        return cantidad*(porcentaje/100);
    }
    public static double precio_total(double precio, double descuento){
        return (iva(precio)-descuento(descuento,precio));
    }


}
