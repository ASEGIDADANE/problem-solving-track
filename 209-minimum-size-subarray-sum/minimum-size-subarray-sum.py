class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        window_sum = 0
        min_lenght = float('inf')
        n = len(nums)
        flage = True


        for right in range(n):
            window_sum += nums[right]

            while window_sum >= target:
                min_lenght = min(min_lenght , (right - left + 1))
                window_sum -= nums[left]
                left += 1
                flage = False
        if flage:
            return 0
        return min_lenght
       