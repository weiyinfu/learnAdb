import re
import subprocess as sp
from typing import List


def run(s: str):
    s = sp.check_output(s, shell=True)
    return str(s, 'utf8')


def devices() -> List[str]:
    ans = run("adb devices")
    devices = []
    for i in ans.splitlines():
        line = i.split()
        if len(line) == 2 and line[1] == 'device':
            devices.append(line[0])
    return devices


def version():
    ans = run("adb version")
    for i in ans.splitlines():
        if i.startswith('Version'):
            return i.split()[1]


class Device:
    def __init__(self, device: str):
        self.device = device

    def run(self, s):
        device_flag = ""
        if self.device:
            device_flag = f"-s {self.device}"
        return run(f"adb {device_flag} {s}")

    def list_application(self, only_system: bool = False, only_thirdparty: bool = False):
        s = ""
        if only_system:
            s = "-s"
        if only_thirdparty:
            s = "-3"
        ans = self.run(f"shell pm list packages {s}")
        apps = []
        for i in ans.splitlines():
            if i.strip():
                apps.append(i[i.index(':') + 1:])
        return apps

    def install(self, apk_path: str, replace=False, test=False, sdcard=False, degrade=False, grant_all_privilige=False):
        flags = []
        if replace:
            flags.append('-r')
        if test:
            flags.append('-t')
        if sdcard:
            flags.append('-s')
        if degrade:
            flags.append('-d')
        if grant_all_privilige:
            flags.append('-g')
        ans = self.run(f"install {' '.join(flags)} {apk_path}")
        print(ans)

    def uninstall(self, package_name: str, keep_config=False):
        flags = ""
        if keep_config:
            flags = "-k"
        ans = self.run(f"uninstall {flags} {package_name}")
        print(ans)

    def clear_app_cache(self, package_name: str):
        ans = self.run(f"shell pm clear {package_name}")
        print(ans)

    def dumpsys_activities(self):
        # 查看处于前台的activity
        ans = self.run(f"shell dumpsys activity activities")
        return ans

    def dumpsys_services(self, package_name: str):
        ans = self.run(f"shell dumpsys activity services {package_name}")
        return ans

    def dumpsys_package(self, package: str):
        ans = self.run(f"shell dumpsys package {package}")
        return ans

    def pm_package_path(self, package: str):
        ans = self.run(f" shell pm path {package}")
        return ans

    def shell_free(self):
        ans = self.run(f"shell free -h")
        return ans

    def shell_meminfo(self):
        ans = self.run(f"shell cat /proc/meminfo")
        return ans

    def shell_cpuinfo(self):
        ans = self.run(f"shell cat /proc/cpuinfo")
        return ans

    def shell_df(self):
        ans = self.run(f"shell df -h")
        return ans

    def mac_address(self):
        ans = self.run(f"shell cat  /sys/class/net/wlan0/address")
        return ans

    def get_prop(self):
        ans = self.run(f"shell getprop")
        kv = {}
        for i in ans.splitlines():
            if re.match("\[(.*)\]:\s*\[(.*)\]", i):
                x = re.search("\[(.*)\]:\s*\[(.*)\]", i)
                k = x.group(1)
                v = x.group(2)
                kv[k] = v
        return kv


d = devices()
print(d)
d = Device(d[1])
# print(d.list_application(only_system=True))
# print(d.dumpsys_activities())
# print(d.shell_cpuinfo())
print(d.get_prop())
