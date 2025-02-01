// https://leetcode.com/problems/valid-parentheses/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const pair = { '}': '{', ']': '[', ')': '(' };
    const d = [];
    for (const i of s) {
        if (pair[i]) {
            if (d.pop() !== pair[i])
                return false;
        } else {
            d.push(i);
        }
    }
    return d.length === 0;
}
