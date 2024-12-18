/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {

    // check for empty
    if (!arr) {
        return false
    }

    // check for length 1
    if (arr.length == 1) {
        return true
    }

    // create a map { num: freq }
    const numMap = {}
    
    for (let i = 0; i < arr.length; i++){
        // if num in numMap, increment freq
        if (arr[i] in numMap) {
            numMap[arr[i]]++;
        }
        // other wise num: 1
        else {
            numMap[arr[i]] = 1
        }      
    }

    // check if list of freq length != length of set of freq length contains duplicate --> return false
    listFreq = Object.values(numMap)
    setFreq = new Set(listFreq)

    if (listFreq.length != setFreq.size) {
        return false
    }
    
    return true
};