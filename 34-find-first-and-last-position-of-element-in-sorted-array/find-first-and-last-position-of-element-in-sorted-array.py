class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = last = -1
        found = False

        for i in range(len(nums)):
            if nums[i] == target and not found:
                first = last = i
                found = True
            elif nums[i] == target:
                last = i

        return [first, last]