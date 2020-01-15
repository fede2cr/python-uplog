import sys
import time
from scapy.all import IP, ICMP, sr1
ip = sys.argv[1]
icmp = IP(dst=ip)/ICMP()
cur_min = 0
f = open("uplog.txt","a")
try:
    while True:
        resp = sr1(icmp,timeout=1)
        secs = time.localtime()
        if cur_min != secs.tm_min:
            cur_min = secs.tm_min
            f.write("]\n["+str(f"{secs.tm_hour:02d}")+":"+str(f"{secs.tm_min:02d}")+":"+str(f"{secs.tm_sec:02d}")+"]|[")
    
        if resp == None:
            f.write("-")
        else:
            f.write(".")
        time.sleep(1)
        f.flush()

except:
    f.close()
