class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        out_put = []
        common = dict()
        
        for i in range(len(list1)):
            if list1[i] in list2:
                common[list1[i]] = i
        
        for j in range(len(list2)):
            if list2[j] in common.keys():
                common[list2[j]] += j

        min_val = min(common.values())
        for key , value in common.items():
            if value == min_val:
                out_put.append(key)

        return out_put


        

                
