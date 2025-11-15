task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        base = "is a high priority task"
    case "medium":
        base = "is a medium priority task"
    case "low":
        base = "is a low priority task"
    case _:
        base = "has an unspecified priority"

if time_bound == "yes":
    print(f"Reminder: '{task}' {base} that requires immediate attention today!")
else:
    print(f"Note: '{task}' {base}. Consider completing it when you have free time.")

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
