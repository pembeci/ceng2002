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