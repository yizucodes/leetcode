class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a set and check if there are the same keys and values

        setS = {}

        for char in s:
            if char not in setS:
                setS[char] = 1  # Initialize to 1 because it's the first occurrence
            else:
                setS[char] += 1  # Increment by 1 for subsequent occurrences
        
        setT = {}

        for char in t:
            if char not in setT:
                setT[char] = 1  # Initialize to 1 for the first occurrence
            else:
                setT[char] += 1  # Increment by 1 for subsequent occurrences

        return setT == setS  # Compare the two dictionaries
