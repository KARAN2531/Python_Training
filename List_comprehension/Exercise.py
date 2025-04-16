'''
1. Filter only negative and zero in the list using list comprehension
'''

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
res = [ i for i in numbers if i<1]
print(res)

'''
2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for row in list_of_lists for list in row for number in list]
print(flattened_list)

'''
3. Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

'''

output = [(i, *[i**j for j in range(6)]) for i in range(11)]
for item in output:
    print(item)

'''
4. Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for (country, capital) in sublist]

print(output)

'''
5. Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
'''

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for (country, city) in sublist]

print(output)

'''
6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

'''

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f"{country} {city}" for sublist in names for (country, city) in sublist]
print(output)

'''
7. Write a lambda function which can solve a slope or y-intercept of linear functions.
'''

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else None  # noqa: E731

y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1 if slope(x1, y1, x2, y2) is not None else None  # noqa: E731

x1, y1 = 1, 2
x2, y2 = 4, 8

m = slope(x1, y1, x2, y2)
b = y_intercept(x1, y1, x2, y2)

print(f"Slope: {m}")
print(f"Y-Intercept: {b}")