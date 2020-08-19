

import shutil
import os
import time
import datetime
import TTA_File_Transfer_Assignment_GUI as ftagui

source = '/Users/ywing/Desktop/FileHolder/'
destination = '/Users/ywing/Desktop/FileReceiver/'

def sortFile():
    fPathList = os.listdir(source)                                      #Lists all files in source directory ex: 'filename.txt')
    fullPathAndModTime = {}                                             #Creates an empty set/dictionary
    timeNow = datetime.datetime.now()                                   #Creates variable of current time ex: 2020-08-19 11:52:15.096446
    last24Hours = timeNow - datetime.timedelta(hours = 24)              #Creates variable of time 24 hours ago time ex: 2020-08-18 11:52:15.096446
    filesToSend = []                                                    #Creates an empty List
    for i in fPathList:
        fullPath = os.path.join(source,i)                               #Gets full path with file name in folder: 'directory/file.ext'
        modificationTime = os.path.getmtime(fullPath)                   #Gets modification time of file since last epoch: '1596312495.2747788'
        modTime = time.ctime(modificationTime)                          #Gets modification time in a better format: 'WkD Mon D# Hr:Min:Sec Year'
        structuredModTime = datetime.datetime.strptime(modTime, "%c")   #Changes the MOD time to a datetime object: 'Year-Month-Day Hr:Min:Sec'
        fullPathAndModTime[i] = structuredModTime                       #Adds the full path and datetime mod time as key value pairs to a dictionary: 'directory/file.ext' : 'Year-Month-Day Hr:Min:Sec'
    for i in fullPathAndModTime.values():                               #Compares the datetime mod time to current time
        if i >= last24Hours and i <= timeNow:
            for key, val in fullPathAndModTime.items():
                if val == i:
                    filesToSend.append(key)
    for i in filesToSend:
            shutil.copy(source+i, destination)


if __name__ == "__main__":
    sortFile()