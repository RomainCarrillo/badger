import os
from datetime import datetime

path = 'badging.txt'
isExistingFile = os.path.exists(path)

if not isExistingFile :
    f = open(path,'a')
    f.writelines('########## BADGING ##########' + '\n')

f = open(path, 'r')
last_line = f.readlines()[-1]
today = datetime.today().strftime('%Y-%m-%d')
now_hour = datetime.now().strftime('%H:%M:%S')

print(last_line)
if not last_line.startswith(today) :
    f = open(path, 'a')
    f.writelines('\n' + today + ' | am-arrival | ' + now_hour + ' | ')
    f.close()
    quit()
if not last_line.__contains__('am-departure') :
    f = open(path, 'a')
    f.write('am-departure | ' + now_hour + ' | ')
    f.close()
    quit()
if not last_line.__contains__('pm-arrival') :
    f = open(path, 'a')
    f.write('pm-arrival | ' + now_hour + ' | ')
    f.close()
    quit()
if not last_line.__contains__('pm-departure') :
    f = open(path, 'a')
    f.write('pm-departure | ' + now_hour + ' | \n')
    f.close()
    quit()