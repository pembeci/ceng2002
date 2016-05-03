
nums = [7,2,9,11,8,5]

r = reduce(lambda x,y: x+y, nums, 100)
print r

init = { "odd": [], "even": [] }

def f(partial, num):
  print partial, num
  if num%2==0:
    partial["even"].append(num)
  else:
    partial["odd"].append(num)  
  return partial
  
print (reduce(f,nums,init))    
