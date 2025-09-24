from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        canMap = defaultdict(list)

        # canonical key, ensure to sort by alphabetical order
        # "a1e1t1" or (('a',1), ('e',1), ('t',1))
        
        for word in strs:
            # sort word alphabetically
            canonical = ''.join(sorted(word)) # "eat" -> "aet"
            canMap[canonical].append(word)

        return list(canMap.values())
