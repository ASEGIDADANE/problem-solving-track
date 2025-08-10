class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0
        prefix = {0:1}

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in prefix:
                count += prefix[prefix_sum - k]
            if prefix_sum not in prefix:
                prefix[prefix_sum] = 1
            else:
                prefix[prefix_sum] += 1
        return count
                

        