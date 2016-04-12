
a = 10

def f(x,y):
    return 2*x + y

def g(x,y):
    global a
    a += 1    # side effect
    return 2*x + y

def h1(x):
    global a
    print("Hop")
    a += 1    # side effect
    return a*x

def h2(x):
    global a
    print("Hip")
    a -= 1    # side effect
    return a*x

def h3(x):
    global a
    a_local = a
    print("Hop")
    a_local += 1    # not a side effect, changing a local variable
    return a_local*x

def h4(x):
    global a
    a_local = a
    print("Hip")
    a_local -= 1    # side effect
    return a_local*x

def h5(x,a):
    print("Hop")
    a += 1    # not a side effect, changing a local variable
    return a*x

def h6(x,a):
    print("Hop")
    a -= 1    # not a side effect, changing a local variable
    return a*x

print(a)
print(f(1,2))
print(a)

print(a)
print(g(1,2))
print(a)

print("Calling h1 and h2")
# print(h2(5) + h1(10))
# print(h1(10) + h2(5))
# print(h3(10) + h4(5))
#
print(h6(5,a) + h5(10,a))

global_nums = [1,2,3,4]

def h7(x):
   global global_nums
   local_nums = global_nums
   local_nums[0] *= 10
   return x * local_nums[0]

def h8(x, nums):
   nums[0] *= 10
   return x * nums[0]