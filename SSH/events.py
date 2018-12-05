import os
import subprocess
import re

psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             './get_event.ps1'], cwd=os.getcwd(), stdout=subprocess.PIPE)

result = psxmlgen.stdout.read().decode()

list_all = result.split('\r\n')

list_user_mac = list_all.pop(3)

reg_mac_add = re.compile(r'\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}')

mac = (reg_mac_add.search(list_user_mac).group(0).replace(' ', ''))

login = list_user_mac[:list_user_mac.find(' ')]
#Удаление лишних записей (UPNK/) добавление префикса @upnk.kz
if login.find(chr(92)) != -1:
    login = login[login.find(chr(92))+1:]+'@upnk.kz'
elif login.find(chr(92)) == -1 and login.find('@') == -1:
    login = login + '@upnk.kz'
print(login)

mac = '01'+mac.replace('-','').casefold()
print(mac)
mac = mac[0:4]+'.'+mac[4:8]+'.'+mac[8:12]+'.'+mac[12:]
print(mac)



