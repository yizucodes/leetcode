from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len is 1
        # return [strs]
        if len(strs) == 1:
            return [strs]
        
        keyMap = defaultdict(list)
        # unique sorted keys for strs array
        for word in strs:
            sortedKey = "".join(sorted(word))
            if sortedKey not in keyMap:
                keyMap[sortedKey] = []
        
        # add words based on the sortedKey
        for word in strs:
            sortedKey = "".join(sorted(word))
            if sortedKey in keyMap:
                keyMap[sortedKey].append(word)

        # return the values in an array by iterating through the map
        return [val for val in keyMap.values()]

