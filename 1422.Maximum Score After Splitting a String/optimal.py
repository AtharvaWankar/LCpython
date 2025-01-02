class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeroes = s.count('0')  # Count total number of '0's in the string

        newZero = 0
        one = 0
        ans = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                one += 1
            else:
                newZero += 1

            if i != 0:  # Avoid splitting at the start
                ans = max(ans, one + (zeroes - newZero))

        return ans