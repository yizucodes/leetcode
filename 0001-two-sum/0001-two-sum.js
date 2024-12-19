/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if (nums.length == 2 && nums[0] + nums[1] === target) {
        return [0, 1]
    }

    const numsMap = {}
    
    for(let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]
        if (complement in numsMap) {
            return [i, numsMap[complement]]
        }

        numsMap[nums[i]] = i
    }

    // create a numMap with the num: index
    // check if the number in array is complement of any number in map

    return []
};