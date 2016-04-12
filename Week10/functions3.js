
/*
Default parameters for JS is part of EcmaScript 6 definition.
So this may not be supported at every browser
*/
function describe(name, gender="female", country="Turkey") {
  console.log(name + " is a " + gender + " from " +country);
}

describe("Maria", "female", "Spain");
describe("Ali", "male");
describe("Zeynep");

/* Before ES6 added this functionality to the language
   people were using the following trick for default values */

function describe2(name, gender, country) {
  gender = gender == undefined ? "female" : gender;
  // country = country == undefined ? "Turkey" : country;
  country = country || "Iran"
  console.log(name + " is a " + gender + " from " +country);
}

function describe3(name) {
  console.log("Name = ", name)
  console.log("arguments = ", arguments)
  if (arguments.length == 1) {
    console.log("Hello " + arguments[0])
  }
  else if (arguments.length == 2) {
    console.log("Hello " + arguments[0]);
    var gender = arguments[1];
    console.log("So you are a " + gender);
  }
  else if (arguments.length == 3) {
    var name = arguments[0];
    var gender = arguments[1];
    var country = arguments[2];
    console.log(name + " is a " + gender + " from " +country);
  }
}

