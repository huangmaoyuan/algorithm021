class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=grid
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0 and j!=0:
                    dp[i][j]=grid[i][j]+dp[i][j-1]
                elif i!=0 and j==0:
                    dp[i][j]=grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i][j-1],dp[i-1][j])
        return dp[m-1][n-1]
