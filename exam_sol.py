import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# #! Q1. c
# a = np.array([1, 2, 34])
# b = np.diag(a)
# print(b)
# c = b
# c[2, 2] = 56
# print(b)

# #!Q1.e (1)
# A = np.identity(3, dtype=int)
# # print(A)

# diagonal_value = np.array([3, 7, 9])
# B = np.diag(diagonal_value)

# print(B)

# #! Q1.e (2)   C(3,6) 3 rows and 6 columns
# C = np.concatenate((A, B), axis=1)
# print(C)

# #! Q1.e (3)    D(6,3) 6 rows and 3 columns
# D = np.concatenate([A, B])
# print(D)

# array = np.arange(9)
# print(array)
# n = array.reshape((3, 3))
# print(n)

# #! Q2.b
# df_withname = pd.DataFrame({'first': [37, 32, 3], 'scc': [7, np.NaN, 7]}, dtype=float)
# df_duplicate_removed = df_withname.drop_duplicates()  # * if all the col are duplicate with other row then drop
# # * removing duplicates acc to specific col
# df_duplicate_removed_col = df_withname.drop_duplicates('scc', keep='last')
# print(df_duplicate_removed_col)

dframe = pd.DataFrame(
    {'color': ['white', 'white', 'red', 'red', 'white'], 'value': [2, 1, 3, 3, 2]})
print(dframe)

c = dframe.drop_duplicates()
print(c)


# #! Q2. e
X = [1, 2, 3, 4, 6, 8]
y = [10, 20, 40, 50, 60, 80]
X1, X2, y1, y2 = train_test_split(X, y, random_state=0, train_size=0.5)

print(X1)
print(y1)
print(X2)
print(y2)
