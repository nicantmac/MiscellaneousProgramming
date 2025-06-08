num_lst = []

first_num = int(input("Enter a number: "))
num_lst.append(first_num)
print("Number successfully added.")

# Loop until 5 numbers (including the first one) are added
while len(num_lst) < 5:
    num_in = int(input("Enter a number: "))
    if num_in == 0:
        print("Please enter another number.")
    elif num_in in num_lst:
        print("Number already exists inside the list. Try again.")
    else:
        num_lst.append(num_in)
        print("Number successfully added.")

print("Final list of numbers:", num_lst)

highest_num = num_lst[0]

for num in num_lst:
    if num > highest_num:
        highest_num = num

print("The highest number in the list is:", highest_num)
