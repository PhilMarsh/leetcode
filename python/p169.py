class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Majority Vote Algorithm
        """
        count = 0
        winner = None
        for num in nums:
            if count == 0:
                winner = num
                count = 1
            elif num == winner:
                count += 1
            else:
                count -= 1

        return winner

