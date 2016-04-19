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