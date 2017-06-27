import xlrd
import xlwt

workbook = xlrd.open_workbook('config_file.xlsx')
sheet = workbook.sheet_by_name('test')

indexArray = sheet.col_values(0)
indexArray.remove('index')

serviceArray = sheet.col_values(1)
serviceArray.remove('Service_Set_(new)')

tcpArray = sheet.col_values(2)
tcpArray.remove('TCP')
tcpArray[0] = tcpArray[0].split(',')
udpArray = sheet.col_values(3)
udpArray.remove('UDP')

desArray = sheet.col_values(4)
desArray.remove('description')

for i in range (len(indexArray)):
    indexArray[i] = i+1



#configuration = "ip service-set "+serviceArray[0]+" type object description "+desArray[0]+"\nservice "+str(indexArray[0]-1)+" protocol TCP destination-port "+tcpArray[0][0]

#print(configuration)
##print(indexArray)
##print(serviceArray)
##print(tcpArray)
##print(udpArray)
##print(desArray)
