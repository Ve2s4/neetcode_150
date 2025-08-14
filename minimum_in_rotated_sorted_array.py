from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float("inf")
        l, r = 0, len(nums) - 1
        while l <= r:

            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            else:
                mid = (l + r) // 2
                ans = min(ans, nums[mid])
                # Is left sorted ?
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            

        return ans
            
sol = Solution()

print(sol.findMin([4,5,6,7,0,1,2]))