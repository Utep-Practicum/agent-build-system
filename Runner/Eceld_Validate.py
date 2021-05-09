import threading
import time
import os

from subprocess import Popen,PIPE,TimeoutExpired

traffic_found = False
dir = os.path.dirname('/home/kali/eceld-netsys/eceld/')

class EceldValidate:

    def __init__(self):
        self.proc = None
        self.project_name = 'FullTest'


    def comparison(self):
        pass


    def start_eceld(self):
        # time.sleep(15)
        counter = 0
        while True:
            self.proc = Popen(['sudo','python3', 'test_engine_invoke.py'], cwd=dir)
            print('Waiting 10 sec for ECELd to complete')
            try:
                outs, errs = self.proc.communicate(timeout=11)
            except TimeoutExpired:
                self.proc.kill()
                outs, errs = self.proc.communicate()
                file_src = dir+'/plugins/collectors/tshark/parsed/networkDataAll.JSON'
                file_dst = '/home/kali/Desktop/Practicum/agent-build-system-1/Project Data/'+self.project_name+'/Runner/Eceld/temp/comp'+str(counter)+'.json'
                Popen(['sudo','cp',file_src,file_dst], cwd='/')
                counter += 1
                if counter > 1:
                    break


        print('Moving to Runner directory for comparison')
        print('Stop ECELd')


    def read_eceld(self):
        print('Looking for specified traffic')


    def validate():
        # Alejandro haz tus chingaderas aqui
        # Eceld files will be saved in "Project Data/Runner/Eceld/temp"
        traffic_found = bool(input('Has the packet been found'))


if __name__ == "__main__":
    t0 = threading.Thread(target=init_eceld_service, daemon=True)
    t1 = threading.Thread(target=start_eceld,daemon=True)
    #t2 = threading.Thread(target=validate)

    t0.start()
    t1.start()
    #t2.start()

    t0.join()
    t1.join()
    # t2.join()
    
    print(traffic_found)