#!/usr/bin/python
#############################################################################
#                    resume Node Manager Operation                          #
#                    COPYRIGHT (C) NOKIA, Egypt                             #
#                    Author: Ahmed Bebars, +201024614238                    #
#############################################################################
import paramiko
import sys
import datetime
import os
import re
#define needed variable
errornumber=1
result_file = open("/home/omc/bebars/NodeManager.log", "a")
currentDT = datetime.datetime.now().strftime('%Y-%m-%d')
result_file.write (currentDT+"\n");
service=["GCSServer","gcssync","gcs-proxy","GCSProxyService"]
#ssh function
def func_connect(ip,hostname,user,password,OS):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
                ssh.connect(ip, username=user, password=password)
        except paramiko.SSHException:
                result_file.write (currentDT+"  "+"Connection Failed")
                quit()
        wincmd="Get-EventLog -LogName 'Nokia GCS' -Message '*Restart GCS*' |  Group-Object -Property Message -NoElement | Select-Object -Property Count | ft -HideTableHeaders"
        stdin,stdout,stderr = ssh.exec_command(wincmd)
        result=stdout.readlines()
        #print (result)
        result=re.search('[+-]?([0-9]*[.])?[0-9]+',str(result))
        #print (result.group(0))
        if int(result.group(0)) > int(errornumber):
                result_file.write (hostname + "Restart GCS error Count= " + result.group(0)+"\n")
                for i in range(len(service)):
                        servicerestart=service[i]
                        wincmd="Restart-Service -Name "+servicerestart+" -Force"
                        stdin,stdout,stderr = ssh.exec_command(wincmd)
        ssh.close()
#call ssh function
func_connect("10.58.95.231","nar2VDA1","administrator","Guisinst1","Windows")
result_file.close()
