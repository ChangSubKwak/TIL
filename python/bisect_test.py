from bisect import bisect_left, bisect_right

array = [1, 2, 2, 2, 3]

result_left = bisect_left(array, 2)
result_right = bisect_right(array, 2)

print("result_left", result_left)
print("result_right", result_right)
