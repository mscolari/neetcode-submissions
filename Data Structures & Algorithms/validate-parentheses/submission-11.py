class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_mapping = {')':'(', ']':'[', '}':'{' }

        for p in s:
            if p in bracket_mapping:
                if stack and stack[-1] == bracket_mapping[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return not stack