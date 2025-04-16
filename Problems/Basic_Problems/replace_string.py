'''
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with User Name'''

UserName = input("Enter Your Name:")

string = "Hello {a}, How are you?".format(a = UserName) # can also use f string here

if len(UserName) < 3:
    print("Username length is less than 3")
else:
    print(string)