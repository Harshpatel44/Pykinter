import tkinter as tk

count=0
def menu_start(event,root,rc):
    widget=event.widget

    def first_time():
        global count
        if(count==0):
            rc.delete('all')
            count+=1
        #rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)



        rc.place(x=widget.winfo_x()+event.x+105,y=widget.winfo_y()+event.y+120)
        rc.create_line(4,20,120,20)
        rc.create_line(4,40,120,40)
        rc.create_line(4,60,120,60)
        rc.create_line(4,80,120,80)
        rc.create_line(4,100,120,100)
        rc.create_line(4,120,120,120)
        rc.create_line(4,140,120,140)
        rc.create_line(4,160,120,160)
        rc.create_line(4,180,120,180)
        # copy_text=tk.Label(rc,tag='harsh',text="Copy")
        # copy_text.pack()
        # copy_last=tk.Label(rc,tag='harsh',text="Properties of Last Widget")
        # copy_last.pack()
        rc.update()
        count=0
        # rc.addtag_all('new')

    first_time()
def menu_close(event,root,rc):
    widget=event.widget

    rc.place_forget()
