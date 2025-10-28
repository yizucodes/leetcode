/**
 * @param {number[]} nums
 * @return {boolean}
 */
 


var containsDuplicate = function(nums) {
    // map to store number : freq
    const freqMap = {}

    for (let num of nums) {
        if (!freqMap[num]) {
            freqMap[num] = 1
        }
        else {
            return true
        }
    }
    return false  
};