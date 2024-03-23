# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("netflix_data.csv", index_col = 0)
netflix_subset = netflix_df[netflix_df["type"] != "TV Show"]
netflix_movies = netflix_subset.iloc[:, [1,4,6,7,9]]
short_movies = netflix_movies[netflix_movies["duration"] < 60]
colors=[]
for lab, row in netflix_movies.iterrows():
    if row["genre"] == "Children":
        colors.append("Red")
    elif row["genre"] == "Documentaries":
        colors.append("Blue")
    elif row["genre"] == "Stand-Up":
        colors.append("Yellow")
    else:
        colors.append("Green")

fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies["release_year"], netflix_movies["duration"], c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")

plt.show()
