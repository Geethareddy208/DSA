class Solution:
    def findPages(self, arr, k):
        # code here
        n=len(arr)
        if k>n:
            return -1
         
        
        def nop(limit):
            pages=0
            s=1
            for book in arr:
                if pages+book<=limit:
                    pages+=book
                else:
                    s+=1
                    pages=book
                if s>k:
                    return False
            return True
                    
        
        low=max(arr)
        high=sum(arr)
        ans=high
        while low<=high:
            mid=(low +high)//2
            if nop(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
        
         
        
        