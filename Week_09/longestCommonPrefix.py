class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        if not strs:
            return res
        m=len(strs)
        n=len(strs[0])
        for j in range(n):
            c=strs[0][j]
            for i in range(1,m):
                if j >= len(strs[i]):
                    return res
                if c==strs[i][j]:
                    continue
                else:
                    return res
            res+=c
        return res
