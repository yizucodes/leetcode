class Solution:
    def isValid(self, s: str) -> bool:
        # if len is 1
        if len(s) == 1:
            return False

        stack = []

        # for each char in s
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) > 0:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            # empty but have a closing char
            else:
                return False

        return len(stack) == 0





