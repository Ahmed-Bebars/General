#######developped by Ahmed Bebars, +201024614238#################
from netmiko import ConnectHandler
import getpass
import sys
ip_array = []
IPpath = raw_input("Enter your IP file path : ")
result_file = open ('D:\\result_file.txt','w')
if os.path.isfile (IPpath):
	with open(IPpath) as f:
	  ip_array = f.readlines()
device = {

'device_type': 'cisco_ios',

'ip': 'IP',

'username': 'xxxxx',

'password': 'xxxxx',

'secret':'xxxxxx'

}
for IP in range(len(ip_array)):
	device['ip']=ip_array[IP]
	ssh_connect = ConnectHandler(**device)
	ssh_connect.enable()
	output1=ssh_connect.send_command('show ip int brief')
	output2=ssh_connect.send_command('show ip sla statistics')
	output3=ssh_connect.send_command('show run | sec sla')
	output4=ssh_connect.send_command('show run | sec tunnel')

	ssh_connect.disconnect()
	result_file.write (output1+output2+output3+output4)
result_file.close()
