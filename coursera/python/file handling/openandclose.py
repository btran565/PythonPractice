import os

print(os.getcwd()) 
file = open("sample.txt", mode = 'r')

data = file.readline()

print(data)

file.close()
