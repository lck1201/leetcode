# Definition for an interval.
from functools import cmp_to_key

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# brilliant example
def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start): #NOTE: sorted function usage
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i
    return out


# def ascend_interval(x,y):
#     if x.start < y.start:
#         return -1
#     elif x.start > y.start:
#         return 1
#     else:
#         return 0
#
# class Solution:
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         if len(intervals) < 1: #NOTE
#             return intervals
#
#         intervals.sort(key=cmp_to_key(ascend_interval))
#
#         idx = 0
#         while idx != len(intervals)-1: #NOTE
#             left = intervals.pop(idx)
#             right = intervals.pop(idx)
#
#             if left.end >= right.start:
#                 new_it = Interval(left.start, max(left.end,right.end)) #Core
#                 intervals.insert(idx, new_it)
#             else:
#                 intervals.insert(idx, right)
#                 intervals.insert(idx, left)
#                 idx += 1 #NOTE
#
#         return intervals
#
