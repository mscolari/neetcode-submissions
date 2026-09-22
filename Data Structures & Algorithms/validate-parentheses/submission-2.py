class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # push if open parentheses
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                stack.append(c)
            else:
                if not stack:
                    return False

                curr = stack.pop()
                if  ((curr != '(' and c == ')') or
                    (curr != '[' and c == ']') or
                    (curr != '{' and c == '}')):
                    return False

        return not stack