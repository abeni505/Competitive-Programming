class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
       
        
        left = 0
        right = len(skill) - 1

        check = [skill[0],skill[len(skill)-1]]

        total = 0
        while left < right:
            if skill[left] + skill[right] == sum(check):
                total += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
    
        return total
