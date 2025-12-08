from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # one letter -> return s
        if len(s) == 1:
            return s

        # Counter for letters in s sorted from high to low
        freqList = Counter(s).most_common()

        charList = []
        # create list of chars where char * frequency 
        for char, freq in freqList:
            chars = char * freq
            charList.append(chars)
            
        # return charList as string

        return ''.join(charList)

