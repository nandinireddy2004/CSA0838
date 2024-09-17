class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels set, including both lower and upper case vowels
        vowels = set("aeiouAEIOU")
        
        vowel_list = [char for char in s if char in vowels]
        vowel_list.reverse()
        s_list = list(s)
        vowel_index = 0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowel_list[vowel_index]
                vowel_index += 1
        return ''.join(s_list)

sol = Solution()
s = "IceCreAm"
output = sol.reverseVowels(s)
print(output)


s = "leetcode"
output = sol.reverseVowels(s)
print(output)
