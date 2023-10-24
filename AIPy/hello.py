from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

dataset = fetch_california_housing()

x= dataset.data
y = dataset.target

model = LinearRegression()
model.fit(x,y)

p = model.predict(x)

mae = mean_absolute_error(y,p)

print("MAE: ", mae)
print ("mean y", np.mean(y))