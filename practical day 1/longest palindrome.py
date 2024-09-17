class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        n = len(s)
        
        for i in range(n):
            # Check for odd-length palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r + 1]
                l -= 1
                r += 1
            
            # Check for even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r + 1]
                l -= 1
                r += 1
        
        return longest

# Example usage
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
        
