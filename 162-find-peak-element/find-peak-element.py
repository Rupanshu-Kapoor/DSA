class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if left == right:
            return left
        if nums[0] > nums[1]:
            return 0
        if nums[right] > nums[right-1]:
            return right

        while left <= right:
            mid = (left + right)//2
            if (nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]):
                return mid
            
            if nums[mid+1]> nums[mid]:
                left = mid + 1
            else:
                right = mid - 1