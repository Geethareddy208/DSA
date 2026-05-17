class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for curr in s:
            if stack and  stack[-1]==curr:
                stack.pop()
            else:
                stack.append(curr)
        return ''.join(stack)