// https://leetcode.com/problems/array-prototype-last/

Array.prototype.last = function() {
    if (this.length){
        return this.at(-1);
    }
    return -1;
};
