class Solution:
    def evalRPN(self, tokens: List[str]) -> int:         
        stack = []
        validOps = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in validOps:
                stack.append(int(token))
            elif token in validOps:
                numTop = stack.pop()
                numBot = stack.pop()
                res = None
                print(stack)
                if token == '+':
                    res = numBot + numTop
                elif token == '-':
                    res = numBot - numTop
                elif token == '*':
                    res = numBot * numTop
                elif token == '/':
                    res = int(numBot / numTop)
                stack.append(res)     

# for each token:
#     if token is number:
#         push to stack
#     else:  # it's an operator
#         pop two numbers
#         calculate result
#         push result back
# return stack[0]
        return stack[-1]

# bottom - top