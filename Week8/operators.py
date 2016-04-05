
a = 0
if (a!=0 and 10/a < 5): 
   print("TRUE");  
else:
   print("FALSE");
   
if (3<5  or vdfvdf < 10):
     print("TRUE");
	 
num = 12

result = num or 3<5
print("RESULT=",result)
result = 3<5 or num
print("RESULT=",result)
result = num and 3<5
print("RESULT=",result)

result = num and 3<1
print("RESULT=",result)

result = "abc" and [1,2] and [] and 3 < 5 
print("RESULT=",result)

result = "" or [1,2] or [] or 3 < 5 
print("RESULT=",result)

result = "" or 5 < 10 or [] or 3 < 5 
print("RESULT=",result)

# those two are equivalent
a = a or 20
if (a==0): a=20

a = 5 or (1/0)                       # a is now ...
print("a =",a)
a = (0 or "abc") and (0 or "")       # a is now ...
print("a =",a)
a = (0 or "") and (0 or "abc")       # a is now ...
print("a =",a)
a = ("" or []) and ("abc" or 0)      # a is now ...
print("a =",a)
a = 0 or "abc" or [1,2]              # a is now ...
print("a =",a)
a = [] or (5 and [1,2]) or "xyz"
print("a =",a)



num = int(input("Give me number: "))
a = num * 10
print(a)