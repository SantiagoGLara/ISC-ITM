//a partir de una lista de edades sumar 5 años a cada edad, despues obtener solo aquellos que sean mayores a 18 y obtener el doble de las edades que sean mayores a 18

let edades=[10,15,20,15].map(x=>x+5).filter(x=>x>=18).map(x=>x*2)

console.log(edades)