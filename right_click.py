import tkinter as tk
import right_clicks
count=0
def menu_start(event,root,rc,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r):
    org_widget=event.widget


    if(org_widget.winfo_class()=="Button"):
        global count
        #if(count==0):
        rc.delete('all')            #deletes the content of canvas first so repetation dont occur each time
        #count+=1
        #rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)



        rc.place(x=org_widget.winfo_x()+event.x+105,y=org_widget.winfo_y()+event.y+120)


        rt1=rc.create_rectangle(30,0,155,20,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte1=rc.create_text(32,10,text="Button Id",anchor='w',tag='id')
        def hover_in(event):
            rc.itemconfig(rt1,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(rt1,fill="#f7f7f7")
        def onclick(event,org_org_widget,arg2):
            right_clicks.button_id(event,org_widget,arg2)       #button_id function invoked

        rc.tag_bind(rte1,"<Enter>",hover_in)
        rc.tag_bind(rte1,"<Leave>",hover_out)
        rc.tag_bind(rt1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))
        rc.tag_bind(rte1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))





        rt2=rc.create_rectangle(30,20,155,40,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte2=rc.create_text(32,30,text="Copy",anchor='w')

        def hover_in(event):
            rc.itemconfig(rt2,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(rt2,fill="#f7f7f7")
        def onclick1(event,org_org_widget,arg2):
           right_clicks.copy(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)              #on click , goes to copy function

        rc.tag_bind(rte2,"<Enter>",hover_in)
        rc.tag_bind(rte2,"<Leave>",hover_out)
        rc.tag_bind(rt2,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick1(event,arg,arg2))
        rc.tag_bind(rte2,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick1(event,arg,arg2))





        r3=rc.create_rectangle(30,40,155,60,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt3=rc.create_text(32,50,text="Copy Widget Properties",anchor='w')

        def hover_in(event):
            rc.itemconfig(r3,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r3,fill="#f7f7f7")
        def onclick2(event,org_org_widget,arg2):
           right_clicks.copy_props(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rt3,"<Enter>",hover_in)
        rc.tag_bind(rt3,"<Leave>",hover_out)
        rc.tag_bind(r3,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick2(event,arg,arg2))
        rc.tag_bind(rt3,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick2(event,arg,arg2))





        r4=rc.create_rectangle(30,60,155,80,tag='delete',fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt4=rc.create_text(32,70,tag='Delete',text="Delete",anchor='w')
        def hover_in(event):
            rc.itemconfig(r4,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r4,fill="#f7f7f7")
        def onclick3(event,org_org_widget,arg2):
           right_clicks.delete(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rt4,"<Enter>",hover_in)
        rc.tag_bind(rt4,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3(event,arg,arg2))
        rc.tag_bind(rt4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3(event,arg,arg2))


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
        rt7=rc.create_text(32,130,text="Select All widget",anchor='w')
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

    if(org_widget.winfo_class()=="Entry"):
        global count
        #if(count==0):
        rc.delete('all')            #deletes the content of canvas first so repetation dont occur each time
        #count+=1
        #rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)



        rc.place(x=org_widget.winfo_x()+event.x+105,y=org_widget.winfo_y()+event.y+120)


        rt1=rc.create_rectangle(30,0,155,20,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte1=rc.create_text(32,10,text="Button Id",anchor='w',tag='id')
        def hover_in(event):
            rc.itemconfig(rt1,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(rt1,fill="#f7f7f7")
        def onclick(event,org_org_widget,arg2):
            right_clicks.button_id(event,org_widget,arg2)       #button_id function invoked

        rc.tag_bind(rte1,"<Enter>",hover_in)
        rc.tag_bind(rte1,"<Leave>",hover_out)
        rc.tag_bind(rt1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))
        rc.tag_bind(rte1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))





        rt2=rc.create_rectangle(30,20,155,40,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte2=rc.create_text(32,30,text="Copy",anchor='w')

        def hover_in(event):
            rc.itemconfig(rt2,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(rt2,fill="#f7f7f7")
        def onclick1(event,org_org_widget,arg2):
           right_clicks.copy(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)              #on click , goes to copy function

        rc.tag_bind(rte2,"<Enter>",hover_in)
        rc.tag_bind(rte2,"<Leave>",hover_out)
        rc.tag_bind(rt2,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick1(event,arg,arg2))
        rc.tag_bind(rte2,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick1(event,arg,arg2))





        r3=rc.create_rectangle(30,40,155,60,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt3=rc.create_text(32,50,text="Copy Widget Properties",anchor='w')

        def hover_in(event):
            rc.itemconfig(r3,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r3,fill="#f7f7f7")
        def onclick2(event,org_org_widget,arg2):
           right_clicks.copy_props(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rt3,"<Enter>",hover_in)
        rc.tag_bind(rt3,"<Leave>",hover_out)
        rc.tag_bind(r3,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick2(event,arg,arg2))
        rc.tag_bind(rt3,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick2(event,arg,arg2))





        r4=rc.create_rectangle(30,60,155,80,tag='delete',fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt4=rc.create_text(32,70,tag='Delete',text="Delete",anchor='w')
        def hover_in(event):
            rc.itemconfig(r4,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r4,fill="#f7f7f7")
        def onclick3(event,org_org_widget,arg2):
           right_clicks.delete(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rt4,"<Enter>",hover_in)
        rc.tag_bind(rt4,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3(event,arg,arg2))
        rc.tag_bind(rt4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3(event,arg,arg2))


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
        rt7=rc.create_text(32,130,text="Select All widget",anchor='w')
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




def menu_close(event,root,rc):
    widget=event.widget
    rc.place_forget()

