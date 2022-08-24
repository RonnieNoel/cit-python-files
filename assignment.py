# 1. Write a Python program to sum all the items in a list.
#     - The list should be generated using list comprehension
# #     - The size of the list should be from a user input

item=[int(input("enter the numbers here"))]
def sum_of_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_of_list(item))

# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : `['abc', 'xyz', 'aba', '1221']`
verbs = ["U", "Down", "Melon"]
count=0
for verb in verbs:
    if len(verb)>1:
        count=count+1
print(count)  
   
      # 3. Write a Python program to remove duplicates from a list, given list
#     `fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
for fruit in fruits:
    if fruits.count(fruit)>1:
        fruits.remove(fruit)
    else:
        print(fruits)   
