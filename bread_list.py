breads = ['white', 'wheat', 'croissant', 'sourdough', 'french']	#initializes list of bread
message = f"My favorite bread is {breads[2].title()}."	#message that prints bread at index 2

print(breads)

breads.append('dutch crunch') #adds dutch crunch at end
print(breads)	#prints new list

del breads[0]
print(breads)

print(message)