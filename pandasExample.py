import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

an = pd.DataFrame([1, 2, 2, 4, 5, np.NaN, 9], dtype=float)

a = pd.DataFrame([[1, 2, 2, 4, 5, np.NaN, 9], [
                 2, 5, 6, 4, 5, 0, 9]], dtype=float)  # * column wise assignment with total rows
ac = pd.DataFrame({'first': [37, 32, 3], 'scc': [7, np.NaN, 7]}, dtype=float)
# print(ac)
b = pd.DataFrame(np.random.randn(4, 6), dtype=int)

# print(b.head(4))

# print(b.index)  #* index in rows
# print(b.columns)  #* index in columns

# print(a.describe())  # * statistics of the data

# print(a.T)  # * row to column or vice versa
# print(a[0])  # * column with name
# print(a[1:3])  # *row from index to

# c = ac.duplicated('scc')  # * check for duplicates
# print(c)

# # * removing duplicates acc to specific col
# d = ac.drop_duplicates('scc', keep='last')
# print(d)

# csv = pd.read_csv('test.csv', header=None)
# print(csv)

# write_sv = csv.to_csv('test_write.csv', index=False, header=False)

# print((csv == 0).sum())  # * to check all col with 0 and sum them

# # * to check for NaN value or null value in all the col
# print(csv.isnull().sum())

# new_df = csv.replace(np.NaN, 0)  # * replacing null with 0
# print(new_df)

# remove_na = csv.dropna()  # * remove the row with null values
# print(remove_na)

# # * replace NaN values with the mean value of the col
# df_imputer = SimpleImputer().fit_transform(csv)
# print(df_imputer)


#! replace 0
# dframe = pd.DataFrame(
#     {'color': ['white', 'white', 'red', 'red', 'white'], 'value': [2, 1, 3, 3, 2]})
# print(dframe)
# new1 = {1: 5, 2: 'wet', np.NaN: 0}
# # dframe1 = dframe.dropna()
# dframe1 = dframe.replace(new1)
# print(dframe1)

#! mapping
# frame = pd.DataFrame({'item': ['ball', 'mug', 'pen', 'pencil', 'ashtray'], 'color': [
#                      'white', 'white', 'red', 'red', 'white']})
# print(frame)
# prices = {'ball': 5.56, 'mug': 4.20, 'bottle': 1.30,
#           'scissors': 3.41, 'pen': 1.30, 'pencil': 0.56, 'pencil': 0.576, 'ashtray': 2.75}

# frame['price'] = frame['item'].map(prices)
# print(frame)

# # ! filter
randframe = pd.DataFrame(np.random.randn(1000, 3))
print(randframe.std())
a = -1.3
print(np.abs(a) + a)
# print(randframe[(np.abs(randframe) > (3 * randframe.std())).any(1)])
randframe.describe()

# # ! groupBy sum
# frame = pd.DataFrame({'color': ['white', 'red', 'green', 'red', 'green'], 'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
#                       'price1': [5.56, 4.20, 1.30, 0.56, 2.75], 'price2': [4.75, 4.12, 1.60, 0.75, 3.15]})
# print(frame)
# group = frame[{'price1', 'price2'}].groupby(frame['color'])
# print(group.sum())
