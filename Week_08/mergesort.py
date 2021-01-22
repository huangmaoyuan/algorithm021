def mergesort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)>>1
    left=mergesort(nums[:mid])
    right=mergesort(nums[mid:])
    return merge(left,right)

def merge(left,right):
    i,j=0,0
    temp=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    while i<len(left):
        temp.append(left[i])
        i+=1
    while j<len(right):
        temp.append(right[j])
        j+=1
    return temp

nums=[3,5,4,1,6,8,7,2,9]
print(nums)
print(mergesort(nums))