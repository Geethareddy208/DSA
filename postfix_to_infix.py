class Solution:
    def postToInfix(self, postfix):
        # Code here


        n=len(postfix)
        i=0
        stack=[]
        while(i<n):
            if postfix[i].isalnum:
                stack.append(postfix[i])
            else:
                t1=stack[-1]
                stack.pop()
                t2=stack[-1]
                stack.pop()
                conv= '('+ t2+postfix[i] + t1 + ')'
                stack.append(conv)
            i+=1
        return stack[-1]
