def quicksort(nums,left,right):
    if left >=right:
        return
    l,r=left,right
    pivot=nums[left]
    while l<r:
        while l<r and nums[r]>=pivot:
            r-=1
        nums[l]=nums[r]
        while l<r and nums[l]<pivot:
            l+=1
        nums[r]=nums[l]
    nums[l]=pivot
    quicksort(nums,left,l-1)
    quicksort(nums,l+1,right)

nums=[3, 5, 4, 1, 6, 8, 7, 2, 9]
print(nums)
quicksort(nums,0,len(nums)-1)
print(nums)