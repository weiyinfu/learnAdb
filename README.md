本repo主要复制于[awesome-adb](https://github.com/mzlogin/awesome-adb)


# apktool apk反编译工具
https://ibotpeaches.github.io/Apktool/install/

mac下可以直接`brew install apktool`进行安装。

首先apk文件就是一个zip文件：
```
unzip testapp.apk
```
而apktool则可以
```
apktool d x.apk
```

# matrix
在android上执行脚本的工具。  
使用matrix可以实现移动端自动化测试。  

getprop ro.serialno 获取系统版本号

# android投屏工具
mac下使用`brew install scrcpy`命令安装，安装时使用brew镜像可能会出错。  
https://github.com/Genymobile/scrcpy/blob/master/BUILD.md#simple


# 在android上运行python：使用QPython
https://github.com/qpython-android/qpython3/releases

# 在android上运行终端：使用termux

# adb shell 网络
adb shell svc wifi disable 可以关闭wifi
adb shell svc wifi enable 可以打开wifi
adb shell svc wifi prefer 即wifi+4G一起打开的情况下，可以优先使用wifi通讯
adb shell svc data disable 可以关闭4G数据通讯
adb shell svc data enable 可以打开4G数据通讯
adb shell svc data prefer 即wifi+4G一起打开的情况下，可以优先使用4G通讯

# Android Web Toolbox
我一直想做的一个ADB管理工具。  
https://yume-chan.github.io/ya-webadb/

* 基于WebUSB API。火狐认为WebUSB很危险，所以直接不支持。要想使用这个网页，需要在Chrome里面使用。
* 在网页里面操作ADB容易被窃取信息，比较危险。  
* 这个网页的安全性基于作者的人格和开源。

竞品：
* https://github.com/webadb/webadb.js：只有js，没有网页；基于WebUSB；5年没有更新了
* https://github.com/antdking/WebADB：有网页，没有README；5年没有更新

## 参考链接
* [Android Debug Bridge](https://developer.android.com/studio/command-line/adb.html)
* [ADB Shell Commands](https://developer.android.com/studio/command-line/shell.html)
* [logcat Command-line Tool](https://developer.android.com/studio/command-line/logcat.html)
* [Android ADB命令大全](http://zmywly8866.github.io/2015/01/24/all-adb-command.html)
* [adb 命令行的使用记录](https://github.com/ZQiang94/StudyRecords/blob/master/other/src/main/java/com/other/adb%20%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%9A%84%E4%BD%BF%E7%94%A8%E8%AE%B0%E5%BD%95.md)
* [Android ADB命令大全(通过ADB命令查看wifi密码、MAC地址、设备信息、操作文件、查看文件、日志信息、卸载、启动和安装APK等)](http://www.jianshu.com/p/860bc2bf1a6a)
* [那些做Android开发必须知道的ADB命令](http://yifeiyuan.me/2016/06/30/ADB%E5%91%BD%E4%BB%A4%E6%95%B4%E7%90%86/)
* [像高手一样使用ADB命令行（2）](http://cabins.github.io/2016/03/25/UseAdbLikeAPro-2/)