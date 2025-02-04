def merge_intervals(intervals):
    if not intervals:
        return []
    def start_time(interval):
        return interval[0]
    intervals.sort(key=start_time)
    merged_intervals=[]
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1] < interval[0] :
            merged_intervals.append(interval)
        else:
            last_merged=merged_intervals[-1]
            merged_intervals[-1] = (last_merged[0], max(last_merged[1], interval[1]))
    return merged_intervals
intervals=[(5,7),(10,13),(9,11)]
merged = merge_intervals(intervals)
print("Merged intervals: ", merged)
