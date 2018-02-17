# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        startList = [i.start for i in intervals]
        endList = [i.end for i in intervals]
        
        startList.sort()
        endList.sort()
        
        endIndex = 0
        totalRooms = 0
        for startIndex in range(len(startList)):
            if startList[startIndex] < endList[endIndex]:
                totalRooms += 1
            else:
                endIndex += 1
                
        return totalRooms