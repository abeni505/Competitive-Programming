class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def next_index(current):
           return (current + nums[current]) % len(nums)


        for root_index in range(len(nums)):
            current_index = root_index
            # print(current_index ,next_)
            visited = set()

            while current_index not in visited and nums[next_index(current_index)] * nums[current_index] > 0:
                visited.add(current_index)
                current_index = next_index(current_index)
            # print(visited)
   
            if current_index == root_index and len(visited) > 1:
                return True
        
        return False
    