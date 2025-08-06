from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0

        nums_set = set(nums)

        longest_sequence = 1

        for ele in nums_set:
            # check if the current element is the start of the sequence
            if ele - 1 not in nums_set:
                temp = ele
                while True:
                    if temp + 1 in nums_set:
                        temp += 1
                    else:
                        break
                print(temp, ele)
                longest_sequence = max(longest_sequence, temp - ele + 1)

        return longest_sequence



sol = Solution()

print(sol.longestConsecutive([100,4,200,1,3,2]))