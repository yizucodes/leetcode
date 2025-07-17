from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Create a data structure to group words by their signature
        # Hint: Use defaultdict(list) so each signature automatically gets an empty list
        anagram_groups = defaultdict(list)
        
        # Step 2: Process each word in the input array
        for word in strs:
            
            # Step 2a: Create a signature for this word
            # Hint: Sort the characters in the word to create a unique identifier
            # Words with same characters will have same signature
            signature = ''.join(sorted(word))

            # Step 2b: Add this word to the group that matches its signature
            # Hint: Use the signature as the key in your dictionary
            anagram_groups[signature].append(word)
        
        # Step 3: Return all the groups as a list of lists
        # Hint: Convert the dictionary values to a list

        return list(anagram_groups.values())
"""
Time Complexity: O(n * k log k)
- n = number of strings in input
- k = maximum length of any string (number of letters)
- For each string: O(k log k) to sort + O(k) to join = O(k log k)
- Total: n strings × O(k log k) = O(n * k log k)

Space Complexity: O(n * k)
- Dictionary storage: O(n) entries in worst case (all unique)
- Each signature: O(k) space
- Each value list: contains original strings O(k) each
- Return list: O(n * k) total
- Total: O(n * k)
"""