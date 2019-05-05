# -*- coding: utf-8 -*-

# 有join的时候（且每个子线程都要添加join），才会实现实现子线程不结束，主线程不会结束的情况出现

import threading
import time


def job():
    print("T1 start \n")
    time.sleep(1)
    print("T1 finish \n")


def main():
    added_thread = threading.Thread(target=job, name="T1")
    added_thread.start()
    added_thread.join()
    print("all done\n")


if __name__ == '__main__':

    main()