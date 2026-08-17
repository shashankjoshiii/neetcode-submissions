class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        total = 0
        
        for num in nums:
            total += num
            maxi = max(maxi, total)
            if total < 0:
                total = 0
                
        return maxi