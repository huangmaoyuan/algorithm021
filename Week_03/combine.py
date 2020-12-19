class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        def recursion(index,arr):
            if len(arr)==k:
                res.append(arr[:])
            for i in range(index,n+1):
                arr.append(i)
                recursion(i+1,arr)
                arr.pop()
        recursion(1,[])
        return res
