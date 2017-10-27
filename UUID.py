# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import subprocess
import os
Qstring, fsStr, dict, uid_list, no_repeat = '', '', {}, [], []
def cutstring(string, referans, start='"', end='"'):
    return string[string.find(start, string.find(referans)+len(referans))+len(start):string.find(end,
                    string.find(start, string.find(referans)+len(referans))+len(start))]
source =  open('/etc/fstab', "r")
for  line in source.readlines():
    fsStr = fsStr + str(line)
proc = subprocess.Popen(['sudo', 'blkid', '-c', '/dev/null'],stdout=subprocess.PIPE)
for ij in range(0, 11, +1):
    line = proc.stdout.readline()
    if len(line.rstrip()) is not 0:
        uid, typ  = cutstring(str(line.rstrip()), 'UUID') + ' ' + '/media/' + cutstring(str(line.rstrip()), 'UUID') , cutstring(str(line.rstrip()), 'TYPE')
        dict[ij] = {'UUID':uid, 'TYPE':typ}
for pt in range(0, len(dict), +1):
    if fsStr.find(dict[pt]['UUID'][0]) is -1:
        uid, typ, ect = 'UUID=' + '"' + dict[pt]['UUID'] + '"', '' + '"' + dict[pt]['TYPE'] + '"', 'auto,users,uid=1000,gid=100,dmask=027,fmask=137,utf8 0 0 '
        Qstring = Qstring + uid + ' ' + typ + ' ' + ect + '\n'
os.system('sudo chmod +777 /etc/fstab')
fsStr = fsStr + '\n' + Qstring.replace('"','')
with open('/etc/fstab', "w") as beta: 
    beta.write(str(fsStr)) 
os.system('sudo chmod 604 /etc/fstab')
