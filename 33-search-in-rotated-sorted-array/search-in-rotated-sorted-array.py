class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = -1
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if target == nums[mid]:
                ind = mid
                break
            if nums[mid] <= nums[right]:
                # if right side is sorted
                if nums[mid] < target <= nums[right]:
                    # if target is in right sorted part
                    left = mid + 1
                else:
                    # if target in left unsorted part
                    right = mid - 1
            else:
                # left side is sorted
                if nums[left] <= target < nums[mid]:
                    # target in left sorted part
                    right = mid - 1
                else:
                    # target is in right unsorted part
                    left = mid + 1
        return ind