import pandas as pd

# Sample data for courses and progress
courses = {
    "Course": ["Python Basics", "Data Science", "Machine Learning", "Web Development", "Statistics"],
    "CompletionPercentage": [90, 50, 70, 20, 60]
}

# Convert to DataFrame
df = pd.DataFrame(courses)

# Check for incomplete courses (less than 100% complete)
incomplete_courses = df[df["CompletionPercentage"] < 100]
print("Incomplete courses:")
print(incomplete_courses)

# Reminder for courses with less than 50% completion
reminder_courses = df[df["CompletionPercentage"] < 50]
print("\nCourses needing immediate attention (less than 50% complete):")
print(reminder_courses)
