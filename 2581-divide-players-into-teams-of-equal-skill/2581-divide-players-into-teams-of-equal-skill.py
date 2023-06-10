class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        target=sum(skill)/(n/2)
        skill.sort()
        ptr1=0
        ptr2=n-1
        chemistry=0
        cur_sum=skill[ptr1]+skill[ptr2]
        matchedpairs=0
        if int(target)!=target:
            return -1
        while ptr2>=ptr1:
            if cur_sum!=target:
                if cur_sum>target:
                    ptr2-=1
                else:
                    ptr1+=1
                cur_sum=skill[ptr1]+skill[ptr2]
            else:
                chemistry+=skill[ptr1]*skill[ptr2]
                matchedpairs+=1
                ptr1+=1
                ptr2-=1
                cur_sum = skill[ptr1] + skill[ptr2]
                
        if matchedpairs != n/2:
            chemistry=-1
        
        return chemistry

        