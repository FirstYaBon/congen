import xlrd
import xlwt

workbook = xlrd.open_workbook('test.xlsx')
sheet = workbook.sheet_by_name('test')

#first column
indexArray = sheet.col_values(0)
indexArray.remove('index')

#second column
serviceArray = sheet.col_values(1)
serviceArray.remove('Service_Set_(new)')

#third column
tcpArray = sheet.col_values(2)
tcpArray.remove('TCP')
for i in range(len(tcpArray)):
    tcpArray[i] = tcpArray[i].split(',')

#fourth column
udpArray = sheet.col_values(3)
udpArray.remove('UDP')
for i in range(len(udpArray)):
    udpArray[i] = udpArray[i].split(',')


#fifth column
desArray = sheet.col_values(4)
desArray.remove('description')

size = len(indexArray)

for i in range(size):
##    print(tcpArray[i])
##    print(len(tcpArray[i]))
    print("#")
    if(tcpArray[i][0]==""):
        protocol_type = "udp"
        protocol_array = udpArray[i]
    else:
        protocol_type = "tcp"
        protocol_array = tcpArray[i]
    config = "ip service-set "+serviceArray[i]+" type object"
    print(config)
    if(desArray[i]!=""):
        print("    description "+ desArray[i])

##    print(protocol_type)

    for j in range(len(protocol_array)):
        protocol_array[j]=str(protocol_array[j]).split("-")
        if(len(protocol_array[j])==2):
            service_code = "    service "+str(j)+" protocol "+protocol_type+" destination-port "+protocol_array[j][0]+" to "+protocol_array[j][1]
        else:
            service_code = "    service "+str(j)+" protocol "+protocol_type+" destination-port "+protocol_array[j][0]
        print(service_code)
    print("#")
