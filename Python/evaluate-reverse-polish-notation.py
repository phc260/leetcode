class Solution:
    # @param tokens, a listk of stkring
    # @return an integer
    def evalRPN(self, tokens):
        operands = []

        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                operands.append(int(t))
            else:
                b = operands.pop()
                a = operands.pop()
                if t == '+': operands.append(a+b)
                elif t == '-': operands.append(a-b)
                elif t == '*': operands.append(a*b)
                elif t == '/': operands.append(int(a*1.0/b))
                    
        return operands.pop()