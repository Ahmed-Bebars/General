import win32com.client
#other libraries to be used in this script
import os
import re
from datetime import datetime, timedelta
print ("Hub;Region;Node (Bep/PTN);# of free STM after connection;Power level;sender;date;LR")
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
inbox = mapi.GetDefaultFolder(6).Folders["LR"]
messages = inbox.Items
received_dt = datetime.now() - timedelta(days=2)
received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
messages = messages.Restrict("[SenderEmailAddress] = 'Ahmed.Sherif-ElShafie@vodafone.com'")
#messages = messages.Restrict("[Subject] = 'Sample Report'")

for message in list(messages):
    #print(message)
    target = str(message.body)
    progressfile = open("C:\\Users\\bebars\\Desktop\\D\\tmp\\ahmed\\result.txt", 'w')
    progressfile.write(message.body)
    progressfile.close()
    f = open('C:\\Users\\bebars\\Desktop\\D\\tmp\\ahmed\\result.txt','r')
    lookup="Hub"
    lookup2="bm"
    lookup3 = "dbm"
    for num, line  in enumerate(f,1):
        if lookup in line:
             start=num-1
        if lookup2 or lookup3 in line:
             end=num
    array = []
    #print(start,end)
    f = open('C:\\Users\\bebars\\Desktop\\D\\tmp\\ahmed\\result.txt','r')
    lines_to_read = range (start,end)
    for position, line in enumerate(f):
        if position in lines_to_read:
            if not line.isspace() or not "\n":
                array.append(line)
    sender=str(message.sender).replace(', ','@')
    date=(message.ReceivedTime).strftime('%m/%d/%Y %H:%M %p')
    subject=str(message.Subject)
    print (array[5].strip() +";"+ array[6].strip()+";"+array[7].strip()+";"+array[8].strip()+";"+array[9].strip()+";"+sender+";"+date+";"+subject)
    array.clear()