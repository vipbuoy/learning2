#this program is made for taking backup of your any file to a specific location!
import os,zipfile,time
from pathlib import Path as p
def backup(drive,ddrive):
    temp=os.path.basename(drive)
    ddrive=ddrive+'\\'+temp+'.zip'
    back=zipfile.ZipFile(ddrive,'w')
    print('working...')
    for path,foldername,filenames in os.walk(drive):
        back.write(path)
        for f in filenames:
            back.write(os.path.join(path,f))
    back.close()        
    print('Done!')    


drive=input('Enter drive:')
drive=drive+':'
while True:
    folder=input('Enter name of folder:')
    drive=drive+'\\'+folder
    if not os.path.exists(drive) or p(drive).is_file():
        print('ERROR!')
        time.sleep(3)
        exit()
    y=input('is this end?(y/n)')
    if y=='y' or y=='Y':
        break
ddrive=input('Enter destination drive:')
ddrive=ddrive+':'
while True:
    if not os.path.exists(ddrive) or p(ddrive).is_file():
        print('ERROR!')
        time.sleep(3)
        exit()
    y=input('is this end?(y/n)')
    
    if y=='y' or y=='Y':
        break
    folder=input('Enter name of folder:')
    ddrive=ddrive+'\\'+folder
   

backup(drive,ddrive)    
