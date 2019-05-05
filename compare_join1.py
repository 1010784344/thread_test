# -*- coding: utf-8 -*-


import threading
import time


def job():
    print("T1 start \n")
    time.sleep(1)
    print("T1 finish \n")


def main():
    added_thread = threading.Thread(target=job, name="T1")
    added_thread.start()
    print("all done\n")


if __name__ == '__main__':

    main()