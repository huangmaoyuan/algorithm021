func solveNQueens(n int) [][]string {
    if n<1{
        return nil
    }
    result:=[][]int{}
    cols:=make(map[int]bool)
    pie:=make(map[int]bool)
    na:=make(map[int]bool)
    var dfs func(n int,row int, cur_state []int)
    dfs = func(n int,row int,cur_state []int){
        if row>=n{
            result=append(result,cur_state)
        }
        for col:=0;col<n;col++{
            if _,ok:=cols[col];ok{
                continue
            }
            if _,ok:=pie[col+row];ok{
                continue
            }
            if _,ok:=na[row-col];ok{
                continue
            }
            cols[col]=true
            pie[col+row]=true
            na[row-col]=true
            dfs(n,row+1,append(cur_state,col))
            delete(cols,col)
            delete(pie,col+row)
            delete(na,row-col)
            
        }
    }
    dfs(n,0,[]int{})
    fmt.Println(result)
}
