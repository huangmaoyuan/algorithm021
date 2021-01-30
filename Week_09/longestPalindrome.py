class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        max_len=-1
        maxi=-1
        maxj=-1
        dp=[[0]*n for _ in range(n)]
        for j in range(0,n):
            for i in range(0,j+1):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]==1):
                    dp[i][j]=1
                    if j-i>max_len:
                        max_len=j-i
                        maxi=i
                        maxj=j
        l=list(s)
        res=l[maxi:maxj+1]
        return "".join(res)
