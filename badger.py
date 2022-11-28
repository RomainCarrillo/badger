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
now_hour = datetime.now()
now_hour_string = now_hour.strftime('%H:%M:%S')

print(last_line)
if not last_line.startswith(today) :
    f = open(path, 'a')
    f.writelines('\n' + today + ' | am-arrival | ' + now_hour_string + ' | ')
    f.close()
    quit()
if not last_line.__contains__('am-departure') :
    f = open(path, 'a')
    f.write('am-departure | ' + now_hour_string + ' | ')
    f.close()
    quit()
if not last_line.__contains__('pm-arrival') :
    f = open(path, 'a')
    f.write('pm-arrival | ' + now_hour_string + ' | ')
    f.close()
    quit()
if not last_line.__contains__('pm-departure') :
    f = open(path, 'a')
    f.write('pm-departure | ' + now_hour_string + ' | ')

    splitLine = last_line.split(' | ')
    am_arrival = datetime.combine(datetime.today(), datetime.time(datetime.strptime(splitLine[2], '%H:%M:%S')))
    am_departure = datetime.combine(datetime.today(), datetime.time(datetime.strptime(splitLine[4], '%H:%M:%S')))
    pm_arrival = datetime.combine(datetime.today(), datetime.time(datetime.strptime(splitLine[6], '%H:%M:%S')))
    pm_departure = now_hour
    
    morning_hours = am_departure - am_arrival
    aftenoon_hours = pm_departure - pm_arrival
    daily_hours = morning_hours + aftenoon_hours
    hours = daily_hours.total_seconds() / 3600
    daily_hours_string = str(round((daily_hours.total_seconds() / 3600),1))
    f.write('daily-hours | ' + daily_hours_string + ' | \n')

    f.close()
    quit()