import xml.etree.ElementTree as ET  
import json
tree = ET.parse('weather.xml')  
root = tree.getroot()
temp ={}
comand = input()
cmd = comand[0:7]
line = ''
# filename = comand[]
substring = comand[8:len(comand)]
for i in substring:
    line += i
    if i == ' ':
        break        
if cmd == 'weather':
    for elem in root:  
        temp[elem.tag] = []
        if len(elem.attrib) != 0:
            temp[elem.tag].append(elem.attrib)
        for i in elem:
            if len(i.attrib) != 0:
                temp[elem.tag].append({
                    i.tag : i.attrib
                    })
            if i.text != None:
                temp[elem.tag].append({
                    i.tag : i.text
                    })
    with open('weather.json', 'w') as outfile:  
        json.dump(temp, outfile)
    print('weather.json')
else:
    filename = substring[len(line):len(substring)]
    fileRead = open(filename,'r')
    for i in range(int(line)):
        print(fileRead.readline())
