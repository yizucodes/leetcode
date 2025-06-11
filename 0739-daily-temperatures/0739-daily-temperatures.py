class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: # why mono decreasing stack
                wait_i = stack.pop()
                res[wait_i] = i - wait_i
            stack.append(i)

        return res
        