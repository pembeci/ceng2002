/**
 * Auto Generated Java Class.
 */
public class B {
  
  public static int objectsCreated = 0;
  public static int totalClicked = 0;
  public int clicked = 0; 
  public B() { 
    objectsCreated++;
    System.out.println("I am the " + objectsCreated + ". B created.");
  }
  
  public void click() {
    this.clicked++;
    totalClicked++;
    System.out.println("I am clicked " + this.clicked + " times.");
  }
  
  public static void main(String[] args) { 
    A a1 = new A();
    A a2 = new A();
    A a3 = new A();
    a2.click();
    a2.click();
    a3.click();
    A a4 = new A();
    a4.click();
    a1.click();
    B b1 = new B();
    B b2 = new B();
    b2.click();
    b2.click();
    b2.click();
    b1.click();
    System.out.println("Count of created objects of mine: " + objectsCreated);
    System.out.println("My objects clicked: " + totalClicked);
    System.out.println("Count of created objects of A: " + A.objectsCreated);
    System.out.println("Count of created objects of B: " + B.objectsCreated);
    System.out.println("A objects clicked: " + A.totalClicked);    
    System.out.println("B objects clicked: " + B.totalClicked);    
    
  }
  
  /* ADD YOUR CODE HERE */
  
}
