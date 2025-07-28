class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
         
        total_chemistry = 0
        sum_of_pair = sum(skill) / (len(skill) / 2)
        if len(skill) == 2:
            return skill[0] * skill[1]

        while left < right:
            if skill[left] + skill[right] == sum_of_pair:
                total_chemistry += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
        return total_chemistry

         

        
      




