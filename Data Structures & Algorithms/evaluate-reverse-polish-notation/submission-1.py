class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if not token in['+','-','*','/']:
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()
            
                if token=='+':
                    sum=a+b
                    stack.append(sum)
                elif token=='-':
                    diff=a-b
                    stack.append(diff)
                elif token=='*':
                    mul=a*b
                    stack.append(mul)
                else:
                    div=int(a/b)
                    stack.append(div)
        return stack[0]

