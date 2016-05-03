
var nums = [7,2,9,11,8,5]

var result = nums.reduce(function(partialResult, nextValue) {
  console.log("Partial result: ", partialResult, "Next value: ", nextValue)
  return partialResult + nextValue;
}, 100)

console.log(result)

var initialResult = { "even": [], "odd": [] }

var result = nums.reduce(function(partialResult, nextValue) {
  console.log("odds: ", partialResult.odd.toString(), 
              "evens", partialResult.even.toString(), 
              "Next value: ", nextValue)
  if (nextValue%2==0) {
    partialResult.even.push(nextValue)
  }
  else {
    partialResult.odd.push(nextValue)
  }
  return partialResult;
}, initialResult)

console.log(result)

var nums2 = [2,3,4,1,2,4,3,2,7,4,3,1,4,3,7,8,2,4,6,1,2]

var result = nums2.reduce(function(partialResult, nextValue) {
  console.log("Partial result: ", partialResult, "Next value: ", nextValue)
  if (partialResult.indexOf(nextValue) == -1) {
    partialResult.push(nextValue);
  }  
  return partialResult;
}, [])

console.log(result)

















