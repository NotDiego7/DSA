/**
 * @param {number} millis
 * @return {Promise}
 */

// Given millis (positive integer) write async func that sleeps for millis and returns whatever
async function sleep(millis) {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(undefined), millis)
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

sleep(5000)