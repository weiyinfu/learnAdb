# 常用
adb shell getprop 查看机器的全部信息参数
adb shell getprop ro.serialno 查看机器的序列号
adb shell getprop ro.carrier 查看机器的CID号
adb shell getprop ro.hardware 查看机器板子代号
adb shell getprop ro.bootloader 查看SPL(Hboot)版本号

adb shell getprop dhcp.wlan0.ipaddress 获得IP

adb shell getprop ro.sf.lcd_density 获得屏幕密度

adb shell getprop ro.serialno 查看serial number

adb shell getprop|grep heapgrowthlimit 查看单个应用程序最大内存限制

adb shell getprop|grep dalvik.vm.heapstartsize 查看应用启动后分配的初始内存

adb shell getprop|grep dalvik.vm.heapsize 查看单个java虚拟机最大的内存限制

// 1.获取厂商名称
getprop ro.product.brand
// 2.设备型号
getprop ro.product.model
// 3.安卓版本
getprop ro.build.version.release
// 4.网卡名称
wifi.interface
// 5.Google glass系统版本
ro.build.version.glass
// 6.MAC地址
ro.boot.macaddr
// IP地址
dhcp.wlan0.ipaddress
# 修改
`getprop [key]`  取得对应的key的属性值
getprop  列出所有配置属性值
如果要修改属性的话，很简单，只需修改字典值就可以了，如：
`setprop [key] [value]` 设置指定key的属性值；
watchprops  监听系统属性的变化，如果期间系统的属性发生变化则把变化的值显示出来