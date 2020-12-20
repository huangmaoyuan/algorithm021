func combine(n int, k int) [][]int {
    var res [][]int
    var recursion func(index int, arr []int)
    recursion=func(index int,arr []int){
        if len(arr)==k{
            temp := make([]int, k)
            copy(temp,arr)   //注意记录结果时深拷贝arr，否则递归返回到上一层，arr去除最后一个元素时，res也会受到影响
            res=append(res,temp)
        }
        for i:=index;i<n+1;i++{
            arr=append(arr,i)
            recursion(i+1,arr)
            arr=arr[:len(arr)-1]
        }
    }
    recursion(1,[]int{})
    return res
}
