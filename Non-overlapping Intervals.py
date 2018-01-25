# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# Runtime: O(nlogn)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x.end)
        count = 1
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start >= end:
                count += 1
                end = intervals[i].end
 
        return len(intervals) - count 