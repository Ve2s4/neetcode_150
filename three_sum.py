from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = []

        for index, ele in enumerate(nums):

            if index > 0 and ele == nums[index-1]:
                continue

            i = index + 1
            j = len(nums) - 1

            while i < j:

                three_sum = ele + nums[i] + nums[j]

                if three_sum < 0:
                    i += 1
                elif three_sum > 0:
                    j -= 1
                else:
                    ans.append([ele, nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
        
        return ans
    
sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))