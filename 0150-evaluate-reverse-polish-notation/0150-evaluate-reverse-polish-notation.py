class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # duplicate consecutive operators
        # one item in tokens
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operators = {'+', '-', '*', '/'}

        for i in range(len(tokens)):
            # take top operand top - 1
            char = tokens[i]
            if char not in operators:
                stack.append(int(char))
            else:
                if len(stack) >= 2:


                    top = stack.pop()
                    bot = stack.pop()

                    if char == '+':
                        stack.append(bot + top)
                    elif char == '-':
                        stack.append(bot - top)
                    elif char == '*':
                        stack.append(bot * top)
                    elif char == '/' and top != 0:
                        stack.append(int(bot / top))
                    elif char == '/' and top == 0:
                        print('division by 0 invalid')
        
        return stack[-1]

        
