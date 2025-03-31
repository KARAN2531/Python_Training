# Dictionary

#1. Write a Python script to sort (ascending and descending) a dictionary by value.

sample_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

# Ascending order
sorted_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)

# Descending order
sorted_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)

#2. Write a Python script to add a key to a dictionary.
    #Sample Dictionary : {0: 10, 1: 20}
    #Expected Result : {0: 10, 1: 20, 2: 30}

Sample_Dictionary = {0: 10, 1: 20}
Sample_Dictionary.update({0: 10, 1: 20, 2: 20 })
print(Sample_Dictionary)

#3. Write a Python script to concatenate following dictionaries to create a new one.
    #Sample Dictionary :
    #dic1={1:10, 2:20}
    #dic2={3:30, 4:40}
    #dic3={5:50,6:60}
    #Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict)  
    
#4. Write a Python program to iterate over dictionaries using for loops.

dict = {0: 10, 1: 20}
for k,v in dict.items():
    print(f"Key : {k}, Value : {v}" )

#5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) 
# in the form (x, x*x).
    # Sample Dictionary ( n = 5) :
    #Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = 5
square_dict = {x: x*x for x in range(1, n+1)}
print(square_dict)  

#6. Write a Python program to remove a key from a dictionary.

sample_dict = {0: 10, 1: 20, 2: 30}
removed_key = 1

if removed_key in sample_dict:
    del sample_dict[removed_key]

print(sample_dict)  

#7. Write a Python program to print all unique values in a dictionary.
    #Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    #Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

unique_values = {val for dic in data for val in dic.values()}
print("Unique Values:", unique_values)  

#8. Write a Python program to create a dictionary from a string.
    #Note: Track the count of the letters from the string.
    #Sample string : 'w3resource'
    #Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

from collections import Counter  # noqa: E402

sample_str = 'w3resource'
letter_count = dict(Counter(sample_str))
print(letter_count)  

#9. Write a Python program to print a dictionary in table format.

sample_dict = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}

print("Key     | Value")
print("---------------")
for key, value in sample_dict.items():
    print(f"{key:<7} | {value}")

#10. Write a Python program to count the values associated with key in a dictionary.
    #Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    #Expected result: Count of how many dictionaries have success as True

data = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]

count_success = sum(1 for item in data if item.get('success') is True)
print("Count of success=True:", count_success) 

#11. Write a Python program to convert a list into a nested dictionary of keys.

lst = [1, 2, 3, 4]
nested_dict = current = {}

for item in lst:
    current[item] = {}
    current = current[item]

print(nested_dict)  

#12. Write a Python program to check multiple keys exists in a dictionary.

sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = {'a', 'c'}

if keys_to_check.issubset(sample_dict.keys()):
    print("All keys exist in the dictionary.")
else:
    print("Some keys are missing.")

#13. Write a Python program to count number of items in a dictionary value that is a list.

sample_dict = {'A': [1, 2, 3], 'B': [4, 5], 'C': [6, 7, 8, 9]}

count = sum(len(value) for value in sample_dict.values() if isinstance(value, list))
print("Total number of items in lists:", count) 
