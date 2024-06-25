// // Write a class that allows setting and getting key-value pairs
// // Each key is associated with a time until expiration
// // Class has 3 methods:
// // set(key, value, duration)
// // get(key)
// // count()

// var TimeLimitedCache = function () {
//     class TimeLimitedCache {

//         constructor() {
//             this.obj = {};
//             this.objetoDeIdentificadores = {};
//         }

//         establecer(key, value, duration) {
//             if (typeof key === "number" && typeof value === "number" && typeof duration === "number") {
//                 if (this.obj[key]) {
//                     clearTimeout(this.objetoDeIdentificadores[key]);
//                     this.obj[key] = value;
//                     timeoutId = setTimeout(() => { delete this.obj[key] }, duration);
//                     this.objetoDeIdentificadores[key] = timeoutId
//                     return true;
//                 }
//                 this.obj[key] = value;
//                 timeoutId = setTimeout(() => { delete this.obj[key] }, duration);
//                 this.objetoDeIdentificadores[key] = timeoutId
//                 return false;
//             }
//         }

//         get(key) {
//             if (this.obj[key]) {
//                 return this.obj[key];
//             } else {
//                 return -1;
//             }
//         }

//         count() {
//             return Object.keys(this.obj).length;
//         }
//     }
//     return TimeLimitedCache;
// };

// /** 
//  * @param {number} key
//  * @param {number} value
//  * @param {number} duration time until expiration in ms
//  * @return {boolean} if un-expired key already existed
//  */
// TimeLimitedCache.prototype.set = function (key, value, duration) {

// };

// /** 
//  * @param {number} key
//  * @return {number} value associated with key
//  */
// TimeLimitedCache.prototype.get = function (key) {

// };

// /** 
//  * @return {number} count of non-expired keys
//  */
// TimeLimitedCache.prototype.count = function () {

// };

// /**
//  * const timeLimitedCache = new TimeLimitedCache()
//  * timeLimitedCache.set(1, 42, 1000); // false
//  * timeLimitedCache.get(1) // 42
//  * timeLimitedCache.count() // 1
//  */













// LeetCode Format:
class TimeLimitedCache {
    constructor() {
        this.obj = {}
        this.objetoDeIdentificadores = {}
    }
}

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */

TimeLimitedCache.prototype.set = function (key, value, duration) {
    if (typeof key === "number" && typeof value === "number" && typeof duration === "number") {
        if (this.obj[key]) {
            clearTimeout(this.objetoDeIdentificadores[key])
            this.obj[key] = value
            timeoutId = setTimeout(() => { delete this.obj[key] }, duration)
            this.objetoDeIdentificadores[key] = timeoutId
            return true
        }
        this.obj[key] = value
        timeoutId = setTimeout(() => { delete this.obj[key] }, duration)
        this.objetoDeIdentificadores[key] = timeoutId
        return false
    }
}

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
    if (this.obj[key]) {
        return this.obj[key]
    } else {
        return -1
    }
}

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
    return Object.keys(this.obj).length
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */


// Time Complexity = set() & get() = O(1) | count() = O(n) -> Proportional to n keys allocated in the {}
// Space Complexity = set() & get() = O(1) | count() = O(n) -> Proportional to n keys allocated in the {}