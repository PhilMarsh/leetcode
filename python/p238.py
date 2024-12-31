class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()

        # built left products.
        left_prod = 1
        for num in nums:
            res.append(left_prod)
            left_prod *= num

        # build right products and multiply with left products.
        right_prod = 1
        for index in range(len(nums) - 1, -1, -1):
            num = nums[index]
            res[index] *= right_prod
            right_prod *= num

        return res

