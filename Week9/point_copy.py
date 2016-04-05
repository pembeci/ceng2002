from copy import copy, deepcopy

class Point3D:
  def __init__(self, x,y,z):
      self.x = x
      self.y = y
      self.z = z 
      
  def __repr__(self):
     return "({0},{1},{2})".format(self.x, self.y, self.z)
      
  def addWithPoint(self, otherPoint):
      result = Point3D(self.x + otherPoint.x, 
                   self.y + otherPoint.y, 
                   self.z + otherPoint.z)
      return result   
      
  def __add__(self, otherPoint):
      result = Point3D(self.x + otherPoint.x, 
                   self.y + otherPoint.y, 
                   self.z + otherPoint.z)
      return result                 
      
  def scaledBy(self, scaleFactor):
      return Point3D(self.x * scaleFactor, self.y * scaleFactor, self.z * scaleFactor)     

  def __mul__(self, scaleFactor):
      # print("Multiplication, point is at left")
      return scaleFactor * self  # calls __rmul__ for same point (same self object)
      # return Point3D(self.x * scaleFactor, self.y * scaleFactor, self.z * scaleFactor)     

  def __rmul__(self, scaleFactor):
      # print("Multiplication, point is at right")
      # return self * scaleFactor
      return Point3D(self.x * scaleFactor, self.y * scaleFactor, 
                     self.z * scaleFactor)     

class Rectangle:
    def __init__(self, top_left, bottom_right, color, width):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.color = color
        self.border_width = width
        
    def __repr__(self):
        return "A {} with TP:{} BR:{} W:{})" \
                 .format(self.color, self.top_left, self.bottom_right, self.border_width)

    def area(self):
        return (self.bottom_right.x - self.top_left.x)*  \
            (self.top_left.y - self.bottom_right.y) 
	 

		
pt1 = Point3D(0,5,0)
pt2 = Point3D(7, 0, 0)

rect1 = Rectangle(pt1,pt2,"red", 3)
print("Initially:\nrect1={}\n".format(rect1))
# assignment by reference
rect2 = rect1

rect2.top_left.y = 20
rect2.color = "green"
rect2.border_width = 7
print("rect1={}\nrect2={}\n".format(rect1, rect2))

# shallow copy
rect3 = copy(rect1)

rect3.top_left.y = 40
rect3.color = "blue"
rect3.border_width = 9
print("rect1={}\nrect3={}\n".format(rect1, rect3))

# deep copy
rect4 = deepcopy(rect1)

rect4.top_left.y = 60
rect4.color = "pink"
rect4.border_width = 11
print("rect1={}\nrect4={}\n".format(rect1, rect4))
 