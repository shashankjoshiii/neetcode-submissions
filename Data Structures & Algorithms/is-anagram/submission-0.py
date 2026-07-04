class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasha={}
        hashb={}
        for hi in s:
            hasha[hi]=hasha.get(hi,0)+1
        for hello in t:
            hashb[hello]=hashb.get(hello,0)+1
        return (hasha==hashb)
        