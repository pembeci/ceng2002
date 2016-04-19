
var b = 5;
var a = b * 10;
b = 6;
console.log("a=" + a);
a = b;
b = 20;
console.log("a=" + a);
b = [10,20,30];
a = b;
b[1] = "new value";
console.log("a=" + a);
a.push(100);
console.log("a=" + a);
console.log("b=" + b);

b = [10,20,30]
a = b.slice()
b[1] = "new value";
a.push(100);
console.log("a=" + a);
console.log("b=" + b);

b = { id:7, name: "izzet" }
a = b;
b.id = 9
a.name = "ismet";
console.log(a);
console.log(b);

hoca12 = { "id": 67, "name": "Izzet Pembeci", "title": "Yrd.Doç.Dr." };
hoca14 = { "id": 157, "name": "Tuğba Süzek", "title": "Yrd.Doç.Dr." };
hoca27 = { "id": 187, "name": "Barış Süzek", "title": "Yrd.Doç.Dr." };

cengDepartment = { "id": 2028, "name": "Computer Engineering", "code": "CENG",
               "address": "Müh. Fak. Kötekli ...", 
               "faculty": [hoca12, hoca14, hoca27]
             };  
b = { id:3, name: "ali", phones: [1234, 5678, 35], dept: cengDepartment }
// a = cloneUser(b);
a = deepCloneUser(b);
b.id = 5;
a.name = "veli";
b.phones.push(1111);
console.log(a);
console.log(b);

function cloneUser (userObj) {
  var newUser = {}
  newUser.id = userObj.id;
  newUser.name = userObj.name;
  newUser.phones = userObj.phones;
  newUser.dept = userObj.dept;
  return newUser;
}

function deepCloneUser (userObj) {
  var newUser = {}
  newUser.id = userObj.id;
  newUser.name = userObj.name;
  newUser.phones = userObj.phones.slice();
  newUser.dept = userObj.dept; // we aren't deep cloning this property
  return newUser;
}

var c = [1,2,3]
var d = c;
c.push(100);
console.log(d);
c = "cat";
console.log(d);

c = "abcde";
var d = c;
console.log(d);
c = c + "XXX";
console.log(d);







