class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
solution1 = Solution()
print(solution1.strStr(haystack = "leetcode", needle = "leeto"))
