# -*— coding:utf-8 -*-

import os
import time

#1、需要备份的文件目录与目录将被指定在一个列表中。
#例如在：Windows系统下：
#source = ['"C:\\My Documents"', 'C:\\Code']

source = ['/Users/user/Desktop/backup-test/source']

target_dir = '/Users/user/Desktop/backup-test/target'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:>>>>>>')
if os.system(zip_command) == 0:
    print('Successfully backup to', target)
else:
    print('Backup FAILED!!!')

