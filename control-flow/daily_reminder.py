task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case to set base reminder based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a HIGH priority task."
    case "medium":
        reminder = f"'{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"'{task}' is a LOW priority task."
    case _:
        reminder = f"'{task}' has an UNKNOWN priority level."

# If-statement to customize based on time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " You can complete it when you have free time."

# Final customized reminder
print("\nReminder:", reminder)

