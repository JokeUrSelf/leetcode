// https://leetcode.com/problems/sleep/

/**
 * @param {number} millis
 */
async function sleep(millis) {
    await new Promise(resolve => setTimeout(resolve, millis));
}
