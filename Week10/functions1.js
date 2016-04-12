
function f(int_arg, bool_arg, arr_arg, obj_arg, str_arg) {
  int_arg++;
  bool_arg = !bool_arg;
  arr_arg[0] *= 10;
  arr_arg.push("new");
  obj_arg.x++;
  obj_arg.z = "new";
  str_arg += "xyz"
  console.log("Inside f", int_arg, bool_arg, arr_arg, obj_arg, str_arg)
}

int_var = 10;
bool_var = true;
arr_var = [2,4,6];
obj_var = {x: 1, y:2};
str_var = "abc"

/* console.log(int_var.toString(), bool_var.toString(), arr_var.toString(), obj_var.toString());
f(int_var, bool_var, arr_var, obj_var);
console.log(int_var.toString(), bool_var.toString(), arr_var.toString(), obj_var.toString());
*/