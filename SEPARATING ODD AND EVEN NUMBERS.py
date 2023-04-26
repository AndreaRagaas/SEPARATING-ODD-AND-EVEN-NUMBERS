#opening the numbers file
my_file = open("numbers.txt","r")

#creating two files separating the odd and even numbers
numbers = [int(line.strip()) for line in my_file.readlines()]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

#write odd numbers to odd.txt
with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")

#write even numbers to even.txt
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

#creating the header
print("WELCOME TO ODD AND EVEN NUMBERS PROGRAM")

#creating options
print("Main Menu")
print("1.Odd Numbers")
print("2.Even Numbers")
print("3.Exit")