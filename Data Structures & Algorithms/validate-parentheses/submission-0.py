class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for c in s:
            if c in d:
                if not stack or (d[c] != stack[-1]):
                    return False
                stack.pop()
            else:
               stack.append(c)
        return not stack