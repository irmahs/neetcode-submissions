class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(tokens[i])
            else:
                b = int(stack[-1])
                stack.pop()
                a = int(stack[-1])
                stack.pop()
                if tokens[i] == '+':
                    result = a + b
                    stack.append(result)
                elif tokens[i] == '-':
                    result = a - b
                    stack.append(result)
                elif tokens[i] == '*':
                    result = a * b
                    stack.append(result)
                elif tokens[i] == '/':
                    result = int(a / b)
                    stack.append(result)
        return int(stack[-1])
        