class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_number_fruits = float('-inf')
        window = Counter()


        for right in range(len(fruits)):
            window[fruits[right]] += 1
            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:

                   del window[fruits[left]]
                left += 1
            max_number_fruits = max(max_number_fruits, right - left + 1)

        return max_number_fruits


            
            




