// https://leetcode.com/problems/container-with-most-water/

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    let max = 0
    let i = 0;
    let j = height.length - 1;
    while (i < j) {
        const s =
            Math.min(height[i], height[j]) * (j - i);
        max = Math.max(max, s);

        if (height[j] < height[i]) j--;
        else i++;
    }
    return max;
};
