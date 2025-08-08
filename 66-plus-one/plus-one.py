class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number="".join(str(d) for d in digits)
        number = int(number)
        number += 1
        res = [int(d) for d in str(number)]
        return res
        