class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        prev = {}

        for i in range(len(s)):
            prev[s[i]] = i

        start = 0
        a = 0
        lists = []

        for i in  range(len(s)):
            a = max(a,prev[s[i]])
            x = (a + 1) - start
            if a == i:
                lists.append(x)
                start = a + 1
                a = 0
        return lists



        