from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low <= high:
            if target == numbers[low] + numbers[high]:
                return [low + 1, high + 1]
            elif target > numbers[low] + numbers[high]:
                low += 1
            else:
                high -= 1
