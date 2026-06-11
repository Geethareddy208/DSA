def shifted(arr):
    n=len(arr)
    ans=float("inf")                #infinte
    low=0
    high=n-1
    index=0
    while(low<=high):
        mid=(low+high)//2
        ##left half
        if(arr[low]<=arr[mid]):
            if(arr[low]<ans):
                ans=arr[low]
                index=low
            low=mid+1           #ans updated or not definately we should remove left space
        ###right half
        if(arr[mid]<=arr[high]):
            if(arr[mid]<ans):
                ans=arr[mid]
                index=mid
            
            high=mid-1   
            
    return index           #remove right space
arr=list(map(int,input().split()))
print(shifted(arr))