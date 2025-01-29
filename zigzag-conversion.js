// https://leetcode.com/problems/zigzag-conversion/

/**
 * @param {string} s
 * @param {number} rows
 * @return {string}
 */
var convert = function(s, rows) {
    if (rows === 1) return s

    newLetters = ""

    for (let row = 0; row < rows; row++) {
        for (let i = row, j = 0; s[i]; j++) {
            let idx = j % 2 ? row : rows - 1 - row
            if (idx === 0) continue

            newLetters += s[i]
            i += 2*idx
        }
    }

    return newLetters
};
