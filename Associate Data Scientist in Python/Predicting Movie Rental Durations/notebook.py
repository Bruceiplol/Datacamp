import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE

# Import any additional modules and start coding below
from sklearn.linear_model import Lasso, LinearRegression, LogisticRegression
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV


df = pd.read_csv("rental_info.csv")
#print(df.head())
#print(df.isna().sum())
seed = 9

# Create a column named "rental_length_days"
df["rental_length"] = pd.to_datetime(df["return_date"]) - pd.to_datetime(df["rental_date"])
#print(df["rental_length"])
df["rental_length_days"] = df["rental_length"].dt.days
#print(df["rental_length_days"])

# Create two columns of dummy variables from "special_features"
#print(df[["special_features"]])
df["deleted_scenes"] =  np.where(df["special_features"].str.contains("Deleted Scenes"), 1,0)
df["behind_the_scenes"] = np.where(df["special_features"].str.contains("Behind the Scenes"), 1,0)

# Avoiding columns that leak data about the target
cols_drop = ["special_features", "rental_length", "rental_length_days", "rental_date", "return_date"]
X = df.drop(cols_drop, axis=1)
y= df["rental_length_days"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = seed)
scores=[]
#for alpha in [0.01, 0.03, 0.1, 0.5, 1, 10]:
#    lasso = Lasso(alpha=alpha)
#    lasso.fit(X_train, y_train)
#    lasso_pred = lasso.predict(X_test)
#    scores.append(lasso.score(X_test, y_test))
    
names = X.columns
lasso = Lasso(alpha=0.01, random_state=seed)
lasso_coef = lasso.fit(X_train, y_train).coef_
#plt.bar(names, lasso_coef)
#plt.xticks(rotation=45)
#plt.show()

X_lasso_train, X_lasso_test = X_train.iloc[: ,lasso_coef >0], X_test.iloc[:, lasso_coef>0]
lr = LinearRegression()
logreg = LogisticRegression(random_state=seed)
dr = DecisionTreeRegressor(random_state=seed)
classifiers = [("Linear Regression", lr),("Logistic Regression", logreg), ("Regression Tree", dr)]

for clf_name, clf in classifiers:
    clf.fit(X_lasso_train, y_train)
    y_pred = clf.predict(X_lasso_test)
    print("{:s} : {:.3f}".format(clf_name, MSE(y_test, y_pred)**(1/2)))

params_df = {
    'n_estimators': np.arange(1,101,1),
    'max_depth': np.arange(1,11,1),
}
rf = RandomForestRegressor()

rf_rs = RandomizedSearchCV(rf, param_distributions=params_df, cv=5, random_state=seed)
rf_rs.fit(X_train, y_train)
best_params = rf_rs.best_params_
#print(best_params)
best_model = rf_rs.best_estimator_
y_pred = best_model.predict(X_test)
rmse_test = MSE(y_test, y_pred) **(1/2)
print('Random Forest : {:3f}'.format(rmse_test))

best_model = rf
best_mse = mse_random_forest
