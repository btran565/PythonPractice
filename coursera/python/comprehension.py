data = [1,2,3,4,5,6,7,8,9,10]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:   #lements in this iterator object cannot be directly accessed and need the help of a for loop
    print(items, end=" ")