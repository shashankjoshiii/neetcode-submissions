class Solution:
    def productExceptSelf(self, nums):
        output = [1]

        # Build suffix products
        for i in range(len(nums) - 1, 0, -1):
            output.append(output[-1] * nums[i])

        output = output[::-1]

        left = 1

        # Multiply by prefix products
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        return output