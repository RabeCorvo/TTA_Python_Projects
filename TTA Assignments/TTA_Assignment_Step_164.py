#
# Python:   3.8.5
#
# Author:   Sam Breidenbach
#
# Purpose:  Create a dB using Python and adding specific
#           files to it.

import sqlite3


def dbFunction():
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    fileExtension = '.txt'
    conn = sqlite3.connect('ttaAssignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute(" \
        CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
        for file in fileList:
            if fileExtension in file:
                cur.execute("INSERT INTO tbl_fileList (col_filename) VALUES(?)", \
                            (file,))
                conn.commit()
                print(file)
    conn.close()       
        

if __name__ == "__main__":
    dbFunction()
