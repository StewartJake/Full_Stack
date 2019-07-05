// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function(){
	  console.log(this.name.length);
  }}


// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee1 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  getInfo: function(){
	  outStr = "";
	  for (key in this){
		  if (key != "getInfo")
		  	outStr += titleCase(key) + " is " + String(this[key]) + ", ";
	  }
	  var outAlert=outStr.slice(0, (outStr.length - 2)) + "."
	  alert(outAlert);
}}
function titleCase(str){
	var outStr = "";
	outStr += str[0].toUpperCase();
	outStr += str.slice(1,str.length);
	return outStr;
}
// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee2 = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function(){
	  last = this.name.split(" ")[1];
	  console.log(last);
  }}


// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
