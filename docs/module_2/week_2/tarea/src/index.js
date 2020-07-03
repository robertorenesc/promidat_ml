// let plain = [[5,4],[7, 6],[1, 3]]

// function calculateAverage(plain) {
//     return plain.map(p => {
//         console.log(Math.pow(p[0], 2))
//         return Math.pow(p[0], 2) + Math.pow(p[1], 2)
//     }).reduce((a, b) => a + b) / plain.length
// }

// console.log(calculateAverage(plain))

// let word = "11000122"

// function esCasiPalindromo(word) {
//     var normal = word.split("")
//     var reverse = word.split("").reverse()
//     var diff = 0
//     for(var i = 0; i < normal.length; i++) {
//         diff += normal[0] === reverse[0] ? 0 : 1
//     }
//     return diff <= 2
// }

// console.log(esCasiPalindromo(word))


// function masPopular(collection, size) {
//     return collection.sort((a,b) =>
//         collection.filter(x => x === a).length - collection.filter(y => y === b).length
//     ).pop();
// }

// console.log(masPopular([4, 7, 7, 1, 1, 7]))