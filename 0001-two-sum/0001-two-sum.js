/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numMap = {}

    for (let i = 0; i < nums.length; i++) {
        const comp = target - nums[i]
    
        // number exists
        if (nums[i] in numMap) {
            return [i, numMap[nums[i]]]
        } 
        // add to map comp : i
        else {
            numMap[comp] = i
        }
    }
    return []
    
};