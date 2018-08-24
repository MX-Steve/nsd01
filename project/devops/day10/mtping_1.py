import threading
import subprocess

def ping(host):
    result = subprocess.call(
        'ping -c2 %s &>/dev/null' % host,
        shell=True
    )
    if result == 0:
        print("%s:up" % host)
    else:
        print("%s:down" % host)

if __name__ == '__main__':
    ips=['176.4.13.%s' % ip for ip in range(1,255)]
    for ip in ips:
        t = threading.Thread(target=ping,args=(ip,))
        t.start()