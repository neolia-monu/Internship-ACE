class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if len(stack) == 0 and (i == ')' or i == '}' or i == ']'):
                return False
            
            if i == '(' or i == '{' or i == '[': 
                stack.append(i)
                continue

            el = stack.pop()
            if (el == '(' and i != ')') or (el == '{' and i != '}')  or (el == '[' and i != ']'):
                return False

            
        return len(stack) == 0 
