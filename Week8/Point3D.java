/**
 * Auto Generated Java Class.
 */
public class Point3D {
  
  public int x,y,z;
  
  public Point3D(int a, int b, int c) { 
    x = a;
    y = b;
    z = c;
  }
  
  public String toString() {
    String y = "why high one why";
    String s = "(" + x + "," + this.y + "," + z + ")";
    return s;
  }
  
  public Point3D addToPoint(Point3D otherPoint) {
    Point3D result = new Point3D(this.x + otherPoint.x,  
                                 this.y + otherPoint.y,
                                 this.z + otherPoint.z);
    return result;
  }
  
  public Point3D scaleBy(int scaleFactor) {
    return new Point3D(this.x * scaleFactor,  
                                 this.y * scaleFactor,
                                 this.z * scaleFactor);
  }
  public static void main(String[] args) { 
  
    Point3D pt1 = new Point3D(2,4,-2);
    Point3D pt2 = new Point3D(1,5,3);
    System.out.println("When you add " + pt1 + " and " + pt2 +
                       " the result is: " + pt2.addToPoint(pt1));
    System.out.println(pt1 + " scaled by 3 is " + pt1.scaleBy(3));
  }
  
  
  
}
