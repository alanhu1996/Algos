# Given a collection of intervals, merge all overlapping intervals.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        def isNotOverlap(i1, i2):
            return i1.end < i2.start
        for i in sorted(intervals, key=lambda n: n.start):
            # Insert interval if there is no overlap.
            if len(result) == 0 or isNotOverlap(result[-1], i):
                result.append(i)
            else:
                # Apply merge if there is overlap.
                if result[-1].end < i.end:
                    result[-1].end = i.end
        return result