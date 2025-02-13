// https://leetcode.com/problems/generate-fibonacci-sequence/

/**
 * @return {Generator<number>}
 */
var fibGenerator = function*(a=0,b=1) {
    yield a;
    yield* fibGenerator(b, a+b);
};
