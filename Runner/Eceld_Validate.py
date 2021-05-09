import threading
import time
import os

from subprocess import Popen,PIPE,TimeoutExpired

traffic_found = False
dir = os.path.dirname('/home/kali/eceld-netsys/eceld/')

class EceldValidate:

    def __init__(self):
        self.proc = 


    def comparison(self):
        pass


    def start_eceld(self):
        time.sleep(15)
        for i in range(2):
            self.proc = Popen(['sudo','python3', 'test_engine_invoke.py'], cwd=dir)
            print('Waiting 10 sec for ECELd to complete')
            try:
                outs, errs = proc.communicate(timeout=12)
            except TimeoutExpired:
                proc.kill()
                outs, errs = proc.communicate()

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