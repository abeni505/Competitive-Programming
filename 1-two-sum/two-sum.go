func twoSum(nums []int, target int) []int {
    
    for i:= 0; i < len(nums); i++{
        for j:= i + 1; j < len(nums); j++{
            if nums[i] + nums[j] == target{
                ans := []int{i , j}
                return ans
            }
        }
    }
    return nums
}
