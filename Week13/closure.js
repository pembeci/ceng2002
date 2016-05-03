
function counter() {
  var a = 7;
  var count=0;
  var f = function () {
    var a = 10;
    // console.log("Called", a, count);
    count++;
    return count;
  }
  
  return f;
}

var counter1 = counter()
var counter2 = counter()
var counter3 = counter()

function advanceCounter(init, step) {
  var count = init
  var f = function () {    
    count += step;
    return count;
  }  
  return f;
}

var counter4 = advanceCounter(100,5);
var counter5 = advanceCounter(10,-1);

console.log(counter4())
console.log(counter4())
console.log(counter5())
console.log(counter5())
console.log(counter4())

function outer(start) {
  var end = 20;
  var inner = function() {
    start++;
    end--;
    console.log("start=" +start + " end=" +end);
  }
  return inner;
}  

var f1 = outer(5)
f1();f1();f1()
var f2 = outer(1)
f2();f2();
f1();
f2();











