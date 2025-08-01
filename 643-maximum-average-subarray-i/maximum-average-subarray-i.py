class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sums = sum(nums[:k])
        maxx = sums
        
        for i in range(len(nums)-k):
            sums =  sums - nums[i] + nums[i + k]
            maxx = max(maxx,sums)
        print(maxx)
        return maxx / k

       
       

        