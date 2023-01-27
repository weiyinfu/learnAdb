import logging
import re
import subprocess as sp
import threading
import time
from pprint import pprint
from typing import Union

import colorama
import colorlog

from fu import dict_util

"""
日志级别过滤：

默认级别为V，输出人日志最低，日志级别最低
D —— Debug
I —— Info
W —— Warning
E —— Error
F —— Fatal 致命
S —— Silent（最高，啥也不输出）

实例：比如想要查看手机的级别为错误的日志

adb logcat *:E（不区分大小写），其中*表示tag

adb logcat ActivityManager:I PowerManagerService:D *:S

"""

log_colors = {
    logging.DEBUG: colorama.Fore.CYAN,
    logging.INFO: colorama.Fore.GREEN,
    logging.WARN: colorama.Fore.YELLOW,
    logging.ERROR: colorama.Fore.RED,
    logging.CRITICAL: colorama.Fore.RED,
}


def package_list():
    s = "adb shell pm list packages"
    content = sp.check_output(s, shell=True)
    content = str(content, "utf8")
    pkg_list = content.splitlines()
    pkgs = []
    for i in pkg_list:
        if not i.strip():
            continue
        if i.startswith('package:'):
            i = i[len('package:'):]
        pkgs.append(i)
    s = "\n".join(pkgs)
    print(f'已安装{len(pkgs)}个包：\n{s}')


def get_package_pid(pkg_name):
    s = f"adb shell pidof -s {pkg_name}"
    try:
        o = sp.check_output(s, shell=True)
    except Exception as ex:
        return -1
    o = str(o, 'utf8')
    o = o.strip()
    if not o:
        return -1
    # 此处只打印第一个进程的日志
    # TODO:此处支持多进程
    return [int(i) for i in o.split()][0]


black_lines = [
    "AudioTrack: isLongTimeZoreData zoer date",
    "PXRSDK_PM ENGINE FPS",
    "AppLog  : receive data=",
]


class Message:
    def __init__(self, s: str):
        self.has_error = True
        self.level = logging.INFO
        self.s = s.strip()
        res = re.search(r"(\S+\s*\S+)\s*(\S+)\s*(\S+)\s*(\S+)\s*(\S+)\s*:\s*(.*)", s)
        if res is None:
            self.content = s
            return
        self.time = res.group(1)
        self.pid1 = res.group(2)
        self.pid2 = res.group(3)
        level = res.group(4)
        self.tag = res.group(5)
        self.content = res.group(6)
        self.level = {
            "I": logging.INFO,
            "W": logging.WARN,
            'E': logging.ERROR,
            'F': logging.FATAL,
            'D': logging.DEBUG,
        }.get(level, logging.INFO)
        self.has_error = False

    def debug(self):
        pprint(dict_util.obj2dict(self))

    def __str__(self):
        fore = log_colors.get(self.level, "")
        return fore + self.s + colorama.Fore.RESET


def logcat(pkg_name: str):
    pid = get_package_pid(pkg_name)
    popen: Union[sp.Popen, None] = None

    def update_pid():
        nonlocal pid, popen
        while 1:
            current_pid = get_package_pid(pkg_name)
            if current_pid != pid:
                pid = current_pid
                if popen:
                    popen.terminate()
                    popen = None
            time.sleep(2)

    def listen_log():
        nonlocal popen
        wait_seconds = 3  # 两次打印之间的时间间隔
        while 1:
            if pid == -1:
                time.sleep(2)
                if int(time.time()) % wait_seconds == 0:
                    # 每隔20s打印一次
                    print(f"没有发现{pkg_name}在运行")
                    wait_seconds = min(wait_seconds * 2, 60 * 10)
                continue
            wait_seconds = 3

            s = f" adb logcat --pid={pid}"
            print(s)
            popen = sp.Popen(s, shell=True, stdout=sp.PIPE)
            while pid != -1:
                if popen is None:
                    break
                s = popen.stdout.readline()
                try:
                    s = str(s, 'utf8')
                except:
                    print(s)
                    continue
                if not s:
                    continue
                # 过滤一些行
                bad = False
                for i in black_lines:
                    if i in s:
                        bad = True
                        break
                if bad:
                    continue
                m = Message(s)
                if m.level >= logging.INFO:
                    print(m)
            print("跳出进程循环")

    threading.Thread(target=update_pid).start()
    threading.Thread(target=listen_log).start()


def parse_line():
    "01-18 17:49:09.202  1914  1936 E PlatformSdkDriver: /Users/sunhan/dev/git/pico/Matrix/sdk/sdk_platform_server/src/main/cpp/messagequeue/ppfMessageQueue.cpp:ppfMessageQueue_PostMessage:75: ppfMessageQueue_PostMessage queue 0x76bffe2800"


def main():
    # pkg_name = sys.argv[1]
    pkg_name = "com.bytedance.platform"
    # pkg_name = "com.picopui.im"
    # pkg_name = "com.bytedance.mpaas.app.client_demo"
    # pkg_name = "com.bytedance.platformonlie"
    # pkg_name = "cn.weiyinfu.myrtcapplication"
    pkg_name = "com.bytedance.pico.matrix"
    # pkg_name = "com.matrix.sdk.unity"
    # pkg_name = "com.bytedance.platformhw"
    # pkg_name = "com.bytedance.platformhw"
    # pkg_name = "com.bytedance.learnPicoXr"
    # pkg_name = "com.bytedance.picoworlds"
    # pkg_name="com.bytedance.GameRTCUnitySDK_android_2017"
    # pkg_name = "com.bytedance.mpaas.app.client_demo"
    # pkg_name = "com.DevsUnitedGames.RealVrFishingP"
    # pkg_name = "com.chesstar.chaoranyike.launcher"
    # pkg_name = "com.example.qiujian12"
    # pkg_name="com.BoyceDemo.PicoSDK"
    # pkg_name = 'com.bytedance.noncnsub'
    # pkg_name = "com.bytedance.platformonlie"
    pkg_name = "com.bytedance.newonline"
    # pkg_name = "com.Alta.ATownshipTale"
    # pkg_name = "com.bytedance.subppe"
    # pkg_name = "com.example.myapplication"
    # pkg_name = "com.Appnori.AllInOneSportsGB"
    # pkg_name = "com.ss.android.ttvr.unity"
    pkg_name = "com.bytedance.platformsdkproxy"
    logcat(pkg_name)


def test():
    m = Message("""09-09 16:50:02.864 10937 10960 I Unity   : 10{"AssetId":7140988031800164396,"AssetType":"default","DownloadStatus":"available","Filepath":"/storage/emulated/0/Android/obb/com.bytedance.platform/charles-proxy-4.6.2-win64.msi","Metadata":"","Filename":"charles-proxy-4.6.2-win64.msi","Version":1,"IapStatus":"not-entitled","IapSku":"Addons_test_6","IapName":"Addons_test_6","IapPrice":"198.90","IapCurrency":"CNY","IapDescription":"来段描述","IapIcon":"https://static-appstore-backup.oss-accelerate.aliyuncs.com/developer-platform/submission/assets/icon/2022-07-08/899623f99bce3fc7fabd3c4bd661011c.jpg"}
    """)
    m.debug()


if __name__ == '__main__':
    main()
