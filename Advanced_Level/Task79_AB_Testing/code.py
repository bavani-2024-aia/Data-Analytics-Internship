import pandas as pd

data = {
    "Group": ["A", "A", "A", "B", "B", "B"],
    "Clicks": [120, 135, 128, 145, 150, 148]
}

df = pd.DataFrame(data)

group_a_avg = df[df["Group"] == "A"]["Clicks"].mean()
group_b_avg = df[df["Group"] == "B"]["Clicks"].mean()

print("Average Clicks for Group A:", group_a_avg)
print("Average Clicks for Group B:", group_b_avg)

if group_b_avg > group_a_avg:
    print("Group B performed better.")
else:
    print("Group A performed better.")