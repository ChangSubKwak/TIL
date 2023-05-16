import os
import pandas as pd
import numpy as np

from sklearn import datasets
data = datasets.load_diabetes()

# print(len(data))
# print(data.keys())
# print(data['data'].shape)
# print(len(data['feature_names']))

df = pd.DataFrame(data['data'], index=data['target'], columns=data['feature_names'])
# print(df)


from sklearn.linear_model import LinearRegression
linearRegression = LinearRegression()

X = df.bmi.values
X = X.reshape(-1,1)

Y = df.index.values
Y = Y.reshape(-1,1)

linearRegression.fit(X, Y)

os.system("cls")
print(linearRegression.coef_[0])
print(linearRegression.intercept_)

import matplotlib.pyplot as plt
plt.scatter(X, Y)
x = np.linspace(-0.1, 0.2, 100)
y = linearRegression.coef_[0][0] * x + linearRegression.intercept_[0]
plt.plot(x, y, color = 'red')
plt.title('y = {}x + {}'.format(linearRegression.coef_[0][0], linearRegression.intercept_[0]))
plt.show()
