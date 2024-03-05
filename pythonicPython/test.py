global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)

def global_var_func2(n: int):
    global_var = global_var
    for i in range(n):
        global_var += i
        print(global_var)

global_var_func1(10)
global_var_func2(10)