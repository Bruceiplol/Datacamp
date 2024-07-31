# Import necessary packages
import pandas as pd
import numpy as np

# Begin coding here ...
# Use as many cells as you like
df_p = pd.read_csv('data/airbnb_price.csv')
df_t = pd.read_excel('data/airbnb_room_type.xlsx')
df_r = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

print(df_p.head())
print(df_t.head())
print(df_r.head())

df = pd.merge(df_p, df_t, on='listing_id')
df = pd.merge(df, df_r, on='listing_id')
#print(df.head())
print(df.info())

# cleaning data
#price
df["price"] = df["price"].str.replace(" dollars", "").astype('float')
print(df["price"].dtype)

#room_type
#df["room_type"] = df["room_type"].astype('category')
#print(df.groupby("room_type").sum())

df["room_type"] = df["room_type"].str.lower()
#print(df.groupby("room_type").sum())
df["room_type"] = df["room_type"].astype('category')
#print(df["room_type"].describe())

#review_date
df["last_review"] = pd.to_datetime(df["last_review"])

#answer
first_reviewed = df["last_review"].min()
last_reviewed = df["last_review"].max()
nb_private_rooms = df[df["room_type"]=="private room"].shape[0]
avg_price = round(df["price"].mean(), 2)

review_dates = pd.DataFrame({
    "first_reviewed":[first_reviewed],
    "last_reviewed":[last_reviewed],
    "nb_private_rooms":[nb_private_rooms],
    "avg_price":[avg_price],
})
print(review_dates)
