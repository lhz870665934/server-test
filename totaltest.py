import os, threading, time

class myThread(threading.Thread):  # 线程处理函数
    def __init__(self, name):   
        threading.Thread.__init__(self);  # 线程类必须的初始化  
        self.thread_name = name;  # 将传递过来的name构造到类中的name  
    def run(self): 
        time.sleep(0.1 * self.thread_name)
        os.system("test.py")


threads = []
for i in range(0, 500):   #1、10、100、500、 1000
    thread = myThread(i)
    threads.append(thread)

for t in threads:
    t.start()

