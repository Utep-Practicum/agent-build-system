import sys
import threading
import time
import os

class ThreadMonitor:

    def __init__(self, name, count) -> None:
        #threading.Thread.__init__(self)
        self.thread_id = name
        self.is_running = False
        self.counter = count

    
    def tshark_collector(self):
        count = 0
        while count < 10:
            file_name = 'pcap_' + str(count)
            cmd = ('tshark -c 500 -w %s.pcap', file_name)
            os.system(cmd)
            count += 1

    def run(self):
        print('Hello!!!')
        time.sleep(1)
        for j in range(10):
            threadLock.acquire()
            t = self.counter - j
            print(self.thread_id + ': got the lock')
            threadLock.release()


threadLock = threading.Lock()
threads =[]

if __name__ == '__main__':
    ThreadMonitor(1,2).tshark_collector()

    """
    for i in range(5):
        threads.append(ThreadMonitor('No. ' + str(i),i))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('Exiting')
    """