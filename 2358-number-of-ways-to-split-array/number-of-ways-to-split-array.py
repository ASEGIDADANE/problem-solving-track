class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = [nums[0]]

        Number_valid_split = 0

        for i in range(1,n):
            prefix_sums.append((prefix_sums[-1] + nums[i]))
        
        for i in range(n-1):
            if prefix_sums[i] >= prefix_sums[-1] - prefix_sums[i]:
                Number_valid_split += 1
        return Number_valid_split