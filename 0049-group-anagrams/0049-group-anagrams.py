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

# Test your implementation:
# Input: ["eat","tea","tan","ate","nat","bat"]
# Expected Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

# Trace through example:
# "eat" -> sorted = "aet" -> goes to bucket "aet"
# "tea" -> sorted = "aet" -> goes to bucket "aet" 
# "tan" -> sorted = "ant" -> goes to bucket "ant"
# "ate" -> sorted = "aet" -> goes to bucket "aet"
# "nat" -> sorted = "ant" -> goes to bucket "ant" 
# "bat" -> sorted = "abt" -> goes to bucket "abt"

# Final buckets:
# "aet": ["eat", "tea", "ate"]
# "ant": ["tan", "nat"] 
# "abt": ["bat"]