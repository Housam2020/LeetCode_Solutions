class Solution(object):
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]

        final = []
        for i in range(len(intervals)):
            # not overlapping cases
            # smaller
            if newInterval[1] < intervals[i][0]:
                final.append(newInterval)
                return final + intervals[i:]
            # bigger
            elif newInterval[0] > intervals[i][1]:
                final.append(intervals[i])
                if i == len(intervals) - 1:
                    final.append(newInterval)
                    return final
            # Overlap! Merge time
            else:
                start = min(intervals[i][0], newInterval[0])
                end = max(intervals[i][1], newInterval[1])
                newInterval = [start, end]
                if i == len(intervals) - 1:
                    final.append(newInterval)
                    return final
                






        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        