from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a map with letter and frequency for s 
        freqMap = Counter(s)
        
        # iterate through this map for t
        for char in t:

        # if letter is not in there or letter frequency is 0
        # return False
            if char not in freqMap or freqMap[char] == 0:
                return False
        
        # decrease frequency as letter exists
            freqMap[char] -= 1

        # Return as it means that all the letters have freq 0
        # If there is any letter with a freq > 0 return False
        for _, freq in freqMap.items():
            if freq > 0:
                return False
        return True
        