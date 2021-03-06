功能能测试配置字段说明：

	Test_plans
		该字段表示一个测试计划的集合，所有的test_plan都应该在这里面配置。
	Test_plan
		该字段表示一个具体的测试计划，之后的大括号里面的所有配置全是该测试计划的具体配置参数；如果需要，一个config文件中，可以同时配置多个test_plan。
	Comment
		该字段表示测试计划的解释说明，该字段的内容会直接被测试报告中引用。所以测试的相关说明性内容都可以在这里配置。
	Jobs
		该字段表示一个测试业务的集合，里面可以配置多个独立的测试业务。
	Job
		该字段表示一个具体的测试业务，同时也是测试工具最小的执行单元。
	Data_file
		该字段指定测试业务需要的配置文件名称，注意：因为程序将数据文件的路径写死了，因此这里只需要指定文件名称即可，同时也意味着数据文件只能放在上面介绍的test_data目录
	Host
		该字段指定测试用的AC或者AP。
		当测试AC的API时，该字段配置AC的IP地址，例：http://172.16.30.100/api
		当测试AP的本地API时，该字段配置AP的IP地址，例：http://172.16.10.10，注意：没有‘/api’
	Hub
		该字段指定测试使用的AP mac地址。当测试本地API时，该字段可以不配置。
	Model
		该字段配置测试用AP的设备类型
	User and pwd
		这两个字段配置AC的开发者账号和密码，当测试云端API时，该字段必须配置正确，测试本地API时，该字段无需配置
	Filter
		该字段配置一些扫描过滤相关的参数，该部分配置主要用在scan接口的测试。可以根据自己实际的测试环境，配置需要的过滤参数。
	case_path
		该字段指定了case字段配置的case所在项目文件夹，我么test_case下的每个目录都可以理解成一个测试项目，
		如果不配置该字段,系统会默认去test_case目录下查找所有的项目。
	Case
		该字段指定了测试业务需要执行的测试用例，最小粒度为一个测试参数，可以同时指定多个测试参数。

性能测试配置字段说明：

	#服务器地址,运行测试工具服务端（server.py）机器的IP地址
	server = 168.168.20.66
	#测试模式,0代表稳定性测试，1代表性能测试；
	test_mode = 1
	#稳定性测试时，所有AP同时开启扫描；
	#性能测试时，间隔一段时间开启一定数量的AP，直到所有AP全部开启扫描

	#性能模式时必须设置下面参数，稳定性测试时下面的参数设置可以忽略
	#两个批次AP开启扫描的时间间隔，秒为单位
	INTERVAL = 100
	#每批次开始扫描的AP数量
	PER_COUNT = 5
	#准备进行测试的进程数量，建议进程数=客户端测试机器数总CPU核数
	PROCESS_COUNT = 2
	#AC相关配置
	#AC地址，待测试的AC地址
	HOST = http://168.168.30.254/api
	#开发者帐号
	user = tester
	pwd = 10b83f9a2e823c47
	#AC的root用户密码，用来自动ssh登录AC执行资源监控命令
	ac_root_pwd = cassia1983
	#测试持续时间，性能测试总体运行时间建议少于2小时，单位为秒
	test_time = 1000
	#测试过程中允许的最大离线AP数量，如果有超过这个数量的AP离线，测试终止
	MAX_OFFLINE = 1
	#测试结果文件存放路径，文件直接从AC上面远程拷贝
	data_path = /root/res/