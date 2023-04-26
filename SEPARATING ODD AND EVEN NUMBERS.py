#opening the numbers file
my_file = open("numbers.txt","r")

#creating two files separating the odd and even numbers
numbers = [int(line.strip()) for line in my_file.readlines()]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]