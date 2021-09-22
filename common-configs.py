#!/usr/bin/python3.7

"""
COMMON SETUP FOR CENTOS 7 (For clients and servers)

        Installed services:
                tcpdump
                traceroute
                net-tools
                FTP(Client)
                SNMP services (walk, SNMP)
                NTP
                SNMP 
                downloading script for penguin logo problem LIBRENMS(SNMP)

        Configs:
                hostname
                timezone ("Asia/Manila")

        Security:
                Firewalld and Selinux (Disabled)

        TODO:
                SNMP config (there are 2 config (for librenms and for ordinary snmpwalk))
                if those 2 are different config, separate this. 

                Verification changes

                Make this as atleast functional programming (OOP optional)
"""

import os

# Installation of common services

install_list = ['yum -y install tcpdump', 'yum -y install traceroute',
'yum -y install net-tools', 'yum -y install ftp',
'yum -y install net-snmp net-snmp-utils', 'yum -y install ntp',
 'curl -o /usr/bin/distro https://raw.githubusercontent.com/librenms/librenms-agent/master/snmp/distro']

install_list_length=0
for i in install_list:
        os.system(install_list[install_list_length])
        install_list_length+=1


# Enabling installed services
enable_service_list = ['systemctl enable ntpd', 'systemctl enable snmpd',
 'systemctl start ntpd', 'systemctl start snmpd', 'chmod +x /usr/bin/distro']

ctr = 0
for i in enable_service_list:
        os.system(enable_service_list[ctr])
        ctr+=1

os.system('clear')

# Configuring hostname

hostname = input("Enter hostname: ")

command_hostname = 'hostnamectl set-hostname {}'.format(hostname)

os.system(command_hostname)

host_config = '''
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4 {}
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
'''.format(hostname)


with open('/etc/hosts', "w") as myfile:
        myfile.write(host_config)

#
# Timezone
#
os.system('timedatectl set-timezone Asia/Manila')

#
# Disabling Security
# 

security_list = ['systemctl stop firewalld', 'systemctl disable firewalld',
 'setenforce 0']

security_list_length=0

for i in security_list:
        os.system(security_list[security_list_length])
        security_list_length+=1


# Disabling Selinux

selinux_disabled = open('selinux_disabled.txt', "r")

with open('/etc/selinux/config', "w") as myfile:
        myfile.write(selinux_disabled.read())

#os.system('reboot')