class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        
        new_str = zip(*strs)
        
        count = 0
        for i in new_str:
            char = "".join(i)
            sort_char = "".join(sorted(char))

            if sort_char != char:
                count += 1

        return count
