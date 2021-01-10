class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        count=0
        for j in range(n):
            for i in range(0,j+1):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]==1):
                    dp[i][j]=1
                    count+=1
        return count
