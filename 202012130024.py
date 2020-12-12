import os
from os.path import expanduser
from tkinter import *
import requests
import time
def download(url,path,filename):
    if not os.path.isdir(path):
        os.makedirs(path)
    url = 'https://drive.google.com/uc?export=download&id='+url
    print(url)
    r = requests.get(url, allow_redirects=True)
    print(path+filename)
    open(path+filename, 'wb').write(r.content)
def showwindow():
    a = Tk()
    a.geometry('480x720')
    a.title('哈哈指令團應用程式正在更新')
    photo_logo = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/public/HHCGLOGO.png")
    photo = {}
    photo[1] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-0.png")
    photo[2] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-4.png")
    photo[3] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-8.png")
    photo[4] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-12.png")
    photo[5] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-16.png")
    photo[6] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-20.png")
    photo[7] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-24.png")
    photo[8] = PhotoImage(file=expanduser("~")+"/.HaHaCommandGroup/Resourse/update/frame-28.png")
    a000 = Label(a,text='\n\n\n\n\n')
    def run(self):
        c = 0
        while True:
            time.sleep(0.5)
            if c < 8:
                a.update()
                c+=1
                a002.configure(image=photo[c])
            elif c == 8:
                a.update()
                c=1
                a002.configure(image=photo[c])
    a001 = Label(a,text='\n指令下載器正在更新中，請稍後...\n',font=(False,15))
    LOGO = Label(a,image=photo_logo)
    a002 = Label(a,image=photo[1])
    a003 = Label(a,text='\n\n\n\n\nThis program made by north-bear in HaHaCommandGroup.\nAny people can edit the program in non-profit premise.',font=(False,8))
    a000.pack(side='top')
    LOGO.pack(side='top')
    a001.pack(side='top')
    a002.pack(side='top')
    a003.pack(side='top')
    a.after(0, run, 0)
    a.mainloop()
def update():
    showwindow()
    print('update')
def start():
    print('start')
def init():
    home = expanduser("~")
    if os.path.isfile(home+"/.HaHaCommandGroup/DatapackDownloader/version"):
        f = open(home+"/.HaHaCommandGroup/DatapackDownloader/version",'r')
        download('16c2CZXx4lPBR1iB1KZdR55rNdxrLchKQ',home+'/.HaHaCommandGroup/DatapackDownloader/temp/','.ver')
        b = f.read()
        f.close()
        g = open(home+"/.HaHaCommandGroup/DatapackDownloader/temp/.ver",'r')
        a = g.read()
        g.close()
        print(a)
        print(b)
        if not a == b:
            update()
        else:
            start()
    else:
        update()
init()
