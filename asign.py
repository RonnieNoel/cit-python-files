# # 1. Print First 10 natural numbers using while loop.
num=1
while  num<11:
    print(num)
    num+=1
# # 2. Calculate the sum of all numbers from 1 to a given number.
# number = int(input("Enter a number of your choice"))

sum = 1
for num in range(0, number+1, 1):
    print(num)
    sum = sum+num


# # 3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...
number=int(input("enter a number of your choice: "))
limit=int(input("enter a limit of your choice: "))
for num in range(0, limit, 1):
    
    prod = num*number
    print(prod)

# 4. Write a program to display only those numbers from a list that satisfy the following conditions

# -. The number must be divisible by five
# -If the number is greater than 150, then skip it and move to the next number
# -If the number is greater than 500, then stop the loop
# # given `numbers = [12, 75, 150, 180, 145, 525, 50]`
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5!=0:
        continue
    if num>150:
        continue
    if num>500:
        break
    print(num)


# 5. Write a program to count the total number of digits in a number using a while loop. given number `4673453`

# # 6. Display numbers from -10 to -1 using while loop
number=-10

while  number<0:

    print(number)
    number+=1

