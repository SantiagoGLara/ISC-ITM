//duplicar los elementos de una lista de almenos 4 elementos
let nums=[2,4,6,8]

console.log("numeros: "+nums)
console.log("dobles: "+nums.map(x=>x*2))

//convertir de pesos a dolares los elementos de la lista
let pesos=[100,250,400,1000]
console.log("\npesos: "+pesos)
console.log("conversion a dolar: "+pesos.map(x=>x/17.19))

//agregar iva a precios de lista

let precios=[10,55,80,30,100]
console.log("precios: "+precios)
console.log("precio+IVA: "+precios.map(x=>x*1.16))

// duplicar solo numeros mayores a 10
let mayores=[5,12,3,20,8,90,68,5,2]
console.log("numeros: "+mayores)
console.log(">10: "+mayores.filter(x=>x>=10).map(x=>x*2))

//De la siguiente lista, obtener el valor absoluto [-5,3,-2,10]
let abs= [-5,3,-2,10]
console.log("lista: "+abs)
console.log("valores absolutos: "+abs.map(x=>Math.abs(x)))