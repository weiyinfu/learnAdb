# shell要领
adb shell进入交互式命令行，这时候的shell完全就是一个精简版的linux系统。  
`echo $PATH`可以查看全部可用的命令所在的位置，其中主要命令都在以下目录下：
* /system/bin  
* /vendor/bin

# 启动应用
    adb shell am start com.bytedance.platform/com.unity3d.player.UnityPlayerActivity
    adb shell dumpsys package com.bytedance.platform

# 使用alias简化一些命令
```shell
alias login='adb shell input text 12345678901 && adb shell input keyevent 61 && adb shell input keyevent 61 && adb shell input text 1234
&& adb shell input keyevent 61 && adb shell input keyevent 61 && adb shell input keyevent 66
&& adb shell input keyevent 61 && adb shell input keyevent 61 && adb shell input keyevent 66'
```

# 执行tap，点击屏幕特定位置
`$ adb shell input tap x y`，通过开发者模式中的指针位置就可以显示View的坐标


# 延时
adb shell本质也是一个shell，和bash, zsh区别不大，在adb shell中可以通过sleep实现休眠的操作，默认的单位是秒

`$ adb shell sleep 0.5`
在tap后增加0.5秒的延时

# 截图+发飞书
`$ adb shell screencap /sdcard/screen_shot_temp.png`
拷贝到电脑上
`$ adb  pull /sdcard/screen_shot_temp.png ~/Downloads/`
打开Downloads
`$ open ~/Downloads -a Finder`
打开Lark，反馈给那个写Bug的RD
`$ open -a Lark`

# 实现录屏功能
```shell
$ alias -g rStart='adb shell screenrecord /sdcard/record.mp4'
$ alias -g rStop='adb pull /sdcard/record.mp4 ~/Downloads/ && open ~/Downloads -a Finder && open -a Lark'
$
$ rStart
^C
$ rStop
```

# 实现锁屏、解锁
锁屏比较简单，直接按电源键即可。  
`adb shell input keyevent 26`  

解锁屏幕的过程：首先按一下电源键，然后扫一下，等待一下，输入密码，按一下enter键。
`adb shell input keyevent 26 && adb shell input swipe 300 600 300 300 && adb shell sleep 0.5 && adb shell input text 123456 && adb shell input keyevent 66`


# 设置网络代理
Charles抓包容易，设置网络代理麻烦

几乎每个Android开发都想过怎样可以快速设置代理？

最简单的方式莫过于adb

`$ adb shell settings put global http_proxy 10.93.233.22:8888`
删除代理

`$ adb shell settings delete global http_proxy`
但是这招杀敌一千，自损八百。删除代理想要生效需要重启手机，不太建议这么玩


# 启动微信
```shell
adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI
```

# 截屏
adb shell screencap -p /sdcard/01.png  截屏
adb pull /sdcard/01.png  把图片下载到本地