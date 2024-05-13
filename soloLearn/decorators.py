##decorators are functions that modify other functions

#IDK HOW THIS WORKS

def print_text():
    print("Hello world!")

@print_list
def decor(func):
    print("~~~~~~~~~~~~~~~")
    func()
    print("~~~~~~~~~~~~~~~")