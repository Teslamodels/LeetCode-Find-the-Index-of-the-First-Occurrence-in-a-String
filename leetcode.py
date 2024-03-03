class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]

solution1 = Solution()
print(solution1.isPalindrome(-121))