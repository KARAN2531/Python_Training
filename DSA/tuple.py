#Tuple 

#1. Write a Python program to create a tuple.

test_tup = ()
print(type(test_tup))

#2. Write a Python program to create a tuple with different data types.

tup = (['karan', 'akshat'], 1,2,(3,4,5))
print(type(tup))
print(type(tup[0]))
print(type(tup[1]))

#3. Write a Python program to unpack a tuple in several variables.

a, b, c = (1, 2, 3)
print(a)
print(b)
print(c) 

#4. Write a Python program to create the clone of a tuple.

original_tuple = (1, 2, 3, 4, 5)

cloned_tuple = tuple(original_tuple)

print("Original Tuple:", original_tuple)
print("Cloned Tuple:", cloned_tuple)

#       or 

# Import the 'deepcopy' function from the 'copy' module

from copy import deepcopy  # noqa: E402

# Create a tuple containing various data types
tuplex = ("HELLO", 5, [], True)
# Print the contents of the 'tuplex' tuple
print(tuplex)

# Create a deep copy of the 'tuplex' tuple using the 'deepcopy()' function
tuplex_colon = deepcopy(tuplex)

# Modify the third element of the 'tuplex_colon' tuple, which is a list, by appending the value 50
tuplex_colon[2].append(50)

# Print the 'tuplex_colon' tuple after the modification
print(tuplex_colon)

# Print the original 'tuplex' tuple to demonstrate that it remains unchanged
print(tuplex) 

#5. Write a Python program to find the repeated items of a tuple.

tup = (1,2,3,2,3,4,5,1,6,7,7,3)
duplicates = []
for x in tup:
    y = tup.count(x)
    if y > 1:
        duplicates.append(x)

print(set(duplicates))

#6. Write a Python program to check whether an element exists within a tuple.

tup = (1,2,3,2,3,4,5,1,6,7,7,3)
x = input("Enter what you want fo find: ")
if tup.count(x)>1:
    print("Yes! It exists!")
else:
    print("does not exist")

#7. Write a Python program to convert a list to a tuple.

lst = [1,2,3,4,5]
lst_to_tuple = tuple(lst)
print(lst_to_tuple)
print(type(lst_to_tuple))

#8. Write a Python program to remove an item from a tuple.
try:
    tup = (1, 2, 3, 4, 5)  # Original tuple
    tup_list = list(tup)  # Convert tuple to list

    x = int(input("Enter the position of the element you want to remove: "))  

    if 1 <= x <= len(tup_list):  # Ensure valid index
        tup_list.pop(x - 1)  # Remove the element at the given position
        tup = tuple(tup_list)  # Convert back to tuple
        print("Updated tuple:", tup)
    else:
        print("Error: Position out of range.")

except ValueError:
    print("Error: Please enter a valid integer.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
        
#9. Write a Python program to slice a tuple.

tup = (1,2,3,4,5,6,7)
sliced_tup = tup[1:3]
print(sliced_tup)

#10. Write a Python program to reverse a tuple.

tup = (1,2,3,4,5)
reversed_tup = tup[::-1]
print(reversed_tup)

new_tup = reversed(list(tup))
print(tuple(new_tup))