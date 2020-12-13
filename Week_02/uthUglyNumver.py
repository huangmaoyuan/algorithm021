class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[1]*n
        a=b=c=0
        for i in range(1,n):
            t1,t2,t3=dp[a]*2,dp[b]*3,dp[c]*5
            dp[i]=min(t1,t2,t3)
            if dp[i]==t1:
                a+=1
            if dp[i]==t2:
                b+=1
            if dp[i]==t3:
                c+=1
        return dp[-1]
