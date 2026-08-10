n=int(input())
low=1
high=n
while(low<high):
    mid=(low+high)//2
    if isBadVersion(mid)==True:
        high=mid
    else:
        low=mid+1
return low
    