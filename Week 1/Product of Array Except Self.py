class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        prefix_product = 1
        postfix_product = 1
        for i in range(1, len(nums)):
            prefix_product *= nums[i-1]
            postfix_product *= nums[len(nums) - i]
            prefix[i] = prefix_product
            postfix[len(nums) - i - 1] = postfix_product
        
        for i in range(len(nums)):
            prefix[i] *= postfix[i]
        return prefix