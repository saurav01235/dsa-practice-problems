# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.


# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.


class Solution:
    def lenOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hs = {}
        res = 0
        l = 0
        for i in range(len(s)):
            if hs.get(s[i]) is None:
                hs[s[i]] = 1
            else:
                hs[s[i]] = hs[s[i]] + 1
            while len(hs)>2:
                hs[s[l]] = hs[s[l]] - 1
                if hs[s[l]] == 0:
                    del hs[s[l]]
                l += 1
            res = max(res, (i - l + 1))
        return res


obj = Solution().lenOfLongestSubstringTwoDistinct("eceba")
print(obj)
