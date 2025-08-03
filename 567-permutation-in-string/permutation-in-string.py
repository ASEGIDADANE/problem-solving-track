class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        con_s1 = Counter(s1)

        for i in range(n,len(s2) + 1):
            sub = s2[i-n:i]
          
            sub = Counter(sub)
            if sub == con_s1:
                return True
        return False
