class Solution:
    
    def priority(self, op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        elif op == '^':
            return 3
        return 0
    def infixToPostfix(self, s):
        # code here
        stack=[]
        ans=""
        i=0
        n=len(s)
        while(i<n):
            if s[i].isalnum():
                ans=ans+s[i]
            elif s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                while(len(stack)!=0 and stack[-1]!='('):
                    ans=ans+stack[-1]
                    stack.pop()
                stack.pop()
            else:
                while(len(stack)!=0 and self.priority(stack[-1])>=self.priority(s[i])):
                    ans=ans+stack[-1]
                    stack.pop()
                stack.append(s[i])
            i+=1
        while(len(stack)!=0):
            ans=ans+stack[-1]
            stack.pop()
        return ans
                    