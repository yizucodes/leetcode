class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        def customSort(item):
            word, freq = item 
            return (-freq, word)  # frequency descending, then alphabetical ascending

        if len(words) == 1:
            return words
        
        # Counter word: freq
        wordMap = Counter(words)

        # Get k most common ones based on frequency
        mostCommon = sorted(wordMap.items(), key = customSort)

        # if same frequency?

        # Return the ones 
        return [el for el, freq in mostCommon[:k]]
        



