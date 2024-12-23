from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = _nums_to_indexes_lookup(nums)
        for num, indexes in lookup.items():
            index = indexes[0]
            diff_indexes = lookup.get(target - num)
            if diff_indexes is not None:
                diff_index = diff_indexes[-1]
                if index != diff_index:
                    return [index, diff_index]
        raise Exception("No solution.")


def _nums_to_indexes_lookup(numbers):
    lookup = defaultdict(list)
    for index, num in enumerate(numbers):
        lookup[num].append(index)
    return dict(lookup)
