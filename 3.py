Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def lengthOfLongestSubstring(self, s: str) -> int:
...         char_map = {}
...         left = 0
...         max_length = 0
... 
...         for right in range(len(s)):
...             if s[right] in char_map:
...                 left = max(left, char_map[s[right]] + 1)
...             char_map[s[right]] = right
...             max_length = max(max_length, right - left + 1)
... 
...         return max_length
