import tkinter as tk
import right_clicks
count=0
def menu_start(event,root,rc):
    widget=event.widget

    def first_time():
        if(widget.winfo_class()=="Button"):
            global count
            if(count==0):
                rc.delete('all')
                count+=1
            #rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)



            rc.place(x=widget.winfo_x()+event.x+105,y=widget.winfo_y()+event.y+120)
            def sample():
                print('working')

            #r.bind('<Button-1>',sample)


            # btn_id_text=tk.Label(rc,text="Id",bd=0,background="#f7f7f7")
            # btn_id_text.place(x=32,y=5)
            # btn_id_entry=tk.Entry(rc,bd=0.5,background="#f7f7f7",width=20,show="Button id")
            # btn_id_entry.place(x=15,y=10)

            r1=rc.create_rectangle(30,0,155,20,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt1=rc.create_text(32,10,text="Button Id",anchor='w',tag='id')
            def hover_in(event):
                rc.itemconfig(r1,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r1,fill="#f7f7f7")
            def onclick(event,arg):
                right_clicks.button_id(event,arg)

            rc.tag_bind(rt1,"<Enter>",hover_in)
            rc.tag_bind(rt1,"<Leave>",hover_out)
            rc.tag_bind(r1,"<Button-1>",lambda event,arg=rc:onclick(event,arg))
            rc.tag_bind(rt1,"<Button-1>",lambda event,arg=rc:onclick(event,arg))



            r2=rc.create_rectangle(30,20,155,40,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt2=rc.create_text(32,30,text="Copy",anchor='w')

            def hover_in(event):
                rc.itemconfig(r2,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r2,fill="#f7f7f7")
            rc.tag_bind(rt2,"<Enter>",hover_in)
            rc.tag_bind(rt2,"<Leave>",hover_out)


            r3=rc.create_rectangle(30,40,155,60,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt3=rc.create_text(32,50,text="Last Widget Properties",anchor='w')
            def hover_in(event):
                rc.itemconfig(r3,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r3,fill="#f7f7f7")
            rc.tag_bind(rt3,"<Enter>",hover_in)
            rc.tag_bind(rt3,"<Leave>",hover_out)


            r4=rc.create_rectangle(30,60,155,80,tag='delete',fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt4=rc.create_text(32,70,tag='delete',text="Delete",anchor='w')
            def hover_in(event):
                rc.itemconfig(r4,fill="#d9d9d9")
                rc.tag_bind(rt4,"<Button-1>",click_copy)
                rc.tag_bind(r4,"<Button-1>",click_copy)
            def hover_out(event):
                rc.itemconfig(r4,fill="#f7f7f7")
            def click_copy(event):
                print()
            rc.tag_bind(rt4,"<Enter>",hover_in)
            rc.tag_bind(rt4,"<Leave>",hover_out)



            r5=rc.create_rectangle(30,80,155,100,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt5=rc.create_text(32,90,text="Change Name",anchor='w')
            def hover_in(event):
                rc.itemconfig(r5,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r5,fill="#f7f7f7")
            rc.tag_bind(rt5,"<Enter>",hover_in)
            rc.tag_bind(rt5,"<Leave>",hover_out)


            r6=rc.create_rectangle(30,100,155,120,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt6=rc.create_text(32,110,text="Command",anchor='w')
            def hover_in(event):
                rc.itemconfig(r6,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r6,fill="#f7f7f7")
            rc.tag_bind(rt6,"<Enter>",hover_in)
            rc.tag_bind(rt6,"<Leave>",hover_out)


            r7=rc.create_rectangle(30,120,155,140,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt7=rc.create_text(32,130,text="Select All Widget",anchor='w')
            def hover_in(event):
                rc.itemconfig(r7,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r7,fill="#f7f7f7")
            rc.tag_bind(rt7,"<Enter>",hover_in)
            rc.tag_bind(rt7,"<Leave>",hover_out)


            r8=rc.create_rectangle(30,140,155,160,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt8=rc.create_text(32,150,text="Select All",anchor='w')
            def hover_in(event):
                rc.itemconfig(r8,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r8,fill="#f7f7f7")
            rc.tag_bind(rt8,"<Enter>",hover_in)
            rc.tag_bind(rt8,"<Leave>",hover_out)


            r9=rc.create_rectangle(30,160,155,180,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt9=rc.create_text(32,170,text="Default Size",anchor='w')
            def hover_in(event):
                rc.itemconfig(r9,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r9,fill="#f7f7f7")
            rc.tag_bind(rt9,"<Enter>",hover_in)
            rc.tag_bind(rt9,"<Leave>",hover_out)

        if(widget.winfo_class()=="Entry"):
            global count
            if(count==0):
                rc.delete('all')
                count+=1
            #rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)



            rc.place(x=widget.winfo_x()+event.x+105,y=widget.winfo_y()+event.y+120)
            def sample():
                print('working')

            #r.bind('<Button-1>',sample)



            r1=rc.create_rectangle(30,0,155,20,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt1=rc.create_text(32,10,text="Entry Id",anchor='w',tag='id')
            def hover_in(event):
                rc.itemconfig(r1,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r1,fill="#f7f7f7")
            rc.tag_bind(rt1,"<Enter>",hover_in)
            rc.tag_bind(rt1,"<Leave>",hover_out)

            r2=rc.create_rectangle(30,20,155,40,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt2=rc.create_text(32,30,text="Copy",anchor='w')

            def hover_in(event):
                rc.itemconfig(r2,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r2,fill="#f7f7f7")
            rc.tag_bind(rt2,"<Enter>",hover_in)
            rc.tag_bind(rt2,"<Leave>",hover_out)


            r3=rc.create_rectangle(30,40,155,60,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt3=rc.create_text(32,50,text="Last Widget Properties",anchor='w')
            def hover_in(event):
                rc.itemconfig(r3,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r3,fill="#f7f7f7")
            rc.tag_bind(rt3,"<Enter>",hover_in)
            rc.tag_bind(rt3,"<Leave>",hover_out)


            r4=rc.create_rectangle(30,60,155,80,tag='delete',fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt4=rc.create_text(32,70,tag='delete',text="Delete",anchor='w')
            def hover_in(event):
                rc.itemconfig(r4,fill="#d9d9d9")
                rc.tag_bind(rt4,"<Button-1>",click_copy)
                rc.tag_bind(r4,"<Button-1>",click_copy)
            def hover_out(event):
                rc.itemconfig(r4,fill="#f7f7f7")
            def click_copy(event):
                print()
            rc.tag_bind(rt4,"<Enter>",hover_in)
            rc.tag_bind(rt4,"<Leave>",hover_out)



            r5=rc.create_rectangle(30,80,155,100,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt5=rc.create_text(32,90,text="Select All Widget",anchor='w')
            def hover_in(event):
                rc.itemconfig(r5,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r5,fill="#f7f7f7")
            rc.tag_bind(rt5,"<Enter>",hover_in)
            rc.tag_bind(rt5,"<Leave>",hover_out)


            r6=rc.create_rectangle(30,100,155,120,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt6=rc.create_text(32,110,text="Select All",anchor='w')
            def hover_in(event):
                rc.itemconfig(r6,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r6,fill="#f7f7f7")
            rc.tag_bind(rt6,"<Enter>",hover_in)
            rc.tag_bind(rt6,"<Leave>",hover_out)


            r7=rc.create_rectangle(30,120,155,140,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
            rt7=rc.create_text(32,130,text="Default Size",anchor='w')
            def hover_in(event):
                rc.itemconfig(r7,fill="#d9d9d9")
            def hover_out(event):
                rc.itemconfig(r7,fill="#f7f7f7")
            rc.tag_bind(rt7,"<Enter>",hover_in)
            rc.tag_bind(rt7,"<Leave>",hover_out)



            rc.update()
            count=0
            # rc.addtag_all('new')
   # event.widget.bind('<Button-1>',lambda event,arg=root,arg2=rc:menu_close(event,arg,arg2))
    first_time()


#def menu_close(event,root,rc):
#    widget=event.widget


