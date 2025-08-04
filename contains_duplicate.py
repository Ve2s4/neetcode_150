# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return not len(unique) == len(nums)
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        freq_dict = {}

        for num in nums:
            if freq_dict.get(num):
                return True
            else:
                freq_dict[num] = 1

        return False

solution = Solution()