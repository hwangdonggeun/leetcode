Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def longestPalindrome(self, s: str) -> str:
...         if len(s) == 0:
...             return ""
...         
...         start = 0
...         end = 0
...         
...         for i in range(len(s)):
...             len1 = self.expandAroundCenter(s, i, i)
...             len2 = self.expandAroundCenter(s, i, i + 1)
...             max_len = max(len1, len2)
...             
...             if max_len > end - start:
...                 start = i - (max_len - 1) // 2
...                 end = i + max_len // 2
...         
...         return s[start:end + 1]
...     
...     def expandAroundCenter(self, s, left, right):
...         while left >= 0 and right < len(s) and s[left] == s[right]:
...             left -= 1
...             right += 1
...         return right - left - 1
