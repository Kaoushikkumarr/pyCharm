''' To check the type of declaration\
    we need to run code of 'terminal' not on 'python console\
     just type mypy file_name.py on the terminal'''


def func(x:int, y:int) -> str:
    return x + y
print(func(8,3))

''' Adding 'str and 'int on return type. '''
def func(x, y) :
    # return x + y
    return 'Hi, Kaoushik!'
print(func(8,"Kumar"))


def func(x, y) -> int:
    return x/y
print(func(8,3))
