PICO独有的特性

* 判断国内还是海外：adb shell get prop ro.pvr.product.global
* getprop ro.serialno：获取系统序列号
* getprop ro.pvr.internal.version：查看系统版本号（ROM版本号）
* 关掉边界提示：adb shell setprop persist.pvrcon.seethrough.enable 0
* 查看demo帧率：adb shell logcat | grep FPS
* 判断是user版还是debug版：adb shell getprop ro.build.type
* 列出系统应用包名：adb shell pm list packages -s 
* 列出三方应用包名：adb shell pm list packages -3 
* 根据包名清楚应用的缓存：adb shell pm clear 包名
* 获取当前正在运行的应用的包名和activity名称：adb shell dumpsys window| grep mCurrentFocus
* 删除指定文件：adb shell rm -rf xxx
* 进入2d设置界面： adb shell am start -n com.android.settings/com.android.settings.Settings
* 打开设置界面：adb shell am start -n com.picovr.settings/com.picovr.vrsettingslib.UnityActivity

             # The matrix version
            adb shell dumpsys package com.bytedance.pico.matrix | grep version

            # The friend app version
            adb shell dumpsys package com.picopui.im | grep version

            # The ROM/PUI version
            adb shell getprop ro.pvr.internal.version