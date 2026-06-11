
def largestrect(height):
    def findPSE(height):
        n=len(height)
        stack=[]
        ans=[0]*n
        for i in range(0,n):
            while(len(stack)!=0 and height[stack[-1]]>=height[i]):
                stack.pop()
            if(len(stack)==0):
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    def findNSE(height):
        n=len(height)
        stack=[]
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while(len(stack)!=0 and height[stack[-1]]>=height[i]):
                stack.pop()
            if(len(stack)==0):
                ans[i]=n
            else:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    n=len(height)
    pse=findPSE(height)
    nse=findNSE(height)
    area=0
    maxArea=0
    for i in range(0,n):
        area=height[i]*(nse[i]-pse[i]-1)
        maxArea=max(area,maxArea)
    return maxArea
height=list(map(int,input().split()))
print(largestrect(height))