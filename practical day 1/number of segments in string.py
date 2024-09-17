class Solution:
    def countSegments(self, s: str) -> int:
        return len([segment for segment in s.split() if segment])
solution = Solution()
print(solution.countSegments("Hello, World! 123"))  
print(solution.countSegments("   "))  
print(solution.countSegments("abc 123 def456"))  
print(solution.countSegments("This is a test."))  
