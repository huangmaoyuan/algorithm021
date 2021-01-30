class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap=dict()
        for i in s:
            hashmap[i]=hashmap.get(i,0)+1
        for j in s:
            if hashmap[j]==1:
                return s.index(j)
        return -1
