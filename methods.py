# NumPy Arrays – Creation, Indexing, Operations
# NumPy Array Create 
import numpy as np
#  1D array 
arr1d = np.array([1, 2, 3, 4, 5])
#  2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
#  3D array 
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# Special functions zero array
zeros = np.zeros((3, 4))  
print(zeros)
# 3 row, 4 column - all 0
ones = np.ones((2, 3))    
# 2 row, 3 column - all 1
#  Identity matrix (diagonal- 1,others 0)
eye = np.eye(3)           
# 3x3 identity matrix
#  Range-ah array
range_arr = np.arange(0, 10, 2)   
# 0-10  2 step [0, 2, 4, 6, 8]
#  Equal interval array
linspace_arr = np.linspace(0, 1, 5)   
# 0 to 1-ku 5 equal parts [0., 0.25, 0.5, 0.75, 1.]
#  Random numbers array
random_arr = np.random.rand(2, 2)   
# 2x2 random numbers [0,1)
#  Indexing and Slicing (Data access) Basic-access 
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])   
# 1 (first element)
print(arr[1:4])   
# [2, 3, 4] (index 1 to 3)
#  2D array-la access 
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#  Single element
print(arr2d[1, 2])   
# 6 (2nd row, 3rd column)
#  Full row
print(arr2d[1])      
# [4, 5, 6] (2nd row)
#  Full column
print(arr2d[:, 1])   
# [2, 5, 8] (2nd column)
#  Sub-matrix
print(arr2d[0:2, 1:3])   
# [[2, 3], [5, 6]] (first 2 rows, columns 2-3)
#  Condition- filter
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])  
# [4, 5]
#  Array Operations (Maths operations)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#  Element-wise operations
print(a + b)   
# [5, 7, 9] (1+4, 2+5, 3+6)
print(a * b)   
# [4, 10, 18] (1*4, 2*5, 3*6)
print(a **2)  
# [1, 4, 9] (1², 2², 3²)
#  Number add 
print(a + 10)   
# [11, 12, 13] (1+10, 2+10, 3+10)
#  Matrix operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
#  Matrix multiplication (dot product)
print(np.dot(a, b))  
# or a @ b
#  [[19, 22], [43, 50]]
#  Transpose (row-column)
print(a.T)   
# [[1, 3], [2, 4]]
#  Summarize 
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))     
# 15 (total)
print(np.mean(arr))    
# 3.0 (average)
print(np.max(arr))     
# 5 (maximum)
print(np.min(arr))     
# 1 (minimum)
print(np.std(arr))     
# 1.414 (standard deviation)

arr = np.arange(12)   
#  3x4 matrix
reshaped = arr.reshape(3, 4)
#  Flat (1D-ah)
flattened = reshaped.flatten()





import pandas as pd

# From a list
s1 = pd.Series([1, 3, 5, 7, 9])
print(s1)

# With custom index
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s2)

# From a dictionary
data = {'apple': 3, 'banana': 5, 'cherry': 7}
s3 = pd.Series(data)
print(s3)


# Basic operations
print(s2 * 2) 
print(s2 + s2) 

# Boolean indexing
print(s2[s2 > 25])

# Accessing elements
print(s2['b'])  
print(s2[1])  


# # Pandas DataFrame
# # A DataFrame is a 2-dimensional labeled data structure with columns that can be of different types.

# # Creating a DataFrame
# # From a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
# print(df)

# With custom index
df_indexed = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df_indexed)

# From a list of dictionaries
data_list = [
    {'Name': 'Alice', 'Age': 25, 'City': 'NY'},
    {'Name': 'Bob', 'Age': 30, 'City': 'LA'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
df_from_list = pd.DataFrame(data_list)
print(df_from_list)

# Viewing data
print(df.head(2))  # First 2 rows
print(df.tail(1))   # Last row
print(df.shape)     # Dimensions (rows, columns)
print(df.columns)   # Column names
print(df.dtypes)    # Data types of columns

# Accessing columns
print(df['Name'])   # As Series
print(df[['Name', 'Age']])  # Multiple columns as DataFrame

# Adding new column
df['Salary'] = [70000, 80000, 90000, 100000]
print(df)

#  Indexing and Filtering
# Basic Indexing

# loc - label-based indexing
print(df.loc[0])           # First row
print(df.loc[0:2, 'Name']) # Rows 0-2, 'Name' column

# iloc - position-based indexing
print(df.iloc[0])          # First row
print(df.iloc[0:2, 0:2])   # Rows 0-1, columns 0-1

# at - fast scalar access by label
print(df.at[0, 'Name'])

# iat - fast scalar access by position
print(df.iat[0, 0])


# Boolean Indexing (Filtering)
# Simple conditions
print(df[df['Age'] > 30])

# Multiple conditions
print(df[(df['Age'] > 25) & (df['City'] == 'LA')])

# isin()
print(df[df['City'].isin(['NY', 'Chicago'])])

# query()
print(df.query('Age > 30 and Salary < 95000'))

# String operations
print(df[df['Name'].str.startswith('A')])

# Reading and Writing Excel & CSV Files
csv_data = pd.read_csv('D:\shopping.shopping.csv')
print(csv_data.head())

# Read Excel
# pip install openpyxl
excel_data = pd.read_excel(r"C:\Users\Admin\Downloads\Students.xlsx", sheet_name='Sheet2')
print(excel_data.head())

#create and write a file
# Write to CSV
df.to_csv('output.csv', index=False)

# Write to Excel
df.to_excel('output.xlsx', sheet_name='Employees', index=False)

# With options
df.to_csv('output_advanced.csv', 
          index=True, 
          columns=['Name', 'Salary'],  # Only these columns
          encoding='utf-8')

# # Create a sample DataFrame
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories'],
    'Price': [1200, 800, 400, 300, 50],
    'Quantity': [15, 30, 25, 10, 50],
    'Date': pd.date_range('20230101', periods=5)
}
sales = pd.DataFrame(data)
sales['Revenue'] = sales['Price'] * sales['Quantity']

# Basic analysis
print("Summary Statistics:")
print(sales.describe())

print("\nCategory-wise Summary:")
print(sales.groupby('Category').agg({'Price': 'mean', 'Quantity': 'sum', 'Revenue': 'sum'}))

# Filtering
high_value = sales[sales['Price'] > 500]
print("\nHigh Value Products:")
print(high_value)

# Sorting
print("\nTop 3 Products by Revenue:")
print(sales.sort_values('Revenue', ascending=False).head(3))

# Pivot table
print("\nPivot Table (Category vs Price):")
print(pd.pivot_table(sales, values='Price', index='Category', aggfunc=['mean', 'count']))

# Save analysis results
sales.to_excel('sales_analysis.xlsx', sheet_name='Sales Data', index=False)
