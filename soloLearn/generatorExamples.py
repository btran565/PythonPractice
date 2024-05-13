#generator
mylist = [1,2,3,4,5]
def gen(list):
    for i in range(len(list)):
        yield list[i] * 2       ##returns each element after generator calculations

for item in mylist:             ##prints mylist
    print(item, end=' ')
print(' ')

for item in gen(mylist):        ##prints generator outputs, should be 2 4 6 8 10
    print(item, end=' ')
print('')