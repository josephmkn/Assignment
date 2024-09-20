
##Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable ##
# _Integer = 1
# _Float = 1.0
# _String = '1'
# print(_Integer , _Float , _String)
# print(_Integer , type(_Integer))
# print(_Float , type(_Float))
# print(_String , type(_String))

##Redeclare the same variable as another number.(2,2.0 and ‘2’) and share your observation on result.
# _Integer = 2
# _Float = 2.0
# _String = '2'
# print(_Integer , _Float , _String)
# print(_Integer , type(_Integer))
# print(_Float , type(_Float))
# print(_String , type(_String))


## Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c..
# a=b=c = 10
# print(a , b)
# print(c)

##Assign two variables a and b as integer and print the sum of a+b.
# a =5
# b=10
# print(a+b)

##Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(fruits)

##How do you access the second and fourth elements from the list.
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(fruits[1],fruits[3])

##Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.
# numbers = [10, 20, 30, 40, 50]
# numbers[2] = 35
# print(numbers)

##How do you create a tuple with the following elements: "red", "green", "blue"?
# colors = ("red", "green", "blue")
# print(colors)

##How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?
# colors = ("red", "green", "blue", "yellow")
# print(colors[0], colors[-1])

##What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?
# colors = ("red", "green", "blue")
# colors[1] = "yellow"
# print(colors) ## tuple cant be modified


##Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.
# coordinates = (10, 20, 30)
# x = coordinates[0]
# y = coordinates[1]
# z= coordinates[2]
# print(x)
# print(y)
# print(z)


##Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").
# colors = ("red", "green", "blue")
# findcolor = "blue"
# result = findcolor in colors
# print("Element BLUE is present in the tuple colors : ",result)


##Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").
# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print(len(days))

##Create a dictionary where the keys are student names and the values are their grades
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print(students)

##How do you access Bob's grade from the dictionary students
# print(students["Bob"])

##Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary
# students["David"] = 92
# print(students)
# students.pop("Charlie")
# print(students)

##Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# students.update({"Bob" : 95})
# print(students)

##Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
# keycheck = "Alice" in students
# print("Alice exist in the dictonary : ",keycheck)

# ##Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
# print(len(students))
