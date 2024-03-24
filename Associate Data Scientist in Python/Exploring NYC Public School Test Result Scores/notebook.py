# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# 1. Which NYC schools have the best math results?
# criteria, columns, requirements
best_math_schools = schools[schools["average_math"]>= 800*0.8][["school_name","average_math"]].sort_values("average_math", ascending=False)
print(best_math_schools)

# 2. What are the top 10 performing schools based on the combined SAT scores?
# create new column
schools["total_SAT"] = schools["average_math"]+ schools["average_reading"] + schools["average_writing"]
# columns, requirements, display
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False).head(10)
print(top_10_schools)

# 3. Which single borough has the largest standard deviation in the combined SAT score?
# groupby, target column, columns, display
borough_df = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
# filter by requirement
largest_std_dev = borough_df[borough_df["std"] == borough_df["std"].max()]
# rename columns
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})
# move index column ("borough") back to column
largest_std_dev.reset_index(inplace=True)
print(largest_std_dev)
