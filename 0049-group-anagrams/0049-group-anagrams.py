class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def createDict(word):
            wordDict = {}

            for char in word:
                if char not in wordDict:
                    wordDict[char] = 1
                else:
                    wordDict[char] += 1
 
            return wordDict

        # if one string
        if len(strs) == 1:
            return [strs]

        # Dictionary to hold groups of anagrams
        anagram_map = {}

        # Create a dictionary with letter frequencies as value for each string
        for word in strs:
            word_dict = createDict(word)

            # Convert dict to tuple of sorted items for comparison
            word_tuple = tuple(sorted(word_dict.items()))

            # Group anagrams together
            if word_tuple in anagram_map:
                anagram_map[word_tuple].append(word)
            else:
                anagram_map[word_tuple] = [word]
            
        # Convert anagram_map vals into list of lists
        res = list(anagram_map.values())

        return res
        