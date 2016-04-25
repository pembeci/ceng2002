/**
 * Auto Generated Java Class.
 */
public class ScopeTest {
  
  public static int b = 5;
  public int c = 100;
  
  public static void f() {
    String a = "aaaa";
    System.out.println("In function f: " + a);
    System.out.println("In function f: b=" + b);
    b = 5000;
  }  

  public void update() {
    c++;
    System.out.println("In function update: c=" + c);
  }

  public void update(int incr) {
    c += incr;
    System.out.println("In function update: c=" + c);
  }
  
  public static void g() {
    System.out.println("In function g: b=" + b);
  }  
  
  public static void main(String[] args) { 
    int a = 5;
    String b = "global_b";
    for (int i=0; i<5; i++) {
       // String a = "aaaa";
      a = 123;
      System.out.println(i);
    }
    f();
    System.out.println(a);
    g();
    // System.out.println(i);
    ScopeTest obj1 = new ScopeTest();
    obj1.update();
    obj1.update();
    obj1.update();
    ScopeTest obj2 = new ScopeTest();
    System.out.println("obj2.c=" + obj2.c);
    System.out.println("obj1.c=" + obj1.c);
    obj2.update();
    System.out.println("obj1.c=" + obj1.c);
    System.out.println("obj2.c=" + obj2.c);
    obj1.update(40);
    System.out.println("obj1.c=" + obj1.c);
    System.out.println("obj2.c=" + obj2.c);
    
  }
  
  /* ADD YOUR CODE HERE */
  
}
