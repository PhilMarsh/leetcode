class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        observations:
        - all local minimums (ie: both neighbors are higher) get 1.
        - local maxes are the max of either slope (left or right).
        - ends of the line can be treated as flat.
        - at each index with value N, there are 9 cases:
            - N -: /-\ end up, start down
            - N N: /-- end up
            - N +:  /  continue up
            N N -: --\ start down
            N N N: --- noop
            N N +: --/ start up
            + N -:  \  continue down
            + N N: \-- end down
            + N +: \-/ end down, start up
        - "start" resets the slope counter.
        - "end" adds to the total according to the current slope counter.
        - up vs down mostly doesn't matter. both directions add to the total
          the same way. the only special case is we need to avoid double-counting
          peaks.
        """
        total = 0
        len_of_slope = None  # will be set before first read.
        pending_peak = None  # set and cleared when needed.

        prev_ratings = [ratings[0]] + ratings[:-1]
        next_ratings = ratings[1:] + [ratings[-1]]
        for index, (prev_rate, curr_rate, next_rate) in enumerate(
            zip(prev_ratings, ratings, next_ratings)
        ):
            # continue climbing up or down.
            if prev_rate < curr_rate < next_rate or prev_rate > curr_rate > next_rate:
                len_of_slope += 1
                continue

            if prev_rate != curr_rate:
                total += _triangle_num(len_of_slope)

                # avoid double-counting peaks.
                # valleys aren't a problem because 2*0 == 0.
                if prev_rate < curr_rate and curr_rate > next_rate:
                    pending_peak = len_of_slope
                elif pending_peak is not None:
                    assert prev_rate > curr_rate
                    # keep the max() by reverting the extra min().
                    total -= min(pending_peak, len_of_slope)
                    pending_peak = None

            if curr_rate != next_rate:
                len_of_slope = 1

        return total + len(ratings)


def _triangle_num(height):
    return sum(i for i in range(height + 1))

