class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = '+-/*'
        for i in tokens:
            if i not in oper:
                stack.append(i)
            elif i in oper:
                res = 0
                print(i)
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if i == '+':
                    res = op1+op2
                elif i == '-':
                    res = op2-op1
                elif i == '*':
                    res = op1*op2
                elif i == '/':
                    res = op2/op1
                else:
                    continue
                stack.append(res)
                
        return int(stack[0])