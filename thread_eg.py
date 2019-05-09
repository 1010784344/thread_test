# -*- coding: UTF-8 -*-
#coding=utf-8
from time import sleep, ctime
import threading

def super_player(file,time):
    for i in range(2):
        print 'Start playing： %s! %s' %(file,ctime())
        sleep(time)

#播放的文件与播放时长
list = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}

threads = []
files = range(len(list))


# 简单来说就是把文件添加到线程池里面，再一起执行。
#创建线程池
for file,time in list.items():
    t = threading.Thread(target=super_player,args=(file,time))
    threads.append(t)

if __name__ == '__main__':
    #启动线程
    for i in files:
        threads[i].start()

    # 有join的时候（且每个子线程都要添加join），才会实现实现子线程不结束，主线程不会结束的情况出现
    # join() 方法是表示等这个线程运行完毕，程序再往下运行。
    for i in files:
        threads[i].join()

    #主线程
    print 'end:%s' %ctime()