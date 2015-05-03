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
> {% highlight javascript linenos %}
var a = ...
var first = a && a[0]
if (first) console.log(first)
else console.log("array is empty")
{% endhighlight %}

### Lazy Evaluation in Booleans

{:.q}
> Q: For boolean expressions, Python and Javascript use lazy evaluation (or sometimes called short circuting in this context). See this [discussion](http://stackoverflow.com/questions/13960657/does-python-evaluate-ifs-conditions-lazily). Give the value of `a` after each line in the following Python code:
>
> {% highlight python linenos %}
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
> {% highlight javascript linenos %}
var x=1, y=2, z=3;

function f() {
  var y = 4;
  z = 5;
  console.log("f1", x, y, z)
  g(x,y)
  console.log("f2", x, y, z)
  h(11,12);
  console.log("f3", x, y, z)
}

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

function h(y,z) {
    console.log("h3", x, y, z);
    x = 9;
    z = 10;
    console.log("h4", x, y, z);
}

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
> {% highlight python linenos %}
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

f()
{% endhighlight %}

{:.q}
> Q: What will be the output of the following code:
>
> {% highlight python linenos %}
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
> {% highlight js linenos %}
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
* Default arguments
* Python \*args, \*\*kargs
* First class values
* Closures
* Higher Order Functions (map, filter, reduce, sort)

## Miscellanous

* List generators
* Tuples in Python (immutable)
* for (key in obj1)
* cloning in Java?


