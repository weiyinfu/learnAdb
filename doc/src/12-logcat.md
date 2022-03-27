# adb logcat -f /sdcard/haha.log 
这个命令输出日志到一个文件，这个文件是android机器的文件，而不是电脑。因此，很容易报错：`logcat: Couldn't open output file: Read-only file system`  

如果真的想要打印到本机，还是使用管道命令比较合适。  
# adb抓取特定应用的日志 
linux/mac:
```sh
adb logcat | grep -F "`adb shell ps | grep com.asanayoga.asanarebel  | tr -s [:space:] ' ' | cut -d' ' -f2`"
```

windows:
```sh
adb logcat | findstr com.example.package
```
这里面用到的`adb shell ps | grep my.package.name`首先获取到进程ID。  


# adb查看特定进程的日志
```sh
adb logcat --pid=233
--pid=<pid>                 Only print logs from the given pid.
```

因此查看特定包的进程的日志：
```
adb logcat --pid=`adb shell pidof -s com.example.app`
```

# adb直接查看特定包的日志
`adb logcat com.example.example:I *:S`

com.bytedance.GameRTCUnitySDK_android_2017



# 查看包名
adb shell pm list package 
adb shell pm list package -f 获取全部的包名及路径
