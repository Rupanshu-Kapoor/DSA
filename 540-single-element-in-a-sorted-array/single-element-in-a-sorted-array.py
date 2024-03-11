class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # brute force 1
        count = 0
        ele = -1

        for i in range(len(nums)):
            if nums[i] == ele:
                count += 1
            else:
                if count == 1:
                    return ele
                else:
                    count = 1
                    ele = nums[i]
        return ele