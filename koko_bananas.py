class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while (low<=high):
            mid=(low+high)//2      #koko eating speed
            sm=0
            for i in piles:
                sm+=ceil(i/mid)
            if sm<=h:
                high=mid-1
            else:
                low=mid+1
        return low
        