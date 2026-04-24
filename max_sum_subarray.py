list=list(map(int,input().split()))
n=len(list)
k=int(input())
left=0
right=k-1
sum=list[0:k]
maxsum=0
while right<n-1:
    sum-=list[left]
    left+=1
    right+=1
    sum+=list[right]
    if(sum>maxsum):
        maxsum=sum
print(maxsum)

