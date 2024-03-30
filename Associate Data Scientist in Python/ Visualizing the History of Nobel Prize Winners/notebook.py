# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Start coding here!
df = pd.read_csv("./nobel.csv")
print(df.head())
print(df.info())

#What is the most commonly awarded gender and birth country?
top_gender = df["sex"].value_counts(sort=True).index[0]
print(top_gender)
top_country = df["birth_country"].value_counts(sort=True).index[0]
print(top_country)

# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
df["usa_winner"] = df["birth_country"] == "United States of America"
df["decade"] = (np.floor(df["year"]/10)*10).astype(int)
prop_usa_winner = df.groupby("decade", as_index=False)["usa_winner"].mean()
max_decade_usa = prop_usa_winner[prop_usa_winner["decade"] == prop_usa_winner["decade"].max()]["decade"].values[0]
print(max_decade_usa)
ax1 = sns.relplot(x="decade", y="usa_winner", data=prop_usa_winner, kind="line")

#Which decade and Nobel Prize category combination had the highest proportion of female laureates?
df["female_winner"] = df["sex"] == "Female"
prop_female_winner = df.groupby(["decade", "category"], as_index=False)["female_winner"].mean()
max_female_winner = prop_female_winner[prop_female_winner["female_winner"]==prop_female_winner["female_winner"].max()]
max_female_dict ={prop_female_winner["decade"].values[0]:prop_female_winner["category"].values[0]}
print(max_female_dict)
ax2 = sns.relplot(x="decade", y="female_winner", data=prop_female_winner, kind="line", hue="category")

#Who was the first woman to receive a Nobel Prize, and in what category?
df_female = df[df["female_winner"]]
firt_female_winner = df_female[df_female["year"]==df_female["year"].min()]
first_woman_name = firt_female_winner["full_name"].values[0]
first_woman_category = firt_female_winner["category"].values[0]
print((first_woman_name, first_woman_category))

#Which individuals or organizations have won more than one Nobel Prize throughout the years?
won_count = df["full_name"].value_counts()
repeat_list = list(won_count[won_count>=2].index)
print(repeat_list)
ax3 = sns.countplot(data=df, x="full_name", order=repeat_list)
plt.xticks(rotation=90)
