#List

#1 Write a Python program to sum all the items in a list.

list = [1,2,3,5]
sum = 0
for i in list:
    sum += int(i)
print(sum)    

#2. Write a Python program to multiplies all the items in a list.

list = [1,2,3,4]
total = 1
for i in list:
    total *= int(i)
print(total)    

#3. Write a Python program to get the smallest number from a list.

list = [1,3,5,23,2,47,68]
smallest_number = sorted(list)[0]
print(smallest_number)

#4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
    #Sample List : ['abc', 'xyz', 'aba', '1221']
    # Result : 2'''

Sample_List = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in Sample_List:
    if len(i)>1 and (i[0] == i[len(i)-1]):
        count+=1
print(count)

#5. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
    #Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    #Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

new = sorted(Sample_List,key = lambda x: x[-1])
print(new)

#6. Write a Python program to remove duplicates from a list.

list = [1,1,3,2,3,2,4,5]
list_updated =[]
for i in list:
    if i not in list_updated:
        list_updated.append(i)
print(list_updated)

#7. Write a Python program to clone or copy a list.

list = [1,1,3,2,3,2,4,5]
new_list = []
for i in list:
    new_list.append(i)
print(new_list)   

#8. Write a Python program to find the list of words that are longer than n from a given list of words.

list = ["kara", "karan", "aadi", "AAditya", "sam", "aniket", "himanshu"]
n =int(input("Enter the vlue of n: "))
new_list = []
for i in list:
    if len(i) > n:
        new_list.append(i)
print(new_list)

#              or

list = ["kara", "karan", "aadi", "AAditya", "sam", "aniket", "himanshu"]
n =int(input("Enter the vlue of n: "))
new_list = [name for name in list if len(name) > n]
print(new_list)

#9. Write a Python function that takes two lists and returns True if they have at least one common member.

list1 = [1,2,3,4,5,6]
list2 = [2,5,7,9]
def check_common_in_list(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False    
print(check_common_in_list(list1, list2))

#10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
   #Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
   #Expected Output : ['Green', 'White', 'Black']

Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
idx = [0,4,5]
remove = []
for i in idx:
    remove.append(Sample_List[i])

print(set(Sample_List) - set(remove))    

#      or 

Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
idx = [0,4,5]
remove = []
for i in idx:
    remove.append(Sample_List[i])

Sample_List = list(filter(lambda x: x not in remove, Sample_List))
print(Sample_List)

#11. Write a Python program to generate all permutations of a list in Python.

from itertools import permutations  # noqa: E402

numbers = [1,2,3]

perms = list(permutations(numbers))

for p in perms:
    print(p)

#12. Write a Python program to get the difference between the two lists.

A_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
B_List = ['Red', 'Green', 'White', 'Pink']

print(set(A_List) - set(B_List))

#        or 

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

diff1 = list(set(list1).difference(set(list2)))  # Elements in list1 but not in list2
diff2 = list(set(list2).difference(set(list1)))  # Elements in list2 but not in list1

print("Elements in list1 but not in list2:", diff1)
print("Elements in list2 but not in list1:", diff2)

#13. Write a Python program to append a list to the second list.

list_1 = [1, 2, 3, 4, 5]
list_2 = [6,7,8]
for i in list_2:
    list_1.append(i)
print(list_1)

#        or

list_1 = [1, 2, 3, 4, 5]
list_2 = [6,7,8]
list_1.extend(list_2)
print(list_1)

#14. Write a python program to check whether two lists are circularly identical.

def are_circularly_identical(list1, list2):
    return len(list1) == len(list2) and str(list2) in str(list1 + list1)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]
list3 = [2, 3, 4, 1]

print(are_circularly_identical(list1, list2))  # True
print(are_circularly_identical(list1, list3))  # True
print(are_circularly_identical(list1, [4, 3, 2, 1]))  # False

#15. Write a Python program to find common items from two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [x for x in list1 if x in list2]
print(list3)

#16. Write a Python program to split a list based on first character of word.

def split_by_first_char(words):
    grouped_words = {}
    for word in words:
        first_char = word[0].lower()
        if first_char not in grouped_words:
            grouped_words[first_char] = []
        grouped_words[first_char].append(word)
    return grouped_words

words_list = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado", "carrot"]
result = split_by_first_char(words_list)

print(result)

#17. Write a Python program to remove duplicates from a list of lists.
 #Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
 #New List : [[10, 20], [30, 56, 25], [33], [40]]

def remove_duplicates(lst):
    # Convert each inner list to a tuple (to make it hashable)
    unique_lists = set(map(tuple, lst))
    
    # Convert back to list of lists
    return [list(item) for item in unique_lists]

# Sample List
sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Remove Duplicates
new_list = remove_duplicates(sample_list)

print("New List:", new_list)