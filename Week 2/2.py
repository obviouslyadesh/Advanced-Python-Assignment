work_hours = [35, 45, 49, 52, 47, 36, 56, 42, 39, 48]

filtered_hours = list(filter(lambda hours: hours >= 40, work_hours))
overtime_hours = list(map(lambda hours: hours - 40, filtered_hours))

print("Original hours:", work_hours)
print("Hours >= 40:", filtered_hours)
print("Overtime hours:", overtime_hours)