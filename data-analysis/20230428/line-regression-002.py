import os
import numpy as np

os.system("cls")

data_elapsed_day = [
  0.0,  1.0,  2.0,  3.0,  4.0 , 7.0,  8.0,  11.0, 14.0, 16.0,
  17.0, 18.0, 21.0, 22.0, 24.0, 25.0, 28.0, 29.0, 32.0, 36.0,
  42.0, 43.0, 45.0, 50.0, 56.0, 58.0, 63.0, 64.0, 65.0, 66.0,
  67.0, 71.0, 73.0, 79.0, 80.0, 84.0, 85.0, 86.0, 87.0, 88.0
]

data_elapsed_day = [int(data_elapsed_day[i]) for i in range(len(data_elapsed_day))]

cumulated_sale_sum = []
sum = [1, 7, 4, 2, 4, 2, 2, 1, 1, 3, 2, 4, 1, 2, 4, 2, 1, 7, 1, 1, 2, 1, 4, 2, 2, 1, 1, 3, 3, 2, 3, 1, 1, 5, 1, 3, 2, 3, 1, 5]
for i in range(len(sum)):
    if i == 0: cumulated_sale_sum.append(sum[i])
    else:      cumulated_sale_sum.append(cumulated_sale_sum[i - 1] + sum[i])

print(data_elapsed_day)
print(cumulated_sale_sum)

data_elapsed_day   = np.array(data_elapsed_day).reshape(-1, 1)
cumulated_sale_sum = np.array(cumulated_sale_sum).reshape(-1, 1)

# print(data_elapsed_day)
# print(cumulated_sale_sum)

from sklearn.linear_model import LinearRegression
linearRegression = LinearRegression()

X = data_elapsed_day
Y = cumulated_sale_sum

linearRegression.fit(X, Y)

# os.system("cls")
print(linearRegression.coef_[0])
print(linearRegression.intercept_)

import matplotlib.pyplot as plt
plt.scatter(X, Y)

min_x = np.min(data_elapsed_day)
max_x = np.max(data_elapsed_day)

print(min_x, max_x)
x = np.linspace(min_x, max_x, 100)
y = linearRegression.coef_[0][0] * x + linearRegression.intercept_[0]
plt.plot(x, y, color = 'red')
plt.title('y = {}x + {}'.format(linearRegression.coef_[0][0], linearRegression.intercept_[0]))
plt.show()

# [0.90732105]
# [13.84434629]