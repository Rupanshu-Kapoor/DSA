class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left <= right:

            if left == right:
                return left
            mid = (left + right)//2
            if (mid==0 and nums[mid]> nums[mid+1]) or\
            (mid==len(nums)-1 and nums[mid]>nums[mid-1]) or \
            (0<mid<len(nums)-1 and nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]):
                return mid
            
            if nums[mid+1]> nums[mid]:
                left = mid + 1
            else:
                right = mid - 1