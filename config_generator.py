import xlrd
import xlwt
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from xlutils.copy import copy
from xlrd import open_workbook

workbook = xlrd.open_workbook('config_file.xlsx')
sheet = workbook.sheet_by_name('test')

#first column: Index
index_array = sheet.col_values(0)
index_array.remove('index')

#second column: Service_Set_(new)
service_name_array = sheet.col_values(1)
service_name_array.remove('Service_Set_(new)')

#third column: TCP
tcp_array = sheet.col_values(2)
tcp_array.remove('TCP')
for i in range(len(tcp_array)):
    tcp_array[i] = tcp_array[i].split(',')

#fourth column: UDP
udp_array = sheet.col_values(3)
udp_array.remove('UDP')
for i in range(len(udp_array)):
    udp_array[i] = udp_array[i].split(',')


#fifth column: description
desc_array = sheet.col_values(4)
desc_array.remove('description')

size = len(index_array)

config_array = []

for i in range(size):
    config_array.append([])
    config_array[i].append("#")
    if(tcp_array[i][0]==""):
        protocol_type = "udp"
        protocol_array = udp_array[i]
    else:
        protocol_type = "tcp"
        protocol_array = tcp_array[i]
    config = "ip service-set "+service_name_array[i]+" type object"
    config_array[i].append(config)
    if(desc_array[i]!=""):
        desc_line = "    description "+ desc_array[i]
        config_array[i].append(desc_line)

    for j in range(len(protocol_array)):
        protocol_array[j]=str(protocol_array[j]).split("-")
        if(len(protocol_array[j])==2):
            service_code = "    service "+str(j)+" protocol "+protocol_type+" destination-port "+protocol_array[j][0]+" to "+protocol_array[j][1]
        else:
            service_code = "    service "+str(j)+" protocol "+protocol_type+" destination-port "+protocol_array[j][0]
        config_array[i].append(service_code)
    config_array[i].append("#")

file = "config_file_test.xlsx"
workbook = load_workbook(filename = file)
worksheet = workbook.get_sheet_by_name("test")
print(len(config_array))
for x in range(len(index_array)):
    write_string = ''
    for j in range(len(config_array[x])):
        write_string = write_string + config_array[x][j]+"\n"
    #print(write_string)
##    worksheet.cell(row = x+1, column = 6, value = write_string)
    worksheet['F1']='Configuration'
    worksheet['F'+str(x+2)]=write_string
    print(x+1)
            
workbook.save(filename = file)
