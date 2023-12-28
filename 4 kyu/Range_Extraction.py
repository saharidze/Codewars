"""
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
"""
from __future__ import annotations


def solution(nums):
    ranges = []
    start = None
    end = None

    for num in nums:
        if start is None:
            start = num
            end = num
        elif num - end == 1:
            end = num
        else:
            if start == end:
                ranges.append(str(start))
            elif end - start >= 2:
                ranges.append(str(start) + '-' + str(end))
            else:
                ranges.append(str(start) + ',' + str(end))
            start = num
            end = num

    if start is not None:
        if start == end:
            ranges.append(str(start))
        elif end - start >= 2:
            ranges.append(str(start) + '-' + str(end))
        else:
            ranges.append(str(start) + ',' + str(end))

    return ','.join(ranges)
