/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    // empty or length 1
    if (s.length <= 1) {
        return s
    }

    let left = 0
    let right = s.length - 1

    while (left < right) {
        // swap the left and right
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        
        // increment left
        left++;
        // decrement right
        right--;
    }

    return s

};