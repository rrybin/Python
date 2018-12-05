Get-WinEvent -ComputerName 192.168.3.20 -FilterHashTable @{LogName="Security";ID = 6278} | 
Select @{n="User";e={([xml]$_.ToXml()).Event.EventData.Data | ? {$_.Name -eq "SubjectUserName"} | 
%{$_.'#text'}}}, @{n="MAC";e={([xml]$_.ToXml()).Event.EventData.Data | ? {$_.Name -eq "CallingStationID"} | 
%{$_.'#text'}}} | Select-Object -First 1

27 	[Graph Report] 	192.168.32.79 	1 440 	150.7 M 	0.9% 	?
['n.uahit@upnk.kz', '01bc.5451.1a82.22', '192.168.32.79']

50 	[Graph Report] 	n.uahit@upnk.kz 	324 	39.1 M 	0.2% 	Сектор маркетинга