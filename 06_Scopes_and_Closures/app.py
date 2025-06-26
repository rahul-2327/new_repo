username = 'Rahul'

def func():
    # username = "Rahul Kumar"
    print(username)
    return

print(username)
func()

x = 12

def func2(y):
    z = x+y
    return z

print(func2(3))

def func3():
    global x
    x = 9
    return

# func3()
print(x)

def f1():
    # x = 88
    def f2():
        print(x)
    f2()
    return

f1()