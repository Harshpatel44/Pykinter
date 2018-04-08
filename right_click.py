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


        rc.place(x=org_widget.winfo_x()+event.x,y=org_widget.winfo_y()+event.y+18)


        rt1=rc.create_rectangle(30,0,170,20,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte1=rc.create_text(32,10,text="Button Id",anchor='w',tag='id')
        def hover_in(event):
            rc.itemconfig(rt1,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(rt1,fill="#f7f7f7")
        def onclick(event,org_org_widget,arg2):
            right_clicks.id_change(event,org_widget,arg2)       #button_id function invoked

        rc.tag_bind(rte1,"<Enter>",hover_in)
        rc.tag_bind(rte1,"<Leave>",hover_out)
        rc.tag_bind(rt1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))
        rc.tag_bind(rte1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))





        rt2=rc.create_rectangle(30,20,170,40,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
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





        r3=rc.create_rectangle(30,40,170,60,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte3=rc.create_text(32,50,text="Copy Widget Properties",anchor='w')

        def hover_in(event):
            rc.itemconfig(r3,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r3,fill="#f7f7f7")
        def onclick2(event,org_org_widget,arg2):
           right_clicks.copy_props(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rte3,"<Enter>",hover_in)
        rc.tag_bind(rte3,"<Leave>",hover_out)
        rc.tag_bind(r3,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick2(event,arg,arg2))
        rc.tag_bind(rte3,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick2(event,arg,arg2))





        r4=rc.create_rectangle(30,60,170,80,tag='delete',fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte4=rc.create_text(32,70,tag='Delete',text="Delete",anchor='w')
        def hover_in(event):
            rc.itemconfig(r4,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r4,fill="#f7f7f7")
        def onclick3_b(event,org_org_widget,arg2):
           print('here')
           right_clicks.delete(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)

        rc.tag_bind(rte4,"<Enter>",hover_in)
        rc.tag_bind(rte4,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3_b(event,arg,arg2))
        rc.tag_bind(rte4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3_b(event,arg,arg2))


        r5=rc.create_rectangle(30,80,170,100,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt5=rc.create_text(32,90,text="Change Name",anchor='w')
        def hover_in(event):
            rc.itemconfig(r5,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r5,fill="#f7f7f7")
        def onclick4(event,org_org_widget,arg2):
           right_clicks.change_name(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rt5,"<Enter>",hover_in)
        rc.tag_bind(rt5,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick4(event,arg,arg2))
        rc.tag_bind(rt5,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick4(event,arg,arg2))

        r6=rc.create_rectangle(30,100,170,120,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte6=rc.create_text(32,110,text="Command",anchor='w')
        def hover_in(event):
            rc.itemconfig(r6,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r6,fill="#f7f7f7")
        def onclick5(event,org_org_widget,arg2):
            right_clicks.command(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rte6,"<Enter>",hover_in)
        rc.tag_bind(rte6,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick5(event,arg,arg2))
        rc.tag_bind(rte6,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick5(event,arg,arg2))

        r7=rc.create_rectangle(30,120,170,140,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte7=rc.create_text(32,130,text="Select All Buttons",anchor='w')
        def hover_in(event):
            rc.itemconfig(r7,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r7,fill="#f7f7f7")
        def onclick6(event,org_org_widget,arg2):
            right_clicks.select_all_specific(event,root,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rte7,"<Enter>",hover_in)
        rc.tag_bind(rte7,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick6(event,arg,arg2))
        rc.tag_bind(rte7,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick6(event,arg,arg2))


        r8=rc.create_rectangle(30,140,170,160,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt8=rc.create_text(32,150,text="Select All Widgets",anchor='w')
        def hover_in(event):
            rc.itemconfig(r8,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r8,fill="#f7f7f7")
        rc.tag_bind(rt8,"<Enter>",hover_in)
        rc.tag_bind(rt8,"<Leave>",hover_out)


        r9=rc.create_rectangle(30,160,170,180,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt9=rc.create_text(32,170,text="Default Size",anchor='w')
        def hover_in(event):
            rc.itemconfig(r9,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r9,fill="#f7f7f7")
        rc.tag_bind(rt9,"<Enter>",hover_in)
        rc.tag_bind(rt9,"<Leave>",hover_out)



    if(org_widget.winfo_class()=="Entry"):
        rc.configure(height=157)
        global count
        #if(count==0):
        rc.delete('all')            #deletes the content of canvas first so repetation dont occur each time
        #count+=1
        #rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)



        rc.place(x=org_widget.winfo_x()+event.x,y=org_widget.winfo_y()+event.y+18)


        rt1=rc.create_rectangle(30,0,170,20,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte1=rc.create_text(32,10,text="Entry Id",anchor='w',tag='id')
        def hover_in(event):
            rc.itemconfig(rt1,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(rt1,fill="#f7f7f7")
        def onclick(event,org_org_widget,arg2):
            right_clicks.id_change(event,org_widget,arg2)       #button_id function invoked

        rc.tag_bind(rte1,"<Enter>",hover_in)
        rc.tag_bind(rte1,"<Leave>",hover_out)
        rc.tag_bind(rt1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))
        rc.tag_bind(rte1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))





        rt2=rc.create_rectangle(30,20,170,40,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
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





        r3=rc.create_rectangle(30,40,170,60,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
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





        r4=rc.create_rectangle(30,60,170,80,tag='delete',fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt4=rc.create_text(32,70,tag='Delete',text="Delete",anchor='w')
        def hover_in(event):
            rc.itemconfig(r4,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r4,fill="#f7f7f7")
        def onclick3_e(event,org_org_widget,arg2):
           right_clicks.delete(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rt4,"<Enter>",hover_in)
        rc.tag_bind(rt4,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3_e(event,arg,arg2))
        rc.tag_bind(rt4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3_e(event,arg,arg2))


        # r5=rc.create_rectangle(30,80,155,100,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        # rt5=rc.create_text(32,90,text="Change Name",anchor='w')
        # def hover_in(event):
        #     rc.itemconfig(r5,fill="#d9d9d9")
        # def hover_out(event):
        #     rc.itemconfig(r5,fill="#f7f7f7")
        # rc.tag_bind(rt5,"<Enter>",hover_in)
        # rc.tag_bind(rt5,"<Leave>",hover_out)


        r6=rc.create_rectangle(30,80,170,110,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt6=rc.create_text(32,90,text="Command",anchor='w')
        def hover_in(event):
            rc.itemconfig(r6,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r6,fill="#f7f7f7")
        rc.tag_bind(rt6,"<Enter>",hover_in)
        rc.tag_bind(rt6,"<Leave>",hover_out)


        r7=rc.create_rectangle(30,100,170,120,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt7=rc.create_text(32,110,text="Select All Entry",anchor='w')
        def hover_in(event):
            rc.itemconfig(r7,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r7,fill="#f7f7f7")
        rc.tag_bind(rt7,"<Enter>",hover_in)
        rc.tag_bind(rt7,"<Leave>",hover_out)


        r8=rc.create_rectangle(30,120,170,140,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt8=rc.create_text(32,130,text="Select All",anchor='w')
        def hover_in(event):
            rc.itemconfig(r8,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r8,fill="#f7f7f7")
        rc.tag_bind(rt8,"<Enter>",hover_in)
        rc.tag_bind(rt8,"<Leave>",hover_out)


        r9=rc.create_rectangle(30,140,170,160,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt9=rc.create_text(32,150,text="Default Size",anchor='w')
        def hover_in(event):
            rc.itemconfig(r9,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r9,fill="#f7f7f7")
        rc.tag_bind(rt9,"<Enter>",hover_in)
        rc.tag_bind(rt9,"<Leave>",hover_out)

    if(org_widget.winfo_class()=="Label"):
        global count
        #if(count==0):
        rc.delete('all')            #deletes the content of canvas first so repetation dont occur each time
        #count+=1
        #rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)



        rc.place(x=org_widget.winfo_x()+event.x+105,y=org_widget.winfo_y()+event.y+120)


        rt1=rc.create_rectangle(30,0,170,20,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rte1=rc.create_text(32,10,text="Label Id",anchor='w',tag='id')
        def hover_in(event):
            rc.itemconfig(rt1,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(rt1,fill="#f7f7f7")
        def onclick(event,org_org_widget,arg2):
            right_clicks.id_change(event,org_widget,arg2)       #button_id function invoked

        rc.tag_bind(rte1,"<Enter>",hover_in)
        rc.tag_bind(rte1,"<Leave>",hover_out)
        rc.tag_bind(rt1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))
        rc.tag_bind(rte1,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick(event,arg,arg2))





        rt2=rc.create_rectangle(30,20,170,40,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
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





        r3=rc.create_rectangle(30,40,170,60,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
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





        r4=rc.create_rectangle(30,60,170,80,tag='delete',fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt4=rc.create_text(32,70,tag='Delete',text="Delete",anchor='w')
        def hover_in(event):
            rc.itemconfig(r4,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r4,fill="#f7f7f7")
        def onclick3_l(event,org_org_widget,arg2):
           right_clicks.delete(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)

        rc.tag_bind(rt4,"<Enter>",hover_in)
        rc.tag_bind(rt4,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3_l(event,arg,arg2))
        rc.tag_bind(rt4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick3_l(event,arg,arg2))


        r5=rc.create_rectangle(30,80,170,100,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt5=rc.create_text(32,90,text="Change Name",anchor='w')
        def hover_in(event):
            rc.itemconfig(r5,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r5,fill="#f7f7f7")
        def onclick4(event,org_org_widget,arg2):
           right_clicks.change_name(event,org_widget,arg2,start_btn,motion,stop_btn,l1,l2,right1,right2,u,d,l,r)
        rc.tag_bind(rt5,"<Enter>",hover_in)
        rc.tag_bind(rt5,"<Leave>",hover_out)
        rc.tag_bind(r4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick4(event,arg,arg2))
        rc.tag_bind(rt4,"<Button-1>",lambda event,arg=org_widget,arg2=rc:onclick4(event,arg,arg2))

        r6=rc.create_rectangle(30,100,170,120,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt6=rc.create_text(32,110,text="Command",anchor='w')
        def hover_in(event):
            rc.itemconfig(r6,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r6,fill="#f7f7f7")
        rc.tag_bind(rt6,"<Enter>",hover_in)
        rc.tag_bind(rt6,"<Leave>",hover_out)


        r7=rc.create_rectangle(30,120,170,140,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt7=rc.create_text(32,130,text="Select All Buttons",anchor='w')
        def hover_in(event):
            rc.itemconfig(r7,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r7,fill="#f7f7f7")
        rc.tag_bind(rt7,"<Enter>",hover_in)
        rc.tag_bind(rt7,"<Leave>",hover_out)


        r8=rc.create_rectangle(30,140,170,160,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
        rt8=rc.create_text(32,150,text="Select All Widgets",anchor='w')
        def hover_in(event):
            rc.itemconfig(r8,fill="#d9d9d9")
        def hover_out(event):
            rc.itemconfig(r8,fill="#f7f7f7")
        rc.tag_bind(rt8,"<Enter>",hover_in)
        rc.tag_bind(rt8,"<Leave>",hover_out)


        r9=rc.create_rectangle(30,160,170,180,fill="#f7f7f7",activefill="#d9d9d9",outline="#f7f7f7",activeoutline="#d9d9d9")
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

