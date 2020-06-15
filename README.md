# app的ui自动化测试 

## 项目结构

```
tests
├── app 	        #存储最新apk
├── baseView 	    #封装一些基本的操作，如：获取页面元素，获取页面大小，页面滑动等等
├── businessView	#存放登录的方法，便于操作登录后的业务，不用重写登录方法，直接调用
├── common	        #存放一些公共的方法
    ├── common_fun.py	 #存放，弹窗操作，如：权限设置，青少年弹窗等等。一些公共的方法，如：截图，时间格式等等
    ├── desired_caps.py  #存放，appium连接手机的一些参数，如：手机版本，apk包名。设备名称等等
├── config #存放一些配置，如appium连接手机的一些参数配置文件（.yaml），日志配置文件等等
├── data 	        #存放一些数据，实现数据驱动
├── log 	        #存放日志
├── reports         #默认生成测试报告的存储文件夹 
├── screenshots 	#存放截图
├── test_case 	    #存放业务代码
└──test_run         #批量运行测试用例
```

### 环境安装

1、Node.js的安装 下载地址：https://nodejs.org/en/download/releases/

环境变量的配置：Path添加Node.js路径

安装验证运行

```shell
$ node -v
v6.11.1
```
```shell
$ npm -v
3.10.10
```


2、Appium的安装

```shell
$ npm install -g appium
```

环境变量的配置：
APPIUM_HOME：C:\Program Files (x86)\Appium
Path：%APPIUM_HOME%\node_modules\.bin

安装验证运行
```shell
$ appium -v
1.4.16
```

注：Appium版本与Node.js版本应该保持差不多，Node.js版本高或低时，Appium运行时，都会不成功。我的是Appium-Server v1.4.16   安装v6.9.4 v6.11.1版本皆可


3、Appium-desktop

下载地址：https://github.com/appium/appium-desktop/releases 


4、Appium-Python-Client

使用 `pip` 进行安装。

```shell
$ pip install  Appium-Python-Client
```


5、Python 版本**：Python 3.0 及以上的所有版本



6、JDK 安装

安装验证运行
```shell
$ java -version
java version "1.8.0_171"
```


7、Android SDK 安装

（1）、下载SDK 
（2）、Tools选择前三个、API选择最新的，Extras全选
（3）、配置环境变量：
                   ①、新建一个系统环境变量，变量名为ANDROID_HOME，变量值为你的SDK安装路径
                   ②、把%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools添加到Path环境变量中


安装验证运行
```shell
$ adb
```


8、Appium-doctor  安装

```shell
$ npm install appium-doctor -g
```

安装验证运行
```shell
$ appium-doctor
```
提示：All Checks were successful（安装成功）


9、pytest 安装

```shell
$ pip install -U pytest
```

安装验证运行
```shell
$ pytest --version
```


10、alluer 安装

网上下载allure

安装验证运行
```shell
$ allure --version 
2.13.1
```

```shell
$ pip install pytest-allure-adaptor
```



