from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = list(_yield_deduplicated(nums))
        nums[0 : len(result)] = result
        return len(result)


def _yield_deduplicated(values):
    seen_counts = defaultdict(int)
    for val in values:
        seen_counts[val] += 1
        if seen_counts[val] <= 2:
            yield val

