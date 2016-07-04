#-*- coding:utf-8 -*-
'''
Created on 2016年6月23日

@author: QiRui.Su
'''
import threading
import time
import subprocess
import sys

def check_system():
    sysinfo = sys.platform
    return sysinfo

def check_host_isalive(sysinfo, ipaddr, times):
    if sysinfo == 'win32':
        isalive = subprocess.call('ping -n 1 %s' % ipaddr, shell=True, stdout=file('D://out.log', 'a'), stderr=subprocess.PIPE )
    else:
        isalive = subprocess.call('ping -c 1 %s' % ipaddr, shell=True, stdout=file('/dev/null', 'a'), stderr=subprocess.PIPE )
        
    if isalive == 1:
        dead_ip_list.append(ipaddr)
    elif isalive == 0:
        alive_ip_list.append(ipaddr)
    print dead_ip_list

if __name__ == '__main__':
    sysinfo = check_system()
    dead_ip_list = []
    alive_ip_list = []
    for i in xrange(1, 255):
        ipaddr = "218.30.110.%s" % i
        t = threading.Thread(target=check_host_isalive, args=(sysinfo, ipaddr, i))
        #threads.append(t)
        #t.setDaemon(True)
        t.start()
        
    print("Dead ip: %s \nAlive ip :%s \n" % (dead_ip_list, len(alive_ip_list)))
#     print (threading.activeCount() -1 )
#     
#     for item in threading.enumerate():
#         print item
#  
#     print
#      
#     for item in threads:
#         print item
