"""
RECORD CHECK  -  my version
===========================

Name  :  Wonshni Reedoy
Lane  :  AI 
Date  :  28th October 2026

Run it:   python template.py
"""


"""Read and process records from a CSV file. 
Calculate percentages, and assign status categories, display results and save a CSV file and a bar chart.
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("records.csv")

df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda percent: "OVER LIMIT" if percent >= 100
    else "WARNING" if percent >= 90
    else "OK"
)

# Display the complete DataFrame, including the new columns.
print ("Full DataFrame:")
print (df)

print ("\nRecords that are not OK:")
print (df[df["status"] != "OK"])   # Select rows where the status is not equal to "OK".

# Group records by status and count the number in each group.
status_counts = df.groupby("status").size()

print ("\nCount per status:")
print (status_counts)

# Save the complete DataFrame to a new CSV file.
# index=False prevents an additional index column.
df.to_csv("processed_records.csv", index = False)

# Create a bar chart showing the count for each status.
status_counts.plot(
    kind = "bar", 
    title = "Count per Status",
    color = ["pink", "purple", "red"],
    alpha = 0.8,
    edgecolor = "black"
    )

# Add axis labels and horizontal gridlines for readability.
plt.xlabel("Status")
plt.ylabel("Number of Records")
plt.grid(axis="y", alpha = 0.3)

# Adjust the layout and save the chart.
plt.tight_layout()
plt.savefig("status_counts.png")

# Display the completed bar chart.
plt.show()



# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
