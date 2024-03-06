class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        indx = bisect.bisect_right(letters,target)
        
        return letters[indx] if indx < len(letters) else letters[0]