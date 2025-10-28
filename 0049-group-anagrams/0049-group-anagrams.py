from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        canMap = defaultdict(list)
        
        for word in strs:
            # sort word alphabetically
            canonical = ''.join(sorted(word)) # "eat" -> "aet"
            canMap[canonical].append(word)

        return list(canMap.values())
