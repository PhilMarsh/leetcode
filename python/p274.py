from collections import defaultdict


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        quality_counts = defaultdict(int)

        for score in citations:
            quality_counts[score] += 1

        max_score = max(quality_counts.keys())

        total_count = 0
        for score in range(max_score, 0, -1):
            total_count += quality_counts[score]
            if total_count >= score:
                return score

        return 0

