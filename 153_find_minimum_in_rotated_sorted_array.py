from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        low = 0
        high = len(nums) - 1

        while low <= high:
            if nums[low] < nums[high]:
                result = min(result, nums[low])
                break

            mid = (low + high) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return result
