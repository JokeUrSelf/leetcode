// https://leetcode.com/problems/remove-element/

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let i = 0
    let j = 0
    while (i+j<nums.length) {
        if (nums[i+j]!=val) {
            nums[i] = nums[i+j]
            i++
        }
        else
            j++
    }
    return nums.length - j
};
