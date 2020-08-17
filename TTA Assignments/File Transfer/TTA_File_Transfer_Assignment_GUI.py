
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import TTA_File_Transfer_Assignment as fta

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(800, 190))
        self.master.title('Check files')

        self.varBrowse1 = tk.StringVar()
        self.varBrowse2 = tk.StringVar()

        self.btnBrowse1 = tk.Button(self.master, text='Source File', width=12, height=1, command=self.Browse1)
        self.btnBrowse1.grid(row=1, column=0, padx=(30,0), pady=(60,0), sticky=SE)
        self.btnBrowse2 = tk.Button(self.master, text='Destination File', width=12, height=1, command=self.Browse2)
        self.btnBrowse2.grid(row=2, column=0, padx=(30,0), pady=(10,0), sticky=SE)
        self.btnCheckFile = tk.Button(self.master, text='File Check', width=12, height=2, command=fta.moveFile)
        self.btnCheckFile.grid(row=3, column=0, padx=(30,0), pady=(10,0), sticky=SE)
        self.btnCloseProgram = tk.Button(self.master, text='Close Program', width=12, height=2, command= self.cancel)
        self.btnCloseProgram.grid(row=3, column=3, padx=(30,30), pady=(10,0), sticky=SE)
        

        self.txtBrowse1 = Entry(self.master, text=self.varBrowse1, font=("Helvetica", 10), fg='black')
        self.txtBrowse1.grid(row=1, column=1, columnspan=4, padx=(30,30), pady=(60,0), sticky=W+E+N+S)
        self.txtBrowse2 = Entry(self.master, text=self.varBrowse2, font=("Helvetica", 10), fg='black')
        self.txtBrowse2.grid(row=2, column=1, columnspan=4, padx=(30,30), pady=(10,0), sticky=W+E+N+S)
        root.grid_columnconfigure(3, weight=1)
        
    def cancel(self):
        self.master.destroy()

    def Browse1(self):
        self.varBrowse1.set(tk.filedialog.askdirectory())

    def Browse2(self):
        self.varBrowse2.set(tk.filedialog.askdirectory())
        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
                    
                              
