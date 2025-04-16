'''
15.Given a string columnTitle that represents the column title as appears in an
Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
'''

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

s = input("Enter your columnTitle: ")
list = []
for i in s:

    if i in letters:
        x = letters.index(i)
        y = numbers[x]
        list.append(y)
    else:
        print("Error occured!")    
output = "".join(str(element) for element in list)
print("output: ", output)