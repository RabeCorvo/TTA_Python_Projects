
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import time
import datetime
import TTA_File_Transfer_Assignment_GUI as ftagui
        
def cancel(self):
        self.master.destroy()

def Browse1(self):
        source = tk.filedialog.askdirectory()
        slash = '/'
        self.txtBrowse1.insert(0,source)
        self.sourceDir = source + '/'

def Browse2(self):
        destination = tk.filedialog.askdirectory()
        self.txtBrowse2.insert(0,destination)
        self.destinationDir = destination + '/'

def sortFile(self):
    source = self.sourceDir
    destination = self.destinationDir
    fPathList = os.listdir(source)                                      #Lists all files in source directory ex: 'filename.txt')
    timeNow = datetime.datetime.now()                                   #Creates variable of current time ex: 2020-08-19 11:52:15.096446
    last24Hours = timeNow - datetime.timedelta(hours = 24)              #Creates variable of time 24 hours ago time ex: 2020-08-18 11:52:15.096446
    filesToSend = []                                                    #Creates an empty List
    for i in fPathList:
        fullPath = os.path.join(source,i)                               #Gets full path with file name in folder: 'directory/file.ext'
        modificationTime = os.path.getmtime(fullPath)                   #Gets modification time of file since last epoch: '1596312495.2747788'
        modTime = time.ctime(modificationTime)                          #Gets modification time in a better format: 'WkD Mon D# Hr:Min:Sec Year'
        structuredModTime = datetime.datetime.strptime(modTime, "%c")   #Changes the MOD time to a datetime object: 'Year-Month-Day Hr:Min:Sec'
        if structuredModTime >= last24Hours and structuredModTime <= timeNow:
                shutil.copy(source+i, destination)

        
if __name__ == "__main__":
    pass
