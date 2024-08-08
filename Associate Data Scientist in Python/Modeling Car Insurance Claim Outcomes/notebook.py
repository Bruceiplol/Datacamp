# Import required modules
import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

# Start coding!
df = pd.read_csv('car_insurance.csv')
print(df.head())
print(df.info())

#missing value: credit_score, annual_mileage
df["credit_score"].fillna(df["credit_score"].mean(), inplace=True)
df["annual_mileage"].fillna(df["annual_mileage"].mean(), inplace=True)
print(df.info())

#build model
models= []
features = df.drop(columns=["id","outcome"]).columns

for f in features:
    model = logit(f"outcome ~ {f}", data=df).fit()
    models.append(model)

print(models)

#measuring performance
accuracies= []

for f in range(0, len(models)):
    conf_matrix = models[f].pred_table()
    TN = conf_matrix[0,0]
    TP = conf_matrix[1,1]
    FN = conf_matrix[1,0]
    FP = conf_matrix[0,1]
    acc = (TN + TP) / (TN + TP + FN + FP)
    accuracies.append(acc)
print(accuracies)

#result
best_feature = features[accuracies.index(max(accuracies))]

best_feature_df = pd.DataFrame({
    "best_feature": best_feature,
    "best_accuracy": max(accuracies)
}, index=[0])

print(best_feature_df)
