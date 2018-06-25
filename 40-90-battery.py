#!/usr/bin/python

import os
import re

# settings
miio = 'miio'
miio_device_id = '88038183'
ceiling = 94
floor = 40

res = os.popen("pmset -g batt").read().replace('\n','')

# level
m = re.match(r'.*\s([0-9]{1,3})%', res)
level = 0
if m != None:
    level = int(m.group(1))

# state
m = re.match(r'.*discharging', res)
discharging = (m != None)

print 'Battery Level: ' + str(level)
print 'Discharging: ' + str(discharging)

cmd = ''
if level>ceiling and not discharging:
    cmd = miio + ' control ' + miio_device_id + ' power false'
    print 'disconnect...'

if level<floor and discharging:
    cmd = miio + ' control ' + miio_device_id + ' power true'
    print 'connect...'

if cmd != '':
    print os.popen(cmd).read()
else:
    print 'do nothing.'