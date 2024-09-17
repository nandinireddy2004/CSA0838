from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).keys().iter().next()
solution = Solution()
s = "abcd"
t = "abcde"
print("The difference is:", solution.findTheDifference(s, t))
