# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import subprocess
Qstring, dict = '', {}
def cutstring(string, referans, start='"', end='"'):
    return string[string.find(start, string.find(referans)+len(referans))+len(start):string.find(end,
                    string.find(start, string.find(referans)+len(referans))+len(start))]
proc = subprocess.Popen(['sudo', 'blkid', '-c', '/dev/null'],stdout=subprocess.PIPE)
for ij in range(0, 10, +1):
  line = proc.stdout.readline()
  if len(line.rstrip()) is not 0:
    uid, typ  = cutstring(str(line.rstrip()), 'UUID') + ' ' + '/media/' + cutstring(str(line.rstrip()), 'UUID') , cutstring(str(line.rstrip()), 'TYPE')
    dict[ij] = {'UUID':uid, 'TYPE':typ}
  else:
    break
for pt in range(0, len(dict), +2):
    uid, typ, ect = 'UUID=' + '"' + dict[pt]['UUID'] + '"', '' + '"' + dict[pt]['TYPE'] + '"', 'defaults, noatime  0  0'
    Qstring = Qstring + uid + ' ' + typ + ' ' + ect + '\n'
print (Qstring.replace('"',''))
