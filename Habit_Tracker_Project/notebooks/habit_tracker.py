import pandas as pd
import random
from datetime import datetime, timedelta
import os

# -------------------------------
# Project Setup
# -------------------------------

random.seed(42)

# Create data folder if it doesn't exist
os.makedirs("../data", exist_ok=True)

# Habits
habits = [
    ("Exercise", "Fitness"),
    ("Reading", "Learning"),
    ("Meditation", "Health"),
    ("Coding", "Learning"),
    ("Drink Water", "Health"),
    ("Walking", "Fitness"),
    ("Journal", "Personal Growth"),
    ("Yoga", "Fitness"),
    ("Sleep 8 Hours", "Health"),
    ("Study", "Education")
]

moods = ["Happy", "Neutral", "Tired", "Motivated", "Stressed"]
notes = [
    "Completed successfully",
    "Busy schedule",
    "Felt energetic",
    "Need improvement",
    "Excellent consistency",
    "Skipped due to work",
    "Weekend break",
    "Very productive",
    "Not feeling well",
    "Great progress"
]

# Date Range (365 Days)
start_date = datetime(2025, 1, 1)
num_days = 365

records = []

# Streak Dictionary
streaks = {habit[0]: 0 for habit in habits}

for day in range(num_days):

    current_date = start_date + timedelta(days=day)

    for habit_name, category in habits:

        completed = random.choices(
            ["Yes", "No"],
            weights=[80, 20],
            k=1
        )[0]

        target = 1

        if completed == "Yes":
            time_spent = random.randint(15, 90)
            streaks[habit_name] += 1
        else:
            time_spent = 0
            streaks[habit_name] = 0

        mood = random.choice(moods)
        note = random.choice(notes)

        records.append({
            "Date": current_date.strftime("%Y-%m-%d"),
            "Habit": habit_name,
            "Category": category,
            "Target": target,
            "Completed": completed,
            "Time Spent (Minutes)": time_spent,
            "Mood": mood,
            "Current Streak": streaks[habit_name],
            "Notes": note
        })

# Create DataFrame
df = pd.DataFrame(records)

# Save CSV
output_path = "habit_tracker.csv"
df.to_csv(output_path, index=False)

print("=" * 50)
print("Habit Tracker Dataset Created Successfully!")
print("=" * 50)
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_path}")
print("=" * 50)

print("\nFirst 10 Rows:\n")
print(df.head(10))

print("\nDataset Information:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe(include='all'))

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nCompleted Habit Count")
print(df["Completed"].value_counts())

print("\nHabit Count")
print(df["Habit"].value_counts())
