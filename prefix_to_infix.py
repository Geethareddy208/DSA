class Solution:
    def preToInfix(self, s):
        # Code here
        n=len(s)
        i=n-1
        stack=[]
        while(i>=0):
            if s[i].isalnum():
                stack.append(s[i])
            else:
                t1=stack[-1]
                stack.pop()
                t2=stack[-1]
                stack.pop()
                conv='(' + t1 + s[i] + t2 + ')'
                stack.append(conv)
            i-=1
        return stack[-1]
        