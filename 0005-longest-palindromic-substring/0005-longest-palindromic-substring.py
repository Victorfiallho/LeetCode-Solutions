class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultado = s[0]

        for i in range(len(s)):

            left, right = i - 1, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > len(resultado):
                    resultado = s[left:right+1]
                left -= 1   
                right += 1 

            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > len(resultado):
                    resultado = s[left:right+1]
                left -= 1
                right += 1

        return resultado