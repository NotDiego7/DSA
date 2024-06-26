// arr int & func map
// return array with transformation applied to arr[i]
// returnedArray[i] = fn(arr[i], i)

// por elemento en matriz {
//     efectuar fn en el elemento dado
// }

const matriz = [1, 2, 3]
const fn = (element, i) => {
    return element + i;
}

function main () {
    const matrizDeRegreso = []
    for (let i = 0; i < matriz.length; i++) {
        const elementoTransformado = fn(matriz[i], i)
        matrizDeRegreso.push(elementoTransformado)
    }
    return matrizDeRegreso
}

// Time Complexity = O(n) | n is each iteration in our for-loop, every other operation within the iteration is constant
// Space Complexity = O(n) | n is each element we, post-transforming, push into returnedArray, everything else is constant


console.log(main())