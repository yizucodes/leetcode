class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            currentIndex = i
            while stack and temperatures[currentIndex] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = currentIndex - index
            stack.append(currentIndex)

        return res