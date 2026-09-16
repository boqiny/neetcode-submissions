"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        i = j = 0
        count = 0
        res = 0

        while i < len(starts):
            if starts[i] < ends[j]:
                count += 1
                i += 1
                res = max(res, count)
            else:
                count -= 1
                j += 1
        return res
