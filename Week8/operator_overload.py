class Point3D:
  def __init__(self, x,y,z):
      self.x = x
      self.y = y
      self.z = z 
      
  def __str__(self):
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
                   
pt1 = Point3D(2,5,-1)
pt2 = Point3D(1, 8, 3)
pt3 = pt1.addWithPoint(pt2)
pt4 = pt1 + pt2

print("When you add " + str(pt1) + " and " + str(pt2) 
       + " then you get " + str(pt3))

print("When you add " + str(pt1) + " and " + str(pt2) 
       + " then you get " + str(pt4))
              
print("{} scaled by 3 is {}".format(pt1, pt1.scaledBy(3)))
print("{} scaled by 3 is {}".format(pt1, pt1 * 3)) # __mul__ is called because Point3d is the left operand
print("{} scaled by 3 is {}".format(pt1, 3 * pt1)) # __rmul__ is called because Point3d is the right operand               

"""
  For a full list of overlodable operators in Python see:
    https://docs.python.org/3/reference/datamodel.html#special-method-names
  If you find this official documentation's language too technical search for
  "Python special methods" or "Python operator overloading" for simpler tutorials
"""  

   
   
     

                   
