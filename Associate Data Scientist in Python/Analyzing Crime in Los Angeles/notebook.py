# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes.head()

# Start coding here
# Use as many cells as you need
#peak_crime_hour 
crimes["OCC_hour"] = crimes["TIME OCC"].str[:2]
crimes["OCC_hour"].astype(int)
sns.countplot(data=crimes, x="OCC_hour", order=crimes["OCC_hour"].value_counts().index)
plt.show()
peak_crime_hour = 12

#peak_night_crime_location
#area, night_crimes(10pm-3:59am)
#AREA NAME, OCC filter
night_crimes = crimes[crimes["OCC_hour"].isin(["22","23","00","01","02","03"])]
peak_night_crime_location = night_crimes.groupby("AREA NAME", as_index=False)["OCC_hour"].count().sort_values("OCC_hour", ascending=False).iloc[0]["AREA NAME"]

#age groups crime
#Vict Age
age_labels=["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
age_bins=[0,17,25,34,44,54,64,np.inf]

crimes["Age Group"] = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels)
victim_ages = crimes["Age Group"].value_counts()
