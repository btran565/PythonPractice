#(print("How old are you?:")
#print("Age: ")
#(num:=int(input()))
#print("Your age is "+str(num)+"!")
"""
this is a docstring
for i in range(0,20,2):
	print(i)

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
"""

file = open("testnumbers.txt")
#print(file.readlines())
for line in file:		#traverses file lines
	print(line)
file.close()

try:
	print("I'm gonna divide by zero")
	print(1/0)
except ZeroDivisionError:
	print("Wow it didn't work thats crazy")
finally:
	print("This code will run no matter what")