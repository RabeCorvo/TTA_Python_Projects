import shutil
import os
import time
import datetime
import TTA_File_Transfer_Assignment_GUI as ftaGUI


def moveFile():
    source = ftaGUI.varBrowse1.get()
    destination = ftaGUI.varBrowse2.get()
    filesToSend = sortFile()   
    for i in filesToSend:
            shutil.copy(source+i, destination)
   
def sortFile():
    source = ftaGUI.varBrowse1.get()
    fPathList = os.listdir(source)
    fullPathAndModTime = {}
    timeNow = datetime.datetime.now()
    last24Hours = timeNow - datetime.timedelta(hours = 24)
    filesToSend = []
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
    return filesToSend


if __name__ == "__main__":
    moveFile()
