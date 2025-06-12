def activity_selection(activities):
    # Step 1: Sort activities by end time
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_end_time = activities[0][1]

    # Step 2: Pick non-overlapping activities
    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end

    return selected

# Test
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
print("Selected activities:", activity_selection(activities))
