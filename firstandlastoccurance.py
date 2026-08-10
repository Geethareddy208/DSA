nums=list(map(int,input().split()))
target=int(input())
n=len(nums)
first=-1
left=0
right=n-1
#first occurance
while(left<=right):
    mid=(left+right)//2
    
    if nums[mid]==target:
        first=mid
        right=mid-1
    if nums[mid]>=target:
        right=mid-1
    else:
        left=mid+1
last=-1
left=0
right=n-1
while(left<=right):
    mid=(left+right)//2
    if nums[mid]==target:
        last=mid
        left=mid-1
    if nums[mid]>target:
       right=mid-1
    else:
       left=mid+1

print(first,last)


