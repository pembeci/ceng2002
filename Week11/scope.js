
function f1() {
  var a = "a_f1";
  c = "c_f1";
  var d = "d_f1";
  e = "e_f1";
  f3();
  console.log("f1....",a,b,c,d,e);
  f2();
  function f2() {
    console.log("f2....", a,b,c,d,e);    
  }

}

function f3() {
  // f2();
  console.log("f3....", a,b,c,e);
}

var a = "a_global";
var b = "b_global";
var c = "c_global";
console.log("Global",a,b,c);
f1();
console.log("Global",a,b,c,e);


