function dividir(numero1, numero2) {
    if (numero2 === 0) {
        return "No es posible dividir por cero";
    }
    return numero1 / numero2;
}
console.log("Hola desde division.js")
module.exports = dividir;
