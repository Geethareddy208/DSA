class Solution:
    def postToPre(self, s):
        # Code here
        n=len(s)
        i=0
        stack=[]
        while(i<n):
            if s[i].isalnum():
                stack.append(s[i])
            else:
                t1=stack[-1]
                stack.pop()
                t2=stack[-1]
                stack.pop()
                conv=s[i]+t2+t1
                stack.append(conv)
            i+=1
        return stack[-1]
        