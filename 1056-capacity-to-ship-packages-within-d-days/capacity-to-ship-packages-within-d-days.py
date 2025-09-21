class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def cargo(mid):
            day = 1
            weight = 0
            for i in range(len(weights)):
                weight += weights[i]
                if weight > mid:
                    day += 1
                    weight = weights[i]
            return day


        best = -1
        while low <= high:

            mid = low + (high - low) // 2

            if cargo(mid) > days:
                low = mid + 1

            else:
                high = mid - 1 
                best = mid
        return best

        