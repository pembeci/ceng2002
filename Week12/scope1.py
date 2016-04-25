
def f():
    global b
    a = "local_f_a"
    b = "local_f_b"
    c = "local_f_c"
    print("print in f: a = ", a)
    f_num = 20
    f_nums = [20,20,20]
    g(num, nums, f_num, f_nums)
    print("print in f: c = ", c)
    print("What happened:",num, nums, f_num, f_nums)
    def h():
        nonlocal c
        c = "value in h"
        print("print in h: c = ", c)
        print("print in h: d = ", d)
    h()
    print("print in f: c = ", c)



def g(arg1,arg2,arg3,dd):
    global c, d
    print("print in g: ", c)
    c = 123
    print("print in g: ", c)
    arg1 += 1
    arg2[0] = "new"
    arg3 += 100
    dd[1] = "new"

num = 10
nums = [10,10,10]
a ="global_a"
b ="global_b"
c ="global_c"
d = "global_d"
f()
print("print in global: a = ", a)
print("print in global: b = ", b)
print("print in global: c = ", c)
print("print in global: d = ", d)



