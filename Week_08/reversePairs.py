class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ans=0
        def mergesort(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)>>1
            left=mergesort(nums[:mid])
            right=mergesort(nums[mid:])
            return merge(left,right)

        def merge(left,right):
            m,n=len(left),len(right)
            i,j=0,0
            while i<m and j<n:
                if left[i]>2*right[j]:
                    self.ans+=m-i
                    j+=1
                else:
                    i+=1
            i,j=0,0
            temp=[]
            while i<m and j<n:
                if left[i]<=right[j]:
                    temp.append(left[i])
                    i+=1
                else:
                    temp.append(right[j])
                    j+=1
            while i<m:
                temp.append(left[i])
                i+=1
            while j<n:
                temp.append(right[j])
                j+=1
            return temp
        mergesort(nums)
        return self.ans
