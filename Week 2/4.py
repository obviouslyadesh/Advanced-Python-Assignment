employee_salaries = {
    "Hari": 65000,
    "Sher": 73000,
    "Lok": 49000,
    "Bam": 86000,
    "Ram": 55000,
    "Lalita": 68000
}

employees_list = list(employee_salaries.items())

filtered_employees = list(filter(lambda emp: emp[1] >= 60000, employees_list))

adjusted_salaries = list(map(lambda emp: (emp[0], round(emp[1] * 1.05)), filtered_employees))

print("Original salaries:", employee_salaries)
print("\nEmployees with salaries >= $60,000:")
for name, salary in filtered_employees:
    print(f"- {name}: ${salary:,}")
    
print("\n Salaries after 5% raise:")
for name, salary in adjusted_salaries:
    print(f"- {name}: ${salary:,}")