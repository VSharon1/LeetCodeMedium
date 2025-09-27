from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)

        for s in strs:
            abc_array_key = [0] * 26

            for char in s:
                abc_array_key[ord(char) - ord("a")] += 1

            result_dict[tuple(abc_array_key)].append(s)

        return list(result_dict.values())
