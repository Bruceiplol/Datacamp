# All required libraries are imported here for you.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
crops = pd.read_csv("soil_measures.csv")

# Write your code here
print(crops.info())
print(crops.isna().sum()) #no missing value
print(crops["crop"].unique()) #target is categorical value

# define dataset and target variables
X = crops.drop("crop", axis=1)
y = crops["crop"]

print(X, y)
print(X.values, y.values)

# split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21)

# evaluate feature performance
feature_dict = {}
log_reg = LogisticRegression(multi_class = "multinomial")

for f in crops.drop("crop", axis=1).columns:
    log_reg.fit(X_train[[f]], y_train)
    y_pred = log_reg.predict(X_test[[f]])
    f_performance = metrics.f1_score(y_test, y_pred, average="weighted")
    feature_dict[f] = f_performance
    print(f"f1_score for {f}: {f_performance}")

# f1_score for K: 0.23673624601294851
best_predictive_feature = {"K": feature_dict["K"]}
