class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                stack.append(c)
            else:
                # no matching beginning parentheses
                if not stack:
                    return False

                # check if parentheses match
                curr = stack.pop()
                if  ((curr != '(' and c == ')') or
                    (curr != '[' and c == ']') or
                    (curr != '{' and c == '}')):
                    return False

        # return true only if all parentheses were matched
        return not stack