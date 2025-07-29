/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const t = [];
    for (let c = 0; c < arr.length; c++) {
        t.push(fn(arr[c], c));
    }
    return t;
};