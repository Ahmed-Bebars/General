import csv
import xml.etree.ElementTree as ET

file=open("C:\\Users\\bebars\\Desktop\\project\\load_stats_log.xml","r")
load=open("C:\\Users\\bebars\\Desktop\\project\\load_stats_log.csv","w")
tree = ET.parse(file)

# get root element
root = tree.getroot()
print(root)
header="time,qos,processedQueries,rejectedQueries,processedUpdates,rejectedUpdates"
string=""
print(header)
load.write(header+"\n")
for child in root.iter():

    if child.tag == "load":
        time=""
        time=str(child.attrib["start"])
        #print(child.attrib["start"])
    if child.tag == "qos":
        print(string)
        load.write(string+"\n")
        string=""
        string = time+","+string + str(child.attrib["level"])+","
        #print(child.attrib["level"])
    if child.tag == "counters":
        string = string + str(child.attrib["processedQueries"])+","+str(child.attrib["rejectedQueries"])+","+str(child.attrib["processedUpdates"])+","+str(child.attrib["rejectedUpdates"])
        #print(child.attrib["processedQueries"])
        #print(child.attrib["rejectedQueries"])
        #print(child.attrib["processedUpdates"])
        #print(child.attrib["rejectedUpdates"])
    #[elem.tag for elem in root.iter()]
