class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        chset=set()
        ml=0
        l=0
        for r in range(n):
            if s[r] not in chset:
                chset.add(s[r])
                ml=max(ml,r-l+1)
            else:
                while s[r] in chset:
                    chset.remove(s[l])
                    l+=1
                chset.add(s[r])
        return ml
        