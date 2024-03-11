class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # brute force 1
        # count = 0
        # ele = -1

        # for i in range(len(nums)):
        #     if nums[i] == ele:
        #         count += 1
        #     else:
        #         if count == 1:
        #             return ele
        #         else:
        #             count = 1
        #             ele = nums[i]
        # return ele

        # brute force 2: hash map
        # h_map = {}
        # for i in nums:
        #     h_map[i] =h_map.get(i,0)+1
        # for i in h_map:
        #     if h_map[i] == 1:
        #         return i

        # brute force: xor
        # ans = 0
        # for i in nums:
        #     ans = ans ^ i

        # return ans


        # using binary search
        left, right = 0, len(nums)-1
        
        while left <= right:
            if left == right:
                return nums[left]
            mid = (left + right)//2
            if mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    right = mid - 1
                elif nums[mid] == nums[mid+1]:
                    left = mid + 1
                else:
                     return nums[mid]
            else:
                if nums[mid] == nums[mid + 1]:
                    right = mid - 1
                elif nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                     return nums[mid]