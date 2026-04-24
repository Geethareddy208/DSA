class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        windsize=n-k
        ws=sum(cardPoints[:windsize])
        totalsum=sum(cardPoints)
        ml=ws
        
        for i in range(windsize,n):
            ws+=cardPoints[i]-cardPoints[i-windsize]
            ml=min(ml,ws)
        return totalsum-ml
