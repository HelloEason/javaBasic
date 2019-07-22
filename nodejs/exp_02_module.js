var a = 10 ; 
var b = [1,2,3];
var c = function(){
	console.log('this is a function');
}
var d = {
	sayHello(){
		console.log('i am d,and i say hello ');
	},
	f:10,
	g:20
}
module.exports.a = a;
module.exports.b = b;
module.exports.c = c;
module.exports.d = d;

