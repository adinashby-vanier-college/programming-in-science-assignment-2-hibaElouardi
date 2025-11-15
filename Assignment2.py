import unittest

# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    unique_numbers = list(numbers)
    
    max_1 = max(unique_numbers)

    while max_1 in unique_numbers:
        unique_numbers.remove(max_1)

    if not unique_numbers:
        return max_1, None

    max_2 = max(unique_numbers)
    return max_1, max_2
    
    

#print(max_two_in_list([3, 8, 2, 10, 7]))

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    new_list = list(set(numbers))

    return sorted(new_list)


# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0

    for num in arr:
        total += num
        result += [total]

    return result

#print(cumulative_sum([1, 2, 3, 4])

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    result = []

    for i in range(columns):
        new_row = []
        for j in range(rows):
            new_row += [matrix[j][i]]
        result += [new_row]
    
    return result



# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    slice = lst[::step]

    return slice

#print(slice_every_nth([1, 2, 3, 4, 5, 6], 2))

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total_product_lists = sum([a * b for a, b in zip(list1, list2)])
    

    return total_product_lists

#print(dot_product([1,


# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    row1 = len(matrix1)
    column1 = len(matrix1[0])
    column2 = len(matrix2[0])

    result = []

    for i in range(row1):
        new_row = []
        for j in range(column2):
            total = 0 
            for k in range(column1):
                total += matrix1[i][k] * matrix2[k][j]

            new_row += [total]
        result += [new_row]

    return result
