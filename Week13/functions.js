
var points = [ {x:2, y:-1, color: "red" },
           {x:5, y:2,  color: "green  " },
           {x:1, y:5,  color:" blue" },
           {x:2, y:4,  color:"pink" },
           {x:3, y:3,  color:"blue" },                       
           {x:4, y:2,  color:"red " },
           {x:5, y:1,  color:"orange" }
         ];

console.log(points);
// alert("Done")         
points.forEach(function(pt) {
  pt.z = 0;
  pt.color = pt.color.trim();
})    
console.log(points);   
           
var colors = points.map(function(pt) {       
  return pt.color;
})

function distToOrigin(pt) {
  return Math.sqrt(pt.x*pt.x + pt.y*pt.y);
}

function printPts(pts) {
  console.log("--------------------------------------------------")
  pts.forEach(function(pt) {
    console.log("x:" + pt.x + " y:" + pt.y + " color: " + pt.color);  
  })
}
       
console.log(colors);              
console.log(points.map(function(pt) {return distToOrigin(pt)}))

// ES 6 function syntactic sugar

console.log(points.map(pt => distToOrigin(pt)))
console.log(points.filter(pt => pt.x > 3))
console.log(points.filter(pt => pt.color == "red"))

printPts(points)
points.sort(function(pt1,pt2) {
  var val1 = pt1.y;
  var val2 = pt2.y;
  /*
  if (val1 < val2) return -1;  // meaning pt1 < pt2
  else if (val1 > val2) return 1; // meaning pt1 > pt2
  else return 0; // meaining pt1 == pt2
  */
  // return val1 - val2;  // ascending sort
  return val2 - val1;  // descending sort
})
printPts(points)

points.sort(function(pt1,pt2) {
  var val1 = pt1.color;
  var val2 = pt2.color;
 
  if (val1 < val2) return -7;  // meaning pt1 < pt2
  else if (val1 > val2) return 3; // meaning pt1 > pt2
  else return 0; // meaining pt1 == pt2
  
})
printPts(points)

// now let's sort points according to y value when colors are same
points.sort(function(pt1,pt2) {
  var val1 = pt1.color;
  var val2 = pt2.color;
 
  if (val1 < val2) return -7;  // meaning pt1 < pt2
  else if (val1 > val2) return 3; // meaning pt1 > pt2
  else return pt1.y - pt2.y;
  
})
printPts(points)






