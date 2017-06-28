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
    if(tcpArray[i][0]==""):
        protocol_type = "udp"
        protocol_array = udpArray[i]
    else:
        protocol_type = "tcp"
        protocol_array = tcpArray[i]
    config = "ip service-set "+serviceArray[i]+" type object description "+ desArray[i]
    print(config)
##    print(protocol_type)

    for j in range(len(protocol_array)):
        service_code = "    service "+str(j)+" protocol "+protocol_type+" destination-port "+str(protocol_array[j])
        print(service_code)






#configuration = "ip service-set "+serviceArray[0]+" type object description "+desArray[0]+"\nservice "+str(indexArray[0]-1)+" protocol TCP destination-port "+tcpArray[0][0]

#print(configuration)
##print(indexArray)
##print(serviceArray)
##print(tcpArray)
##print(udpArray)
##print(desArray)
