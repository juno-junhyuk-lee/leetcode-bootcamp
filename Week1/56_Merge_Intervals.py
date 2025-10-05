class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval

        merged.append(prev)
        return merged