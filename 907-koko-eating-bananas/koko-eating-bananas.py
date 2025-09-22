class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        best = -1

        def hour(mid):
            cal_h = 0
            for i in range(len(piles)):
                cal_h += ceil(piles[i] / mid)
            return cal_h


        while low <= high:
            mid = low + (high - low ) // 2

            if hour(mid) > h:
                low = mid + 1
            else:
                high = mid - 1
                best = mid
        return best
        