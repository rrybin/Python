import paramiko
import os
import subprocess
import re
import itertools
#Работа с CISCO по SSH
HOSTNAME = '192.168.2.1'
PORT = 22
USERNAME = 'python'
PASSWORD = '2b9psEImVL'

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=HOSTNAME,port=PORT,username=USERNAME,password=PASSWORD)
stdin, stdout, stderr = client.exec_command('show ip dhcp binding | include Vlan32')

data_string = stdout.read().decode()
client.close()

data_list = data_string.split('\r\n')
for x in range(6):
    data_list.pop(0)
data_list.pop(-1)

reg_ip_add = re.compile(r'\d{3}.\d{3}.\d{1,3}.\d{1,3}')
reg_mac_add = re.compile(r'\w{4}.\w{4}.\w{4}.\w{0,2}')
ip_mac_list = []
for line in data_list:
    temp_list = []
    temp_list.append(reg_ip_add.search(line).group(0).replace(' ',''))
    temp_list.append(reg_mac_add.search(line).group(0).replace(' ',''))
    ip_mac_list.append(temp_list)

#Работ с событиями vm-nps при помощи PowerShell
psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                              '-ExecutionPolicy',
                              'Unrestricted',
                              './get_event.ps1'], cwd=os.getcwd(), stdout=subprocess.PIPE)

result = psxmlgen.stdout.read().decode()

list_all = set(result.split('\r\n'))

list_second = []
reg_mac_add = re.compile(r'\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}')
for line in list_all: #Удаляем записи не имеющие mac адреса и разбиваем список
    if reg_mac_add.search(line) is not None:
        list_second.append(line.split(' '))

list_four = []
for line in list_second:
    list_therd = []
    for line_2 in line:
        if line_2 != "":
            if line_2.find(chr(92)) != -1: #приведение логин к стандартному виду
                line_2 = line_2[line_2.find(chr(92))+1:]+'@upnk.kz'
            elif line_2.find(chr(92)) == -1 and line_2.find('@') == -1 and line_2.find('-') == -1:
                line_2 = line_2 + '@upnk.kz'
            elif line_2.find('-') != -1: #Приведение mac адреса к формату cisco
                line_2 = '01'+line_2.replace('-','').casefold()
                line_2 = line_2[0:4]+'.'+line_2[4:8]+'.'+line_2[8:12]+'.'+line_2[12:]
            list_therd.append(line_2)
    list_four.append(list_therd)

#Создание результирующего листа с сортировкой и удалением повторяющихся записей
list_four.sort()
list_result = list(list_four for list_four,_ in itertools.groupby(list_four))

#Сопоставляем два списка по mac адресам
for line in list_result:
    for line_2 in ip_mac_list:
        if line[1] in line_2:
            line.append(line_2[0])

for line in list_result:
    print(line)
