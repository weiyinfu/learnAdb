# dumpsys 相关命令

<!-- vim-markdown-toc GFM -->
* [获取当前Activity](#获取当前activity)
* [获取当前Window](#获取当前window)
<!-- vim-markdown-toc -->


### 获取当前Activity

Linux:
```sh
adb shell dumpsys activity | grep "mFocusedActivity"
```

Windows:
```sh
adb shell dumpsys activity  | findstr "mFocusedActicity"
```

### 获取当前Window

```sh
adb shell dumpsys window w | grep \/  |  grep name=
```

# dumpsys
dumpsys用于获取各个服务的运行情况

* `adb shell dumpsys <service-name>`
* `adb shell dumpsys windows`
* `adb shell dumpsys windows displays`查看设备的分辨率
* `adb shell dumpsys meminfo <package_name> or <pid>` 根据包名或者进程ID查看某一程序的内存使用情况


常见的service
```plain
DMAgent
NvRAMAgent
SurfaceFlinger
accessibility
account
activity
alarm
appwidget
audio
audioprofile
backup
battery
batteryinfo
bluetooth
bluetooth_a2dp
bluetooth_profile_manager
bluetooth_socket
clipboard
connectivity
content
country_detector
cpuinfo
device_policy
devicestoragemonitor
diskstats
drm.drmManager
dropbox
entropy
gfxinfo
hardware
input_method
iphonesubinfo
isms
location
media.audio_flinger
media.audio_policy
media.camera
media.mdp_service
media.player
meminfo
memory.dumper
mount
mtk-agps
mtk-epo-client
netpolicy
netstats
network_management
notification
oppo.com.IRUtils
package
permission
phone
power
samplingprofiler
search
sensorservice
simphonebook
statusbar
telephony.registry
telephony.registry2
textservices
throttle
uimode
usagestats
usb
vibrator
wallpaper
wifi
wifip2p
window

```