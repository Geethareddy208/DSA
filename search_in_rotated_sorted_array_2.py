nums=list(map(int,input().split()))
target=int(input())
low=0
high=len(nums)-1
found=False
while(low<=high):
    mid=(low+high)//2
    if nums[mid]==target:
        found=True
        break
    if nums[low]==nums[mid]==nums[high]:
        low=low+1
        high=high-1
    #left sorted or not check 
    elif nums[low]<=nums[mid]:
        if nums[low]<=target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1
    #right sorted
    elif nums[mid]<=nums[high]:
        if nums[mid]<=target<=nums[high]:
            low=mid+1
        else:
            high=mid-1
print(found)
          