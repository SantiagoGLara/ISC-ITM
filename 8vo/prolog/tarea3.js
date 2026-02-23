//funciones lamda
//funcion lambda para cuadrado

cuadrado=(x)=>x*x;
console.log(cuadrado(3));

// 2.Crear una función lambda que reciba dos números y devuelva el mayor
mayor=(a,b)=>(a>b)?a:b;
console.log(mayor(1,2));

// 3.Crear una función lambda que reciba un numero y devuelva true si es par y false si no lo es
paridad=(n)=>(n%2==1)?false:true;
console.log(paridad(3));