class Solution:
    def findFirst(self, nums, target):
        pass
        first = -1
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right )//2

            if nums[mid] >= target:
                first = mid
                right = mid-1
            else:
                left = mid + 1
        if nums[first] != target:
            first = -1
        return first

    def findLast(self, nums, target):
        last = -1
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target:
                last = mid
                left = mid + 1
            else:
                right = mid - 1
        if nums[last] != target:
            last = -1
        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last] 