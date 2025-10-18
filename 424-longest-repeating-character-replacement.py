class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            c_count[s[r]] = c_count.get(s[r], 0) + 1

            while (r - l + 1) - max(c_count.values()) > k:
                c_count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
