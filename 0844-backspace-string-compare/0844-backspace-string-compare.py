class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            result = []
            numDelete = 0
            for i in range(len(string) - 1, -1, -1):
                if string[i] == '#':
                    numDelete += 1
                elif numDelete > 0:
                    numDelete -= 1
                else:
                    result.append(string[i])
            return ''.join(reversed(result))

        finalS = process(s)
        finalT = process(t)

        print("finalS:", finalS)
        print("finalT:", finalT)

        return finalS == finalT
