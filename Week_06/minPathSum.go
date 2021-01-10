func minPathSum(grid [][]int) int {
    var min func(a int , b int) int
    min = func(a int, b int) int{
        if a<b{
            return a
        }else{
            return b
        }
    }
    dp:=grid
    m:=len(grid)
    n:=len(grid[0])
    for i:=0;i<m;i++{
        for j:=0;j<n;j++{
            if i==0 && j==0{
                continue
            }else if i==0 && j!=0{
                dp[i][j]=dp[i][j]+dp[i][j-1]
            }else if i!=0 && j==0{
                dp[i][j]=dp[i][j]+dp[i-1][j]
            }else{
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+dp[i][j]
            }
        }
    }
    return dp[m-1][n-1]
}
