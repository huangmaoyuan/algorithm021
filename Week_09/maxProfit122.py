class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m=len(prices)
        n=2
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,m):
                dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
                dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]
