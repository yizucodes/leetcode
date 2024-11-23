class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split string to have array of words
        wordList = s.split()

        lastWord = wordList[-1]

        return len(lastWord)