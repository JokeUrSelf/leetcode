// https://leetcode.com/problems/promise-time-limit/

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {
    return (...args) => {
        return new Promise((resolve, reject) => {
            setTimeout(() => reject("Time Limit Exceeded"), t)
            fn(...args).then(result => resolve(result)).catch(error => reject(error));
        });
    };
}

