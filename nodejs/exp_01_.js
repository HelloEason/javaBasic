node例程：

/**	hello world 例程
**  1 使用require 导入http模块
**  2 使用 http.createServer 创建http服务器，调用监听方法；
**  3 使用回调函数 响应请求
*/
	var http = require('http'); 	//导入http模块
	http.createServer(function(request,response){
		response.writeHead(200,{'Content-Type':'text/plain'});
		response.end('hello world');
	}).listen(8088);
	console.log('first server run at http://127.0.0.1:8088');

	/**	repl 例程
	* 相当于一个立即执行的 node环境，类似shell, 可以用来测试 nodejs程序 。
	*/
	在终端中输入 node 即可启动 repl;
	一些repl命令：
		ctrl + c - 终止当前命令
		ctrl + c twice - 终止Node REPL
		ctrl + d - 终止Node REPL
		Up/Down Keys - 查看命令历史记录和修改以前的命令
		tab Keys - 当前指令的列表
		.help - 所有命令的列表
		.break - 退出多行表达式
		.clear - 从多行表达退出
		.save filename - 当前Node REPL会话保存到文件中
		.load filename - 加载文件的内容在当前Node REPL会话

/**	npm 常用命令
**  用于第三方包管理 ，下载，安装，管理；
*/
	npm -v 					查看版本；
	npm install npm -g  	更新npm；

	npm install <Module Name>  [-g]   安装模块；[g]表示全局安装或本地安装；
	npm list <Module Name> [-g]		  查看安装模块的版本号；

	npm uninstall <Module Name> 	 卸载模块
	npm update <Module Name>		 更新模块
	npm search <Module Name> 		 搜索模块

	npm publish		发布自己的模块（具体需要经过生成package.json,注册npm用户等步骤）；

	使用淘宝cnpm镜像，可以加快安装模块速度；


/**	时间循环实例
**  1 引入事件包
	2 创建时间发射器对象
	3 创建时间处理程序
	4 使用发射器绑定 事件+事件处理函数；
	5 触发事件；
*/
	var events = require('events');
	var eventEmitter = new events.EventEmitter();

	var connectHandler = function connected(){console.log('这是连接处理程序');}
	eventEmitter.on('connection',connectHandler);	//绑定事件与处理程序

	console.log('开始触发连接事件');
	eventEmitter.emit('connection');
	console.log('程序执行结束');



/** events包 、EventEmitter 类
*/
	var events = require('events');
		//导入events包；	
		//typeof events  === function；
	var ee = new events.EventEmitter();
		//使用构造函数获得一个“事件发射对象”；

	var EventEmitter = require('events').EventEmitter; 
		//实际上，EventEmitter是events模块里的一个构造函数 属性。可以用这种方式先获取到该构造函数/类模板。
		//构造函数名，用大写开头。
	var e = new EventEmitter(); 
		方法：
			addListener(event,listener)
			on(event，listener)
			once(...)
			removeListener(...);
			removerAllListener(event);
			listeners(event);
			emit(event,[args..]);
			//event是事件，事件，可以是自定义的时间，但是触发条件也要自定义。
			//不然，就需要使用系统的时间，如键盘，鼠标点击等事件。
			//一个事件，可以对应多个handler,
	总结：发射器类，一般是用来被继承的，而不是直接使用。


/**  Buffer 内置库
*
*/
var buf1 = new Buffer(10);
var buf2 = new Buffer([10,20,30,40,50]);
var buf3 = new Buffer("hello world ","utf-8");
var str = "hello this is a string";
len1 = buf1.write(str,5,10,"utf-8");
