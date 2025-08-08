from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        solution_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += num

            solution_sum = max(solution_sum, current_sum)

        return solution_sum
