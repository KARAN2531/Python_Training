#Sets 

#1. Write a Python program to create a set.

my_set = {1, 2, 3, 4, 5}
print(my_set)  

#2. Write a Python program to iteration over sets.

my_set = {10, 20, 30, 40}
for item in my_set:
    print(item)

#3. Write a Python program to add member(s) in a set.

my_set = {1, 2, 3}
my_set.add(4)  
my_set.update([5, 6, 7])  
print(my_set)  

#4. Write a Python program to remove item(s) from set

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  
my_set.discard(2)  
print(my_set) 

#5. Write a Python program to remove an item from a set if it is present in the set.

my_set = {1, 2, 3, 4}
if 3 in my_set:
    my_set.remove(3)
print(my_set)  

#6. Write a Python program to create an intersection of sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print(intersection_set) 

#7. Write a Python program to create a union of sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  

#8. Write a Python program to create set difference.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2, 5} (Elements in set1 but not in set2)


#9. Write a Python program to create a symmetric difference.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Output: {1, 2, 5, 6} (Elements in either set1 or set2 but not both)

#10. Write a Python program to clear a set.

my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)  

#11. Write a Python program to use of frozensets.

my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset) 

# my_frozenset.add(5)  # This will raise an AttributeError since frozensets are immutable

#12. Write a Python program to find maximum and the minimum value in a set.

my_set = {10, 20, 5, 8, 30}
max_value = max(my_set)
min_value = min(my_set)
print("Max:", max_value)  
print("Min:", min_value) 
