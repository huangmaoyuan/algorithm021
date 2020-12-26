nums=[4,5,6,7,0,1,2]
def search(nums):
	l,r=0,len(nums)-1
	while l<=r:
		mid=int((l+r)/2)
		if nums[mid]>nums[mid+1]:
			return mid
		if nums[mid]>nums[l]:
			l=mid+1
		else:
			r=mid
res=search(nums)
print(nums)
print("This array is disorder at index:" ,res,res+1)
