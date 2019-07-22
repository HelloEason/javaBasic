/**
 * 主要是掌握函数式编程思想，函数的句柄作为参数传给绑定函数作输入
 * 面向对象思想，函数也是对象，处理函数也是。
 */
var events = require('events');
var eventEmitter = new events.EventEmitter();

var connectHandler = function connected(){console.log('这是连接处理程序');};
eventEmitter.on('connection',connectHandler);	//绑定事件与处理程序

console.log('开始触发连接事件');
eventEmitter.emit('connection');
console.log('程序执行结束');