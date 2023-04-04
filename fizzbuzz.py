
count = int(input("Please enter an integer: "))

fizzbuzz_list = []

#Fizzbuzz
for number in range(count):
    if number == 0:
        fizzbuzz_list.append(number)
    elif number % 3 == 0 and number % 5 == 0:
        fizzbuzz_list.append("Fizzbuzz")
    elif number % 5 == 0:
        fizzbuzz_list.append("Fizz")
    elif number % 3 == 0:
        fizzbuzz_list.append("Buzz")
    else:
        fizzbuzz_list.append(number)

sum = 0
count_fizz = 0
count_buzz = 0
count_fizzbuzz = 0
for value in fizzbuzz_list:
    print(value)
    if value == "Fizzbuzz":
        count_fizzbuzz += 1
    elif value == "Fizz":
        count_fizz += 1
    elif value == "Buzz":
        count_buzz += 1
    elif type(value) == int:
        sum += value

print(f"The sum of all integers is {sum}\n")
print(f"The count of Fizzbuzz is {count_fizzbuzz}\n")
print(f"The count of Fizz is {count_fizz}\n")
print(f"The count of Buzz is {count_buzz}\n")
