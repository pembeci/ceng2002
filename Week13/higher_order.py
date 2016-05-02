from random import randint, choice

def print_pts(pts):
  for pt in pts:
    print("x:{} y:{} color:{}".format(pt["x"],pt["y"],pt["color"]))
    
points = []
colors = ["red", "green", "pink", "blue", "orange"]
for i in range(30):
  pt = { "x": randint(1,7), "y": randint(1,7), "color": choice(colors) }
  points.append(pt)
  
print_pts(points)  

def color_of_point(pt):
   return pt["color"]

def is_point_red(pt):
   return pt["color"] == "red"
      
colors = map(color_of_point, points)
print(colors)

red_points = filter(is_point_red, points)
print("Red points")
print_pts(red_points)  

print("Points with x>5")
print_pts(filter(lambda pt: pt["x"] >5, points))

print("Points sorted somehow??")
print_pts(sorted(points))

sorted([6,9,-2,1,7,8])
sorted([6,9,-2,1,7,8], reverse=True)
teams = "fener cimbom trabzon besiktas kartal mugla".split(" ")
sorted(teams)

print("Points sorted by x")
print_pts(sorted(points[:12], key=lambda pt: -pt["x"]))

print("Points sorted by color first and then difference between x,y")
print_pts(sorted(points, 
                 key=lambda pt: (pt["color"], abs(pt["x"]-pt["y"]), pt["y"])) )
                 
# if you want to sort in-pace use sort method

points.sort(key=lambda p: p["color"])                 
print_pts(points) # sorted

# functions being first-class values

f = color_of_point
print(f(points[0]))
my_functs = [f, is_point_red]
print(my_functs[1](points[-2]))

print("Testing functions as return values")
def add_with(x):
  def g(y):
    return x+y
  return g
 
add5 = add_with(5)
print(add5(12)) 

# List comprehensions in Python
# actually map and filter are not used in Python 
# since we have list comprehensions

# colors = map(lambda pt: pt["color"], points)
colors = [pt["color"] for pt in points]
print(colors)
new_points = [ pt for pt in points if pt["color"]=="green" and pt["x"]<=4  ]
print_pts(new_points)

vals = "A B C F E D".split()
pairs = []
for v1 in vals:
  for v2 in vals:
    if v1 != v2 and v1 < v2:
       pairs.append( (v1,v2) )
    
print len(pairs), " pairs produced:", pairs    

pairs = [ (v1,v2) for v1 in vals for v2 in vals 
                    if v1 != v2 and v1 < v2
        ]
print len(pairs), " pairs produced:", pairs 
        
max_value = 200

pyth_triples = [ (a,b,c) for a in range(1,max_value+1) \
                          for b in range(1,max_value+1) \
                           for c in range(1,max_value+1) \
                            if a<b and a**2+b**2 == c**2 ]                                       
print "All pyth triples: ", pyth_triples              
   
def multiple_of(t1, t2):
  if t1 == t2: return False
  a1 = float(t1[0])
  a2 = float(t2[0])
  b1 = float(t1[1])
  b2 = float(t2[1])

  return a1/a2 == b1/b2 
  
  
print "Original pyth triples", \
      [t1 for i,t1 in enumerate(pyth_triples) \
           if all(not multiple_of(t1,t2) for t2 in pyth_triples[:i]) ]

                        


  









































