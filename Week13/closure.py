
def counter(init, step):
   count = init
   def f():
     nonlocal count
     count += step
     return count
   return f  


counter1 = counter(100,10)
counter2 = counter(10,-1)

print(counter1())
print(counter1())
print(counter2())
print(counter2())
print(counter1())
print(counter2())
