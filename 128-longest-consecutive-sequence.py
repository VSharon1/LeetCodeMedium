from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
        count = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                count = 0

                while (num + count) in nums_set:
                    count += 1

                longest_seq = max(longest_seq, count)

        return longest_seq
