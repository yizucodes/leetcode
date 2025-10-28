/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {

    // two empty strings considered anagram
    if(!s && !t) {
        return true
    }

    // diff length return false
    if(s.length != t.length) {
        return false
    }

    // sMap, tMap
    sMap = {}
    tMap = {}
    // letter: freq

    // iterate s string
    for (let letter of s) {
        // no letter
        if (!sMap[letter]) {
            sMap[letter] = 1
        } 
        // increment freq by 1
        else {
            sMap[letter]++;
        }
    }

    // iterate t string
    for (let letter of t) {
        // no letter
        if (!tMap[letter]) {
            tMap[letter] = 1
        } 
        // increment freq by 1
        else {
            tMap[letter]++;
        }
    }

    for (let key in sMap) {
        if (sMap[key] !== tMap[key]) {
            return false;
        }
    }
    return true;
};