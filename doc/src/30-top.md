adb shell top -m 5 -s cpu 查看前5个进程cpu的使用情况

输出如下：
```plain
User 35%, System 13%, IOW 0%, IRQ 0% // CPU占用率 
User 109 + Nice 0 + Sys 40 + Idle 156 + IOW 0 + IRQ 0 + SIRQ 1 = 306 // CPU使用情况 

PID CPU% S #THR VSS RSS PCY UID Name // 进程属性 
xx  xx% x   xx  xx  xx  xx  xx   xx 
```

CPU占用率属性： 
* User    用户进程 
* System  系统进程 
* IOW IO等待时间 
* IRQ 硬中断时间 

CPU使用情况（指一个最小时间片内所占时间，单位jiffies。或者指所占进程数）： 
* User    处于用户态的运行时间，不包含优先值为负进程 
* Nice    优先值为负的进程所占用的CPU时间 
* Sys 处于核心态的运行时间 
* Idle    除IO等待时间以外的其它等待时间 
* IOW IO等待时间 
* IRQ 硬中断时间 
* SIRQ    软中断时间 

进程属性： 
* PID 进程在系统中的ID 
* CPU%    当前瞬时所以使用CPU占用率 
* S   进程的状态，其中S表示休眠，R表示正在运行，Z表示僵死状态，N表示该进程优先值是负数。 
* #THR    程序当前所用的线程数 
* VSS Virtual Set Size 虚拟耗用内存（包含共享库占用的内存） 
* RSS Resident Set Size 实际使用物理内存（包含共享库占用的内存） 
* PCY OOXX，不知道什么东东 
* UID 运行当前进程的用户id 
* Name    程序名称android.process.media 


内存占用大小有如下规律：VSS >= RSS >= PSS >= USS 
* PSS  Proportional Set Size 实际使用的物理内存（比例分配共享库占用的内存） 
* USS  Unique Set Size 进程独自占用的物理内存（不包含共享库占用的内存）

我们一般观察Uss来反映一个Process的内存使用情况，Uss 的大小代表了只属于本进程正在使用的内存大小,这些内存在此Process被杀掉之后，会被完整的回收掉，
Vss和Rss对查看某一Process自身内存状况没有什么价值，因为他们包含了共享库的内存使用，而往往共享库的资源占用比重是很大的，这样就稀释了对Process自身创建内存波动。 而Pss是按照比例将共享内存分割，某一Process对共享内存的占用情况。