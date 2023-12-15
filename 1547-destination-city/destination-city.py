class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        start_city = set()
        end_city = set()

        for start ,end in paths:
             start_city.add(start)
             end_city.add(end)

        for i in end_city:
            if i not in start_city:
                return i