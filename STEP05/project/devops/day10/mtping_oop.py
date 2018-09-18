import threading
import subprocess

class Ping:
    def __init__(self,host):
        self.host=host
    def __call__(self):
        result = subprocess.call(
            'ping -c2 %s &>/dev/null' % self.host,
            shell=True
        )
        if result == 0:
            print("%s : up" % self.host)
        else:
            print("%s : down "% self.host)

if __name__ == '__main__':
    ips = ['176.4.13.%s' % ip for ip in range(1,255)]
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        t.start()
