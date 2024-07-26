func min(arr []int)(int, int) {
    minVal := arr[0]
    minIndex := 0
    for index, value := range arr {
        if value < minVal {
            minVal = value
            minIndex = index 
        }
    }
    return minVal , minIndex
}

func luckyNumbers (matrix [][]int) []int {

    var lucky []int
    
    var row int = len(matrix)

    for i:=0 ; i < row ; i++{
        minVal , minIndex := min(matrix[i])

        for j:=0 ; j < row; j++{
            if matrix[j][minIndex] > minVal{
                break
            }
            if j == len(matrix) - 1{
                lucky = append(lucky, minVal)
            }
        }
    }

    return lucky

}
