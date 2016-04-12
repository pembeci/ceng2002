/**
 * Auto Generated Java Class.
 */
public class User implements Cloneable {
  
  public int id;
  public String name;
  public Department dept;
  
  public User(int i,String n) {
    this.id = i;
    this.name = n;
    this.dept = null;
  }
  
  
  protected Object clone() throws CloneNotSupportedException {
      User cloned = (User) super.clone();
      cloned.dept = (Department) this.dept.clone();
      return cloned;
  } 
     
  public static void main(String args[]) throws CloneNotSupportedException {
    int b = 5;
    int a = b;
    b = 6;
    System.out.println("a=" + a);
    int[] arr2 = { 1,2,3,4,5 };
    int[] arr1 = arr2;
    arr2[1] = 200;
    System.out.println("arr1[1]=" + arr1[1]);
    
    Department ceng = new Department(17, "CENG");
    
    User u2 = new User(6, "izzet");
    u2.dept = ceng;
    User u1 = u2;
    ceng.code = "CS";
    u2.id = 9;
    System.out.println("u1.id=" + u1.id);
    System.out.println("u1.dept.code=" + u1.dept.code);
    System.out.println("u1" + u1);
    System.out.println("u2" + u2);
    
    
    User u4 = new User(6, "izzet");
    u4.dept = new Department(12, "CENG");
    User u3 = (User) u4.clone();
    u4.dept.code = "CS";
    u4.id = 9;
    System.out.println("u3.id=" + u3.id);
    System.out.println("u3.dept.code=" + u3.dept.code);
    System.out.println("u4.dept.code=" + u4.dept.code);
    System.out.println("u3" + u3);
    System.out.println("u4" + u4);
    System.out.println("u3.dept" + u3.dept);
    System.out.println("u4.dept" + u4.dept);
  }
}
