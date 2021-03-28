__author__ = 'Harsh'

from old.program_editor import update, all_codes
import tkinter as tk
import os
def editor(self,main,frame1,frame2):
    data=''
    def updt(event):
        global data

        data= all_codes.init_part + update.sync_data()
        a.insert(tk.END,"import " + all_codes.import_part[0])
        a.insert(tk.END,data)
        a.insert(tk.END, all_codes.frame2_s)
        a.insert(tk.END, all_codes.mainloop)
    syncbutton=tk.Button(frame2,text="Sync")
    syncbutton.bind('<Button-1>',updt)
    syncbutton.pack(side='top')

    def save():
        f=open('../new_file.py', 'w')
        f.write(a.get(1.0,tk.END))

    savebutton=tk.Button(frame2,text='Save',command=save)
    savebutton.pack(side='top')

    def run():
        os.system('python new_file.py')

    runbutton=tk.Button(frame2,text='Run',command=run)
    runbutton.pack(side='top')
    a=tk.Text(frame2,width=2000,height=500)




    a.pack(expand=True,fill='both')





def left_side(self,main,frame1,frame2):
    print()