class Solution:

    def myMin(self, nums, left, right):
        if left >= right:
            return nums[left]
        mid = (left + right)//2

        left_min = self.myMin(nums, left, mid)
        right_min = self.myMin(nums, mid+1, right)

        mini = min(left_min, right_min)
        return mini

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        # return self.myMin(nums, left, right)

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        