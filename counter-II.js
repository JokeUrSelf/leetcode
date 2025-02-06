// https://leetcode.com/problems/counter-ii/

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let n = init;
    return {
        increment : () => ++n,
        decrement : () => --n,
        reset : () => (n = init)
    };
};
