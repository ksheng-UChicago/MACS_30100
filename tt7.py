import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

## YOUR CODE HERE ##
morg_df = pd.read_csv("./data/morg_d07_strings.csv", index_col = "h_id")



# TASKS 2-6
# For each of the tasks, print the value requested in the task.


## YOUR CODE HERE ##
# TASK 2
print(morg_df["age"])

# TASK 3
print(morg_df.loc["1_2_2"])

# TASK 4
print(morg_df.iloc[0:4])

# TASK 5
missing = {}

for column in morg_df.columns:
    if any(morg_df[column].isna()):
        missing[column] = 0

print(missing)

# TASK 6

morg_df.fillna(value = missing)


### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

## YOUR CODE HERE ##

for cat in TO_CATEGORICALS:
    morg_df[cat] = morg_df[cat].astype("category")


# Example use of cut()
boundaries = range(16, 89, 8)
morg_df.loc[:, "age_bin"] = pd.cut(morg_df.loc[:, "age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

### Task 8

## YOUR CODE HERE ##
boundaries = range(0, 99, 10)
morg_df.loc[:, "hwpw_bin"] = pd.cut(morg_df.loc[:, "hours_worked_per_week"],
                                    bins = boundaries,
                                    labels = range(len(boundaries) - 1),
                                    include_lowest = True, right = True)

print("Morg columns types after Task 8")
print(morg_df.dtypes)


### Tasks 9-13
filter = (morg_df["hours_worked_per_week"] >= 35)
morg_df[filter]

filter = (morg_df["employment_status"] != "Working")
morg_df[filter]

filter = ((morg_df["hours_worked_per_week"] >= 35) | (morg_df["earnings_per_week"] > 1000))
morg_df[filter]

race_count = morg_df["race"].value_counts()[:5]
print(race_count)

race_count_2 = morg_df.groupby("race").size()[:5]
print(race_count_2)

### Task 14

students = pd.read_csv("data/students.csv")
extended_grades = pd.read_csv("data/extended_grades.csv")
