class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i, val in enumerate(nums[:-1]):
            if val == 0:
                if max_reachable <= i:
                    return False
            else:
                max_reachable = max(max_reachable, i + val)
        return True
