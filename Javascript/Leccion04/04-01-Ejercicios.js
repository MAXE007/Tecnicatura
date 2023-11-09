//Ejercicio 1:Calcular estacion del año
let mes = 7;
let estacion; //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estación de: "+estacion);


//Ejercicio 2: Hora del dia
let horaDia = 19;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good Morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good Afternoon";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good Evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good night";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje)

//Estructura switch(La sintaxis es igual a Java)
switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estacion de: "+estacion);

//Evita repetir tu codigo
//Dry don't repeat yourself
let days = 1;

switch (days) {
    case 1:
        console.log('hoy es lunes')
        break;
    case 2:
        console.log('hoy es martes')
        break;
    case 3:
        console.log('hoy es miercoles')
        break;
    case 4:
        console.log('hoy es jueves')
        break;
    case 5:
        console.log('hoy es viernes')
        break;
    case 6:
        console.log('hoy es sabado')
        break;
    case 7:
        console.log('hoy es domingo')
        break;   

    default:
        console.log("Error en el ingreso del dia de la semana");
        break;
}
//esta es la opcion mejorada

let days2 = ['Lunes','Mares','Viernes','Sabado','Domingo'];

function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(5));

let month = 11;
switch (month) {
    case 1:
        console.log("Es Enero")
        break;
    case 2:
        console.log("Es Febrero")
         break;
    case 3:
        console.log("Es Marzo")
        break;
    case 4:
        console.log("Es Abril")
        break;
    case 5:
        console.log("Es Mayo")
        break;
    case 6:
        console.log("Es Junio")
        break;
    case 7:
        console.log("Es Julio")
        break;
    case 8:
        console.log("Es Agosto")
        break;
    case 9:
        console.log("Es Septiembre")
        break;
    case 10:
        console.log("Es Octubre")
        break;
    case 11:
        console.log("Es Noviembre")
        break;
    case 12:
        console.log("Es Diciembre")
        break;
    default:
        break;
}

//Esta es la opcion mejorada

let month2 = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciemrbe'];
function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error('Out of range');
    }
    return month2[n-1];
}
console.log(getMonth(1));