---
layout: default
---

# Midterm Examples

## Expressions

* Operator [precedence](en.wikipedia.org/wiki/Order_of_operations) and [associativity](http://en.wikipedia.org/wiki/Operator_associativity)

{:.q}
> Q: Let's suppose that in Language A every operator is left associative but in Language B every operator is right associative. Moreover, in language A `+` has higher precedence than `-` but in language B the situtation is the opposite. For other operators the usual rules apply. For every expression below give their value both in languages A and B.
>
> Expression | Language A | Language B
-----------|:----------:|:----------:
`10 - 5 + 3`   |            |
`100 / 20 / 5` |            |
`19 + 5 - 2 + 7 % 3 / 10 * 10` |            |

{:.q}
> Q: For expression `(a+b)%c*d` draw the corresponding [expression tree](http://en.wikipedia.org/wiki/Binary_expression_tree).

{:.q}
> Q: For the following expression tree, give the corresponding expression. Additionally, show step by step how this tree will be
reduced to calculate the expression's value.
>
> ![exp-tree](http://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Exp-tree-ex-11.svg/239px-Exp-tree-ex-11.svg.png){:height="160"}
> {:align="center"}

* Conditional Expressions

{:.q}
> Q: Write the value of `a` after each line and give an equivalent Python [conditional expression](https://docs.python.org/2.5/whatsnew/pep-308.html):
> {% highlight javascript linenos %}
var x=5, y=8, a;
a = x>y ? "yes" : (y%2 == 0 ? "no" : "may be")
a = x<y ? "yes" : (y%2 == 0 ? "no" : "may be")
a = x==y ? "yes" : (x%2 == 0 ? "no" : "may be")
{% endhighlight %}

{:.q}
> Q: Give the JS equivalent of the following Python code:
> {% highlight python linenos %}
a = 5 if x>y else (4 if x<y else 3)
{% endhighlight %}

{:.q}
> Q: Rewrite the following function by replacing all conditional statements by conditional expressions:
> {% highlight python linenos %}
def f(x,y):
    if x>y: a = x
    else: a = y
    if a>0: return g(a*2)
    else: return g(a/4)
{% endhighlight %}


## Types

### Type Casting

{:.q}
> Q: Sometimes PLs cast a value into another type *implicitly* (automatically, without programmer's explicitly stating to do so) to make some expression's type correct. Find such implicit type castings in the following JS code. Explain each like "in line 7 variable x was cast from string to int".
>
> {% highlight javascript linenos %}
var a = 5, s = "123", x = [3,4,5];

function f(p1, p2) {
  p1 = p1 || 7;
  if (p2) {
    // do something
  }
}

alert("My array is: " + x);
f(a,x);
console.log(a*s);
console.log(s+a);
{% endhighlight %}

{:.q}
> Q: Give values for variables `a` and `b` such that in JS `a == b` is `true` but `a === b` is `false`.

{:.q}
> Q: Give two different values for `a` such that either the `if` part or `else` part will be executed. Explain shortly
how the code runs in both cases.
> {% highlight javascript %}
var a = ...
var first = a && a[0]
if (first) console.log(first)
else console.log("array is empty")
{% endhighlight %}

### Lazy Evaluation in Booleans

{:.q}
> Q: For boolean expressions, Python and Javascript use lazy evaluation (or sometimes called short circuting in this context). See this [discussion](http://stackoverflow.com/questions/13960657/does-python-evaluate-ifs-conditions-lazily). Give the value of `a` after each line in the following Python code:
>
> {% highlight python linenos%}
a = 5 or (1/0)                       # a is now ...
a = (0 or "abc") and (0 or "")       # a is now ...
a = (0 or "") and (0 or "abc")       # a is now ...
a = ("" or []) and ("abc" or 0)      # a is now ...
a = 0 or "abc" or [1,2]              # a is now ...
a = [] or (5 and [1,2]) or "xyz"     # a is now ...
{% endhighlight %}


## Scope

{:.q}
> Q: Give the console output of the following code snippet. Recall that, in Javascript `var` keyword creates a new local variable in the current scope:
>
> {% highlight javascript %}
var x=1, y=2, z=3;
                                                       //
function f() {
  var y = 4;
  z = 5;
  console.log("f1", x, y, z)
  g(x,y)
  console.log("f2", x, y, z)
  h(11,12);
  console.log("f3", x, y, z)
}
                                                       //
function g(a,b) {
  var x = 6;
  console.log("g1", x, y, z);
  function h(y,z) {
    console.log("h1", x, y, z);
    x = 7;
    z = 8;
    console.log("h2", x, y, z);
  }
  h(y,z);
  console.log("g2", x, y, z);
}
                                                       //
function h(y,z) {
    console.log("h3", x, y, z);
    x = 9;
    z = 10;
    console.log("h4", x, y, z);
}
                                                       //
console.log("global", x, y, z)
f()
console.log("global", x, y, z)
{% endhighlight %}

{:.q}
> Q: Try to achieve the same output of the previous question by writing an equivalent code in Python. Note that, unlike Javascript, in Python global variables are not automatically accessable in local scopes. You need to use the `global` keyword to make them available.

## Assignment Semantics

{:.q}
> Q: Give the values of each local variable in function `f` at the end of its execution (i.e. the output of the print statements at the end):
>
> {% highlight python %}
def f():
a = [ 3, {'x':3, 'y':4}, [1,2,3], (10,20), "xyz" ]
b = a
    c = b[:]              # shallow copy
    (a0,a1,a2,a3,a4) = a  # equivalent of a0=a[0], a1=a[1] ... a4=a[4]
    a5 = a[2][:]
    a2.append("new")
    c[0] = 30
    c[1]['x'] = 40
    a[4] = "hello"
    a[0] = 50
    a3 = "world"
    for (k,v) in locals().items():
    print("{0} = {1}".format(k,v))
    #
f()
{% endhighlight %}

{:.q}
> Q: What will be the output of the following code:
>
> {% highlight python %}
a = [1,2,3]
b = a
c = [1,2,3]
print(a==c)
print(a is b)
print(a is c)
a.append(4)
print(a==c)
print(a is b)
b = [1,2,3,4]
print(a == b)
print(a is b)
{% endhighlight %}

{:.q}
> Q: What will be the output of the following code:
>
> {% highlight javascript %}
a = [1,2]
b = [1,2]
c = a
console.log(a == b)
console.log(c == a)
d = {'x':0}
e = {'x':0}
console.log(d == e)
console.log(d.x == e.x)
{% endhighlight %}


## Functions

* Argument Passsing

{:.q}
> Q: What will be the value of global variables `x1,x2,x3,x4,x5` at the end of
this code (i.e. after call to `f` returns):
>
> {% highlight javascript %}
function g(a40, a41, a,b,d,e) {
    a40.push(50);
    a41 += "ghi"
    a *= 10
    b.c *= 10
    b.f += "ghi"
    d.push(50);
    e += "ghi"
}
function f(a1,a2,a3,a4,a5) {
    a1 *= 10;
    a2 += "def";
    a3.push(40);
    a4[0].push(40);
    a4[1] += "def";
    a5.a *= 10;
    a5.b.c *= 10;
    a5.b.f += "def";
    a5.d.push(40);
    a5.e += "def";  
    g(a4[0],a4[1],a5.a, a5.b, a5.d, a5.e)
}
var x1 = 1
var x2 = "abc"
var x3 = [1,2,3]
var x4 = [ [1,2,3], "abc" ]
var x5 = { 'a':1, 'b': {'c': 2, 'f':"abc"}, 'd': [1,2,3], 'e': "abc"}
f(x1,x2,x3,x4,x5);
// print the values of x1,x2,x3,x4,x5 at this point
{% endhighlight %}

* Default arguments

{:.q}
> Q: What will be the output of the following JS code:
>
> {% highlight javascript %}
function f(a,b,c,d) {
    if (b == undefined) b = 5;
    c = c || 10;
    d = d || 20;
    console.log([a,b,c,d]);
}
f(1)
f(1,2)
f(1,2,3,4)
f(0,0,0,0)
{% endhighlight %}

* Python \*args, \*\*kargs

{:.q}
> Q: What will be the output of the following Python code:
>
> {% highlight python %}
def f(a, b=10, c=20, *args, **kargs):
    d = args[2] if len(args)>2 else 40
    # if key "x" exists in kargs dict returns its value (kargs["x"]), otherwise returns default value 40
    e = kargs.get("x",50)
    print("a={}, b={}, c={}, d={}, e={}".format(a,b,c,d,e))
    #
f(1,2)
f(1,2,3,4)
f(1,2,3,4,5,x="x")
f(1,2,3,4,5,6,7)
{% endhighlight %}

{:.q}
> Q: Write the equivalent of the following Python function in Java and Javascript. Note
that in Javascript arguments array includes all the arguments passed (i.e. will include
`k` at index 0 and `inc` at index 1 if you include them in function parameters). In Java,
you can pass variable length arguments as an array as well:
[example1](http://www.deitel.com/articles/java_tutorials/20060106/VariableLengthArgumentLists.html),
[example2](http://viralpatel.net/blogs/varargs-in-java-variable-argument-method-in-java-5/).
>
> {% highlight python %}
def f(k, inc, *args):
    sum = 0
    for num in args:
    sum += num * k
    k += inc
    return sum
    #
print(f(5,3,4,1,2))  # 50 = 4*5 + 1*(5+3) + 2*(5+3+3)
{% endhighlight %}

* Functions as first class values

  If functions are first class values in a PL you can do use them as other value types like integer.
  For instance:

  - Store them in variables: `var f = function(){}`
  - Pass them to other functions as arguments
  - Return them from functions
  - Construct a list of functions or use them as values in objects  

{:.q}
> Q: What will be the output of the following Javascript code:
>
> {% highlight javascript %}
var x = 30;
function f1(a) {
    return a+10;
}
var f2 = function (b) {
    return b+x;
}
function f3(a,b) {
    return function(x) {
        return x+a+b;
    }
}
funcs = [function(c) {return c+20}, f1, f3(3,4), f2]
var f4 = funcs[0];
funcs.push(f4);
for (i=0; i<funcs.length; i++) {
    console.log(funcs[i](3))
}
{% endhighlight %}

* Closures

  Let's suppose that some function (let's call it outer) defines a function (inner)
  and then returns it. If the inner function references a local variable in outer function
  then those variables should't be destroyed as what normally happens. If they were destroyed,
  when the returned inner function is called its code will not be able to use them.
  So for such cases those local variables are kept (as a closure of the inner function)
  but they are only available to the inner function.

{:.q}
> Q: What will be the output of the following Javascript code:
>
> {% highlight javascript %}
function outer(start) {
  var end = 20;
  var inner = function() {
    start++;
    end--;
    console.log("start=" +start + " end=" +end);
  }
  return inner;
}  
                                                    //
var f1 = outer(5)
f1();f1();f1()
var f2 = outer(1)
f2();f2();
f1();
f2();
{% endhighlight %}

* Higher Order Functions (map, filter, reduce, sort)

{:.q}
> Q: Give the output of the following Javascript code and write the corresponding code
in Python.
>
> {% highlight javascript %}
var teams = [
  { name: "HataySpor", "wins": 3, "draws": 2, "losses": 1},
  { name: "HataySporrr", "wins": 3, "draws": 2, "losses": 1},
  { name: "Karabük", "wins": 4, "draws": 0, "losses": 1},
  { name: "Muğlaspor", "wins": 7, "draws": 1, "losses": 0},
  { name: "UlaGücü", "wins": 1, "draws": 3, "losses": 0},
  { name: "Kötekli", "wins": 1, "draws": 7, "losses": 0},
  { name: "Dalaman", "wins": 2, "draws": 0, "losses": 2}
]
teams.map(function(t) {
   t.points = 2*t.wins+t.draws;
   t.played=t.wins+t.draws+t.losses
})
teams
  .filter(function(t) { return t.played >= 5;})
  .sort(function (t1,t2) {
    if (t1.points != t2.points) return t2.points - t1.points;
    else if (t1.played != t2.played) return t1.played - t2.played;
    else return t2.name.length - t1.name.length;
  })
  .forEach(function(t) {
    t.flag = true;  // will this affect teams[4] output below?
    console.log(t.name + ": " + t.points + "-" + t.played);
  })
console.log(teams[4]);
{% endhighlight %}  

{:.q}
> Q: Give the output of the following Javascript code (i.e. result's final value):
>
> {% highlight javascript %}
var nums = [3,7,2,6,11,4,9,4,1,3]
var result = nums.reduce(function(accumulated, nextValue) {
     if (nextValue % 2 == 0) accumulated[0].push(nextValue);
     else accumulated[1].push(nextValue);
     return accumulated;
  },
  [ [], [] ]  // initial value for accumulated
)
console.log(result);
{% endhighlight %}  

### That's all folks. See you at the midterm... 
