import numpy as np
# Load the datasets into arrays
data1 = np.genfromtxt('testmarks1.csv', delimiter='\t', skip_header=1) 
data2 = np.genfromtxt('testmarks2.csv', delimiter='\t', skip_header=1)
# Matrix Operations
# Addition
matrix_sum = data1 + data2
# Subtraction
matrix_diff = data1 - data2
# Multiplication
matrix_product = np.matmul(data1[:, 1:], data2[:, 1:].T)
# Transpose 
matrix_transpose = data1.T
# Horizontal and Vertical Stacking 
horizontal_stack = np.hstack((data1, data2)) 
vertical_stack = np.vstack((data1, data2))
# Custom Sequence Generation 
custom_sequence = np.arange(10, 51, 10)
# Arithmetic and Statistical Operations # Mean
mean = np.mean(data1)
# Standard Deviation 
std_dev = np.std(data1)
# Minimum
minimum = np.min(data1)
# Maximum
maximum = np.max(data1)
# Mathematical Operations # Square Root
sqrt = np.sqrt(data1)
# Exponential
exp = np.exp(data1)
# Bitwise Operators
bitwise_and = np.bitwise_and(data1.astype(int), data2.astype(int)) 
bitwise_or = np.bitwise_or(data1.astype(int), data2.astype(int))
# Copying and Viewing Arrays 
copy_array = data1.copy() 
view_array = data1.view()
# Data Stacking
data_stack = np.column_stack((data1, data2))
# Searching
index = np.where(data1 == 40.9)
# Sorting

sorted_data = np.sort(data1, axis=0)
# Counting
unique_values, counts = np.unique(data1[:, 1], return_counts=True)
# Broadcasting 
broadcasted_array = data1 + 10
# Displaying the results print("Matrix Sum:") print(matrix_sum) print("\nMatrix Difference:") print(matrix_diff) print("\nMatrix Product:") print(matrix_product) print("\nMatrix Transpose:") print(matrix_transpose) print("\nHorizontal Stack:") print(horizontal_stack) print("\nVertical Stack:") print(vertical_stack) print("\nCustom Sequence:") print(custom_sequence) print("\nMean:")
print(mean)
print("\nStandard Deviation:")
print(std_dev ) 
print("\nMinimum:") 
print(minimum)
print("\nMaximum:") 
print(maximum)
print("\nSquare Root:") 
print(sqrt) 
print("\nExponential:") 
print(exp)
print("\nBitwise AND:") 
print(bitwise_and) 
print("\nBitwise OR:") 
print(bitwise_or) 
print("\nCopied Array:") 
print(copy_array)
print("\nView Array:") 
print(view_array)
print("\nData Stack:") 
print(data_stack)
print("\nIndex of 40.9 in data1:") 
print(index)
print("\nSorted Data:") 
print(sorted_data)
print("\nUnique Values and Counts:") 
print(unique_values, counts) 
print("\nBroadcasted Array:")
print(broadcasted_array)