func twoSum(nums []int, target int) []int {
    mapsum:=map[int]int{}
    for i,x:=range nums{
        if k,ok := mapsum[target - x]; ok{
            return []int{k, i}
        }
        mapsum[x]=i
    }
    return nil
