func numIslands(grid [][]byte) int {
    res:=0
    var dfs func(i int,j int)
    dfs = func(i int,j int){
        if 0<=i && i<len(grid) && 0<=j && j<len(grid[0]) && grid[i][j]=='1'{
            grid[i][j]='0'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        }
    }
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[0]);j++{
            if grid[i][j]=='1'{
                dfs(i,j)
                res++
            }
        }
    }
    return res
}
