class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)
        for i in range(n):
            
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            
            elif s[i]==')' or s[i]==']' or s[i]=='}':
                if len(stack)==0:
                    return False
                ch=stack[-1]
            

                if s[i]==')' and ch=='(':
                    stack.pop()

                    
                elif s[i]==']' and ch=='[':
                    stack.pop()
                elif s[i]=='}' and ch=='{':
                    stack.pop()
            
                else:
                    return False
        return len(stack)==0
        