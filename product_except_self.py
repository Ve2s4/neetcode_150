from typing import List

class Solution:

    def helper(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                arr[i] = nums[i]
            else:
                arr[i] = nums[i] * arr[i-1]
        return arr
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = self.helper(nums)
        suffix = list(reversed(self.helper(list(reversed(nums)))))

        output = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                output[i] = suffix[1]
            elif i == len(nums)-1:
                output[i] = prefix[len(nums)-2]
            else:
                output[i] = prefix[i-1] * suffix[i+1]
        return output
    

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))

