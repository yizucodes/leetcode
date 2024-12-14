from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # if one num return true
        if len(arr) == 1:
            return True

        # make num : freq map
        freqMap = Counter(arr)

        # check if list of freq has unique values --> return False if it does not
        freqValues = list(freqMap.values())

        if len(freqValues) != len(set(freqValues)):
            return False

        return True
        