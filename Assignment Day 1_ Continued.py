##Write a Python program that takes two numbers as input from the user and performs the following operations:
from os.path import split
from random import sample

# _Number_A = float(input("Enter the number A : "))
# _Number_B = float(input("Enter the number B : "))
# print(("Addition : ",(_Number_A + _Number_B)),"\n",("Subraction : ",(_Number_A - _Number_B)),"\n",("Multiplication : ", (_Number_A * _Number_B)),"\n", ("Division : ",(_Number_A / _Number_B)),"\n",("Modules : " , (_Number_A % _Number_B)))

##Write a Python program that checks whether a given number is even or odd using the modulus operator.
# A_Number = float(input("Enter the number A : "))
# if round(A_Number,0) % 2 == 0:
#     print("Number is Even Number")
# else:
#     print("Number is odd Number")
# print(int(round(A_Number,0)))

##Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.
# x = float(input("Enter the number : "))
# if x <0:
#     print("Given number is negative")
# elif x >0:
#     print("Given Number is positive")
# elif x == 0:
#     print("Given number is Zero")
# else:
#     print("Not valid")

##Write a Python program that calculates the grade of a student based on the marks entered by the user
# y = float(input("Enter the number : "))
# if y >= 90:
#     print("Grading scale is A")
# elif y >= 80 and y <= 89:
#     print("Grading scale is B")
# elif y >= 70 and y <= 79:
#     print("Grading scale is C")
# elif y >= 60 and y <= 69:
#     print("Grading scale is D")
# else:
#     print("Grading scale is F")

##Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
# filename = "sample.txt"
# file = open(filename, 'w')
# file.write("Hello, this is a sample file created by joseph." "\n")
#
# file = open(filename, "a")
# file.write("Gurukul assignment" )
#
# file = open(filename, 'r')
# print(file.read())
#
# file.close()

##Write a Python program that reads a text file called data.txt and counts the number of words in the file.
# filename = "sample.txt"
# file = open(filename, "r")
# print(len(str(file)))

##Write a Python program to print the numbers from 1 to 10 using a for loop.
# for i in range(10):
#     print(i)

##Write a Python program to display the multiplication table of a number entered by the user using a for loop.
# multiplication = int(input("Enter the number : "))
# for i in range(1 , 11):
#     print(i, "*" , multiplication, "=", (i*multiplication))
