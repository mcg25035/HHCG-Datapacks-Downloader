import requests, zipfile, threading
from tkinter import *
import os, win32api
TEMP = os.environ['TEMP'] + '\\hhcg\\luncher'
if os.path.isdir(TEMP):
    TEMP = TEMP + '\\'
    with zipfile.ZipFile('HHCGDSL.hrp', 'r') as (myzip):
        for file in myzip.namelist():
            myzip.extract(file, TEMP)

else:
    os.makedirs(TEMP)
    TEMP = TEMP + '\\'
    with zipfile.ZipFile('HHCGDSL.hrp', 'r') as (myzip):
        for file in myzip.namelist():
            myzip.extract(file, TEMP)

def update():
    print('更新中')
    aURL = 'https://www.dropbox.com/s/hbqts9su61x8evh/update.zip?dl=1'
    r = requests.get(aURL, allow_redirects=True)
    open('update.zip', 'wb').write(r.content)
    with zipfile.ZipFile('update.zip', 'r') as (myzip):
        for file in myzip.namelist():
            myzip.extract(file, '')

    win32api.ShellExecute(0, 'open', 'HHCG_datapacks_download.exe', '', '', 0)
    tkWindow.destroy()


if os.path.exists('_.ver'):
    f = open('_.ver', 'r')
    a = f.read()
    URL = 'https://drive.google.com/u/1/uc?id=1rcGSpZAVOpjlo05aBlUc0nWRhZZo6KZ0&export=download'
    r = requests.get(URL, allow_redirects=True)
    open('last.version', 'wb').write(r.content)
    fn = open('last.version', 'r')
    an = fn.read()
    if an == a:
        win32api.ShellExecute(0, 'open', 'HHCG_datapacks_download.exe', '', '', 0)
    else:
        print(an)
        tkWindow = Tk()
        tkWindow.geometry('400x400')
        tkWindow.resizable(False, False)
        tkWindow.title('哈哈指令團指令包下載器更新')
        im1 = PhotoImage(file=(TEMP + '\\\\logo.imagefile.res'))
        im2 = PhotoImage(file=(TEMP + '\\\\text.imagefile.res'))
        Label0 = Label(tkWindow, text='\n\n\n\n').pack(side='top')
        imgLabel0 = Label(tkWindow, image=im1)
        imgLabel0.pack(side='top')
        imgLabel1 = Label(tkWindow, image=im2)
        imgLabel1.pack(side='top')
        th = threading.Thread(target=update)
        th.daemon = True
        th.start()
        tkWindow.mainloop()
else:
    tkWindow = Tk()
    tkWindow.geometry('400x400')
    tkWindow.resizable(False, False)
    tkWindow.title('哈哈指令團指令包下載器更新')
    im1 = PhotoImage(file=(TEMP + '\\\\logo.imagefile.res'))
    im2 = PhotoImage(file=(TEMP + '\\\\text.imagefile.res'))
    Label0 = Label(tkWindow, text='\n\n\n\n').pack(side='top')
    imgLabel0 = Label(tkWindow, image=im1)
    imgLabel0.pack(side='top')
    imgLabel1 = Label(tkWindow, image=im2)
    imgLabel1.pack(side='top')
    th = threading.Thread(target=update)
    th.daemon = True
    th.start()
    tkWindow.mainloop()
