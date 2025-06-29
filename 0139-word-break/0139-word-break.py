class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
            # Start at position 0, work forward
            # At each position, try all dictionary words
            # Check if word matches at CURRENT position
            # If match found AND rest can be broken, success!
        memo = [-1] * len(s)

        def dp(i):
            # base case

            # finish match
            if i == len(s):
                return True
            
            # check if memo value
            if memo[i] != -1:
                return memo[i]
            
            for word in wordDict:
                if s[ i : i + len(word)] == word:
                    if dp(i + len(word)):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False

        return dp(0)

                
                






