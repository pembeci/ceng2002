
def describe(name, gender="female", country="Turkey", age=25, *hobbies):
  print("{} is a {} year old {} from {}".format(name,age,gender,country))
  print("{} hobbies are:".format("His"))
  for h in hobbies:
    print(h)
  
def f(x,y):
  return x*y
    
def my_max(*nums):
   result = nums[0]
   for n in nums[1:]:
     if n>result: result = n
   return result
      
    
describe("Maria", "female", "Spain", 39, "Swimming", "Books", "Movies")    

def select_sql(table, filters, *columns):
  result = "SELECT {} FROM {}".format(", ".join(columns) ,table)
  # print(filters)
  # print(filters.items())
  # print([ t[0] + "=" + repr(t[1]) for t in filters.items()])
  filter_strs = [ t[0] + "=" + repr(t[1]) for t in filters.items()]
  return result + "\n    WHERE " + " AND ".join(filter_strs)
  
d = {"f1": 5, "f2": 7, "f10": "izzet"}  
print(select_sql("Book", d, "author", "price", "year"))

def select_sql2(table, *columns, **filters):
  result = "SELECT {} FROM {}".format(", ".join(columns) ,table)
  print(filters)
  print(filters.items())
  print([ t[0] + "=" + repr(t[1]) for t in filters.items()])
  filter_strs = [ t[0] + "=" + repr(t[1]) for t in filters.items()]
  return result + "\n    WHERE " + " AND ".join(filter_strs)
  
print(select_sql2("Book", "author", "price", "year", 
                       publisher="Iletisim", author="Orhan Pamuk", year=1996))

def describe2(name, gender="female", country="Turkey", age=25, *hobbies, **visits):
  print("{} is a {} year old {} from {}".format(name,age,gender,country))
  print("{} hobbies are:".format("His"))
  for h in hobbies:
    print(h)
  for (country, year) in visits.items():  
    print("Visited {} in {}".format(country, year))

describe2("Maria", "female", "Spain", 39, "Swimming", "Books", "Movies", 
            Turkey=2013, Japan=1998, USA=2001) 
 
