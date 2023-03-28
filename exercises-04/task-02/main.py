import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import sklearn.linear_model as lm
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score,
)
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


data = pd.read_csv("data_C02_emission.csv")

# data = data.drop(["Make", "Model"], axis=1)

input_variables = [
    "Fuel Consumption City (L/100km)",
    "Fuel Consumption Hwy (L/100km)",
    "Fuel Consumption Comb (L/100km)",
    "Fuel Consumption Comb (mpg)",
    "Engine Size (L)",
    "Cylinders",
    "Fuel Type",
]

output_variable = ["CO2 Emissions (g/km)"]

ohe = OneHotEncoder()
X_encoded = ohe.fit_transform(data[["Fuel Type"]]).toarray()
data["Fuel Type"] = X_encoded

X = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

plt.figure()
plt.scatter(x=X_train[:, 0], y=y_train, c="b")
plt.scatter(x=X_test[:, 0], y=y_test, c="r")
plt.show()

sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

ax1 = plt.subplot(211)
ax1.hist(x=X_train[:, 0])
ax2 = plt.subplot(212)
ax2.hist(x=X_train_n[:, 0])
plt.show()

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
print(linearModel.coef_)

y_test_p = linearModel.predict(X_test_n)

RMSE = mean_squared_error(y_test, y_test_p, squared=False)
MAE = mean_absolute_error(y_test, y_test_p)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
R2 = r2_score(y_test, y_test_p)

plt.figure()
plt.scatter(x=X_test_n[:, 0], y=y_test, c="b")
plt.scatter(x=X_test_n[:, 0], y=y_test_p, c="r")
plt.show()

print("RMSE", RMSE)
print("MAE", MAE)
print("MAPE", MAPE)
print("R2", R2)
