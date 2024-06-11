Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def twoSum(self, nums, target):
...         num_to_index = {}
...         for index, num in enumerate(nums):
...             complement = target - num
...             if complement in num_to_index:
...                 return [num_to_index[complement], index]
...             num_to_index[num] = index
... 
...             
