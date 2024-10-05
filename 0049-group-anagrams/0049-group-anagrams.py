from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # One string
        if len(strs) <= 1:
            return [strs]
        
        wordMap = defaultdict(list)

        for word in strs:
            # Init 26 zeros list for letters
            charList = [0] * 26
            # Find corresponding index of letter of each word in strs
            for char in word:
                index = ord(char) - ord('a')
                charList[index] += 1
            charListKey = tuple(charList)
            wordMap[charListKey].append(word)

        result = list(wordMap.values())
        return result

    