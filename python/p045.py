class Solution:
    def jump(self, nums: List[int]) -> int:
        end_index = len(nums) - 1
        num_jumps = 0
        min_index = 0
        max_index = 0
        while max_index < end_index:
            (
                min_index,
                max_index,
            ) = (
                max_index + 1,
                max(i + nums[i] for i in range(min_index, max_index + 1)),
            )
            num_jumps += 1

        return num_jumps

