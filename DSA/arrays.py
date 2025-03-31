#1. Write a Python program to create an array of 5 integers and display the array items. 
# Access individual element through indexes.

import array

# Creating an array of 5 integers
arr = array.array('i', [10, 20, 30, 40, 50])

# Displaying the array elements
print("Array elements:", arr)

# Accessing elements by index
print("First element:", arr[0])
print("Last element:", arr[-1])

#2. Write a Python program to reverse the order of the items in the array.

arr.reverse() 
print("Reversed array:", arr)

#     or 

reversed_arr = arr[::-1]  
print("Reversed array (using slicing):", reversed_arr)

#3. Write a Python program to get the number of occurrences of a specified element in an array.

num = 30
count = arr.count(num)
print(f"Occurrences of {num}:", count)

#4. Write a Python program to remove the first occurrence of a specified element from an array.

num_to_remove = 30
if num_to_remove in arr:
    arr.remove(num_to_remove)  # Removes the first occurrence
print("Array after removal:", arr)
