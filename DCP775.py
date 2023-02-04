"""
DAILY CODING PROBLEM #775

Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom
lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

SOURCE: founders@dailycodingproblem.com
"""

import random
import numpy as np

def generate_random_array(size="random",
max_total_length=14*60,
max_class_length=150):
    if size == "random":
        size = random.randint(2,30*int(max_total_length/60)+1)
    times_array = []
    for c in range(size):
        start_time = random.randint(0,max_total_length)
        if start_time + max_class_length < max_total_length:
            max_end_time = start_time + max_class_length
        else:
            max_end_time = max_total_length
        end_time = random.randint(start_time+1,max_end_time+1)
        times_array.append([start_time,end_time])
    times_array.sort(key = lambda x: x[0])
    return np.array(times_array)

def find_min_rooms_needed(schedule):
    num_class_today = len(schedule)
    first_class_start = np.min(schedule)
    last_class_end = np.max(schedule)
    schedule_minutes = []
    for cls in schedule:
        schedule_minutes += [i for i in range(cls[0],cls[1]+1)]
    schedule_minutes.sort()
    max_conflicts = 0
    for minute in range(first_class_start, last_class_end + 1):
        conflicts = schedule_minutes.count(minute)
        if conflicts > max_conflicts:
            max_conflicts = conflicts
    return max_conflicts
    
# Randomly generate a schedule for today
schedule = generate_random_array()
print(f"Schedule Size:    {schedule.shape[0]}")
print("Schedule...")
print(schedule)

# Find the minimum number of classrooms needed today
# through the find_min_rooms_needed function.
min_rooms_needed = find_min_rooms_needed(schedule)
print(f"Minimum Classrooms Needed:    {min_rooms_needed}")