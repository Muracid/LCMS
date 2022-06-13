import os
import shutil
import sched, time
s = sched.scheduler(time.time, time.sleep)
path_LCMS= 'W:/...LCMS...'
path_home = 'C:/.../My_LCMS'
from datetime import datetime
now = datetime.now()
today = now.strftime ("%Y-%m-%d")
todays_files = path_LCMS + '/' + today
todays_files_mine = path_home + '/' + today
folders_in = os.listdir(todays_files)
# Create the folder on my PC
def folder():
    today_folder = path_home + '/' + today
    if not os.path.exists(today_folder):
        os.makedirs(today_folder)
        print ('created a new folder for today')
folder()
My_files = []
for files in folders_in:
    if files.startswith('2021-MR-'):
        My_files.append(files)
#print(My_files)

def transfer ():
    for my_run in My_files:
        temp0 = todays_files + '/'+ my_run
        temp = todays_files_mine + '/' + my_run
        if not os.path.exists(temp):
            shutil.copytree(temp0, temp)
            print (temp[50:])
transfer()
print ('done')


