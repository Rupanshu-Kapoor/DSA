class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            if nums[mid] <= nums[right]:
                # right side is sorted
                if nums[mid] < target <= nums[right]:
                    # target in right sorted side
                    left = mid + 1
                else:
                    # target in left unsorted sidr
                    right = mid - 1

            else:
                # left side is sorted
                if nums[left] <= target < nums[mid]:
                    # target in left sorted side
                    right = mid - 1
                else:
                    # target in right unsorted side
                    left = mid + 1
        return False