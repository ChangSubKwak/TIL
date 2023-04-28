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

sum = [1, 7, 4, 2, 4, 2, 2, 1, 1, 3, 2, 4, 1, 2, 4, 2, 1, 7, 1, 1, 2, 1, 4, 2, 2, 1, 1, 3, 3, 2, 3, 1, 1, 5, 1, 3, 2, 3, 1, 5]
cumulated_sale_sum = []
for i in range(len(sum)):
    if i == 0: cumulated_sale_sum.append(sum[i])
    else:      cumulated_sale_sum.append(cumulated_sale_sum[i - 1] + sum[i])

# print(data_elapsed_day)
# print(cumulated_sale_sum)

# data_elapsed_day   = np.array(data_elapsed_day).reshape(-1, 1)
# cumulated_sale_sum = np.array(cumulated_sale_sum).reshape(-1, 1)

data_elapsed_day   = np.array(data_elapsed_day)
cumulated_sale_sum = np.array(cumulated_sale_sum)

# print(data_elapsed_day)
# print(cumulated_sale_sum)

# print(np.average(data_elapsed_day))
# print(np.average(cumulated_sale_sum))
# print(np.var(data_elapsed_day))
# print(np.var(cumulated_sale_sum))
# print(np.cov(data_elapsed_day, cumulated_sale_sum))
# print(np.cov(data_elapsed_day))
# print(np.cov(cumulated_sale_sum))

average1 = np.average(data_elapsed_day)
average2 = np.average(cumulated_sale_sum)
variance1 = np.var(data_elapsed_day)
variance2 = np.var(cumulated_sale_sum)

covariance = 0.0
for i in range(len(data_elapsed_day)):
  covariance += (data_elapsed_day[i] - average1) * (cumulated_sale_sum[i] - average2)
covariance /= 40.0

print("covariance", covariance)
# covariance = np.cov(data_elapsed_day, cumulated_sale_sum)[0][1]

a = covariance / variance1
b = average2 - a * average1

print("a", a)
print("b", b)

X = data_elapsed_day
Y = cumulated_sale_sum

import matplotlib.pyplot as plt
plt.scatter(X, Y)

min_x = np.min(data_elapsed_day)
max_x = np.max(data_elapsed_day)
sum_maxamt = 119 / 2

print(min_x, max_x)
x = np.linspace(min_x, max_x, 100)
y = a * x + b
plt.plot(x, y, color = 'red')

y = sum_maxamt - a * x - b
plt.plot(x, y, color = 'green')

plt.axvline(x=0, color = 'black')   # draw x =0 axes
plt.axhline(y=0, color = 'black')   # draw y =0 axes

plt.title('y = {}x + {}'.format(a, b))
plt.show()


import sympy
x, y = sympy.symbols('x, y')
f = sum_maxamt - a * x - b
result = sympy.solve(f)
print("result", result)

# 하루치 재고량 계산 
print("one day stock ", sum_maxamt - a * (result[0] - 5) - b)

