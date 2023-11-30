class Solution:
    def average(self, salary: List[int]) -> float:
        min_ = min(salary)
        max_ = max(salary)

        return (sum(salary)-min_-max_)/(len(salary)-2)