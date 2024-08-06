from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # If there's only one person and no trust relationships, they are the judge.
        if n == 1 and not trust:
            return 1
        
        # Create a list to keep track of trust counts.
        # trust_count[i] will be positive if person i is trusted, negative if they trust someone.
        trust_count = [0] * (n + 1)
        
        # Calculate trust counts.
        for a, b in trust:
            trust_count[a] -= 1  # Person a trusts someone, decrement.
            trust_count[b] += 1  # Person b is trusted by someone, increment.
        
        # The judge should be trusted by n-1 people and trust no one.
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        
        return -1  # Return -1 if no judge is found.
