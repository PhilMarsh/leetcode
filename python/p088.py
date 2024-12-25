class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        target_index = m + n - 1
        assert target_index == len(nums1) - 1
        left_index = m - 1
        right_index = n - 1
        while target_index >= 0:
            if left_index >= 0 and (
                right_index == -1 or nums1[left_index] > nums2[right_index]
            ):
                nums1[target_index] = nums1[left_index]
                left_index -= 1
            elif right_index >= 0 and (
                left_index == -1 or nums2[right_index] >= nums1[left_index]
            ):
                nums1[target_index] = nums2[right_index]
                right_index -= 1
            else:
                raise Exception("wat.")

            target_index -= 1

        assert left_index == -1 and right_index == -1

