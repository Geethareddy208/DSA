nums=list(map(int,input().split()))

low=0
high=len(nums)-1
ind=float('inf')
while(low<=high):
    mid=(low+high)//2
    if nums[low]<=nums[mid]:#sorted left so min in low itself
        if nums[low]<ind:
            ind=nums[low]
        low=mid+1
    elif nums[mid]<=nums[high]:
        if nums[mid]<ind:
            ind=nums[mid]
        high=mid-1

print(ind)

    