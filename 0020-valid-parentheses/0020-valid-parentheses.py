class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        # stack
        st = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                st.append(char)
            elif len(st) > 0 and char == ')' and st[-1] == '(':
                st.pop() 
            elif len(st) > 0 and char == ']' and st[-1] == '[':
                st.pop()
            elif len(st) > 0 and char == '}' and st[-1] == '{':
                st.pop()
            # else:
            #     return False

        return len(st) == 0