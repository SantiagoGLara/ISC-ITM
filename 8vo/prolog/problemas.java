// 1.Una función que recibe un número entero y devuelve su doble.
// 2.Una función que recibe dos números enteros y devuelve el mayor.
// 3.Una función que recibe un número entero y devuelve True si es par.
// 4.Una función que recibe una calificación y devuelve una cadena con el resultado (“aprobado” o “reprobado”).
import java.util.Scanner;
public class problemas{
    public static void main(String[] args) {
        //programacion imperativa
        //ejercicio 1
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero entero: ");
        int num1 = sc.nextInt();
        int doble = num1 * 2;
        System.out.println("El doble de " + num1 + " es: " + doble);
        //ejercicio 2
        System.out.println("Ingrese el primer numero entero: ");
        int num2 = sc.nextInt();
        System.out.println("Ingrese el segundo numero entero: ");
        int num3 = sc.nextInt();
        if(num2 > num3){
            System.out.println("El mayor de " + num2 + " y " + num3 + " es: " + num2);
        } else {
            System.out.println("El mayor de " + num2 + " y " + num3 + " es: " + num3);
        }
        //ejercicio 3
        System.out.println("Ingrese un numero entero: ");
        int num4 = sc.nextInt();
        if(num4 % 2 == 0){
            System.out.println(num4 + " es un numero par.");
        } else {
            System.out.println(num4 + " es un numero impar.");
        }
        //ejercicio 4
        System.out.println("Ingrese una calificacion: ");
        int calificacion = sc.nextInt();
        if(calificacion >= 70){
            System.out.println("Aprobado");
        } else {
            System.out.println("Reprobado");
        }
        //programacion funcional
        //ejercicio 1
        System.out.println("Ingrese un numero entero: ");
        System.out.println("el doble es:"+doble(sc.nextInt()));
        //ejercicio 2
        System.out.println("ingrese el primer numero");
        int n1=sc.nextInt();
        System.out.println("ingrese el segundo numero");
        int n2=sc.nextInt();
        System.out.println("el numero mayor es:"+mayor(n1, n2));
        //ejercicio 3
        System.out.println("ingrese un numero");
        System.out.println(paridad(sc.nextInt()));
        //ejercicio 4
        System.out.println("ingrese calificacion");
        System.out.println("ustes ha:"+Calificar(sc.nextInt()));
        sc.close();
    }
    public static String Calificar(int cal){
        return(cal>70)?"Aprobado":"Reprobado";
    };
    public static boolean paridad(int n){
        return (n%2==1)?false:true;
    };
    public static int mayor(int n1,int n2){
        return (n1>n2)?n1:n2;
    };
    public static int doble(int num){
        return num * 2;
    }
    
}

