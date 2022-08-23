# str = "l love python programming"
# n = 0
# count = 0
# while n < len(str):
#     if str[n] == "o":
#         count = count + 1
#     n = n + 1
# print(count)
# enumerating a string
my_string = 'Hello World'
print(list(enumerate(my_string))) # prints [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'W'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]

# getting the length of a string
print(len(my_string)) # prints 11