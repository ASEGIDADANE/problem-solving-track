class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * len(nums)
        prev = 0
        for i in range(len(nums)):
            prev += nums[i]
            self.prefix_sum[i] = prev


        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        result = self.prefix_sum[right] - self.prefix_sum[left - 1]
        return result


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)