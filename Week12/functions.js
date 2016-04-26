
function f1(x) {
  return x*x;
}

var my_func = f1;

function f2(x) {
  return x+10;
}

function f3(x) {
  return x*2+15;
}

var my_funcs = [f1,f2,f3,function (x) {return x- 3;}];

function applyTwice(f,x) {
  return f(f(x));
}

function appliedTwice(f) {  
  var result = function (x) {
      return f(f(x));
  }
  return result;
}

f1_twice = appliedTwice(f1);
f2_twice = appliedTwice(f2);
f3_twice = appliedTwice(f3);

function map(f,arr) {
  var new_arr = [];
  for (var i=0; i<arr.length; i++) {
    var new_value = f(arr[i]);
    new_arr.push(new_value);
  }
  return new_arr;
}

function filter(f,arr) {
  var new_arr = [];
  for (var i=0; i<arr.length; i++) {
    if (f(arr[i])) {
       new_arr.push(arr[i]);
    }   
  }
  return new_arr;
}

var nums = [1,2,3,4,5,6,7,8,9]

var nums_sqr = map(function(x) {return x*x}, nums);

function isEven(x) {
  return x%2==0;
}

points = [ {x:2,y:5}, {x:3, y:4}, {x:5, y:12} ]

function distToOrigin(pt) {
  return Math.sqrt(pt.x*pt.x + pt.y*pt.y);
}

points.forEach(function(pt) { 
   console.log(pt.x);
   pt.dist =  distToOrigin(pt);
})

// Exercise from last year

var teams = [
  { name: "HataySpor", "wins": 3, "draws": 2, "losses": 1},
  { name: "HataySporrr", "wins": 3, "draws": 2, "losses": 1},
  { name: "Karabük", "wins": 4, "draws": 0, "losses": 1},
  { name: "Muğlaspor", "wins": 7, "draws": 1, "losses": 0},
  { name: "UlaGücü", "wins": 1, "draws": 3, "losses": 0},
  { name: "Kötekli", "wins": 1, "draws": 7, "losses": 0},
  { name: "Dalaman", "wins": 2, "draws": 0, "losses": 2}
]

teams.forEach(function(t) {
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

// New shorter syntax for anonymous functions in EcmaScript6. 
// Google for "ES6 arrow functions" 

teams
  .filter(t => t.played >= 5)
  .sort( (t1,t2) => 
    t1.points != t2.points ? 
      t2.points - t1.points
    : t1.played != t2.played ? 
        t1.played - t2.played : t2.name.length - t1.name.length
  )
  .forEach(t => {
    t.flag = true;  // will this affect teams[4] output below?
    console.log(t.name + ": " + t.points + "-" + t.played);
  })








