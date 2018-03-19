import tkinter  as tk
import backend_properties
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor

root=tk.Tk()
root.withdraw()






ne=tk.StringVar()
he=tk.StringVar()
we=tk.StringVar()
fce=tk.StringVar()
fse=tk.StringVar()
fsie=tk.StringVar()
aln=tk.StringVar()
acn=tk.StringVar()
bdn=tk.StringVar()
bcn=tk.StringVar()
bce=tk.StringVar()
var=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()

name_enter=''
height_enter=''
width_enter=''
fontstyle_enter=''


def get_color():
    color=askcolor()
    print(color)

Iconlist_win=["abc","def"]
Iconlist_taskbar=["abc","bdg"]
cursorlist=["arrow","circle","cross","dotbox","exchange","fleur","heart","clock","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"]
def sync_widget():

    backend_properties.check_configure(name_enter,height_enter,fontstyle_enter)    #configures which attrivutes should be disabled acc to widgets






def prop_tab(self,main,middle_frame3,middle_frame2):



    global name_enter,width_enter,height_enter,fontstyle_enter



    design = tk.Canvas(middle_frame3, width=300, height=25,bg='#99AAAA',highlightthickness=0,background="#333333")    #title canvas
    design.place(x=0,y=0)

    design2=tk.Canvas(middle_frame3,height=495,width=300,scrollregion=(0,0,300,1600))   #main canvas
    scrollbar=tk.Scrollbar(middle_frame3,command=design2.yview)
    scrollbar.place(x=280,y=26,height=500)
    design2.configure(yscrollcommand=scrollbar.set)
    design2.place(x=0,y=26)
    props_frame=tk.Frame(design2,height=502,width=300)                                #mainframe inside canvas
    design2.create_window((0,0),window=props_frame,anchor='nw')





    change_name=tk.Label(props_frame,text="Name:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    change_name.place(x=30,y=50)
    name_enter=tk.Entry(props_frame,width=20,textvariable=ne)
    #name_enter.bind("<FocusIn>",backend_properties.check_configure)
    #name_enter.bind("<Enter>",backend_properties.check_configure)
    name_enter.bind("<Tab>",backend_properties.name_enter)
    name_enter.bind("<FocusOut>",backend_properties.name_enter)
    name_enter.bind("<Return>",backend_properties.name_enter)
    name_enter.place(x=140,y=50)

    #
    # X_name=tk.Label(props_frame,text="X:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    # X_name.place(x=30,y=70)
    # X_enter=tk.Entry(props_frame,width=20,textvariable=he)
    # X_enter.bind("<Return>",backend_properties.height_enter)
    # X_enter.bind("<FocusOut>",backend_properties.height_enter)
    # X_enter.bind("<Return>",backend_properties.height_enter)
    # X_enter.place(x=140,y=70)
    #
    # Y_name=tk.Label(props_frame,text="Y:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    # Y_name.place(x=30,y=90)
    # Y_enter=tk.Entry(props_frame,width=20,textvariable=he)
    # Y_enter.bind("<Return>",backend_properties.height_enter)
    # Y_enter.bind("<FocusOut>",backend_properties.height_enter)
    # Y_enter.bind("<Return>",backend_properties.height_enter)
    # Y_enter.place(x=140,y=90)


    height_name=tk.Label(props_frame,text="Height:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    height_name.place(x=30,y=70)
    height_enter=tk.Entry(props_frame,width=20,textvariable=he)
    # height_enter.bind("<FocusIn>",backend_properties.check_configure)
    # height_enter.bind("<Enter>",backend_properties.check_configure)
    height_enter.bind("<Return>",backend_properties.height_enter)
    height_enter.bind("<FocusOut>",backend_properties.height_enter)
    height_enter.bind("<Return>",backend_properties.height_enter)
    height_enter.place(x=140,y=70)

    width_name=tk.Label(props_frame,text="Width:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    width_name.place(x=30,y=90)
    width_enter=tk.Entry(props_frame,width=20,textvariable=we)
    width_enter.bind("<Return>",backend_properties.width_enter)
    width_enter.bind("<FocusOut>",backend_properties.width_enter)
    width_enter.place(x=140,y=90)



    alignment_name=tk.Label(props_frame,text="Align:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    alignment_name.place(x=30,y=110)
    alignment_enter=tk.Entry(props_frame,width=20,textvariable=aln)
    alignment_enter.place(x=140,y=110)


    bgcolor_name=tk.Label(props_frame,text="Background color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bgcolor_name.place(x=30,y=130)
    bg_enter=tk.Entry(props_frame,width=10,textvariable=bcn)
    bg_enter.bind("<Return>",backend_properties.bg_enter)
    bg_enter.bind("<FocusOut>",backend_properties.bg_enter)
    bg_enter.bind("<Return>",backend_properties.bg_enter)
    bg_enter.place(x=140,y=130)
    Button2=tk.Button(props_frame,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button2.place(x=185,y=130)

    bd_name=tk.Label(props_frame,text="Border Size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bd_name.place(x=30,y=150)
    bd_enter=tk.Entry(props_frame,width=20,textvariable=bdn)
    bd_enter.bind("<Return>",backend_properties.bd_enter)
    bd_enter.bind("<FocusOut>",backend_properties.bd_enter)
    bd_enter.bind("<Return>",backend_properties.bd_enter)
    bd_enter.place(x=140,y=150)

    bdcolor_name=tk.Label(props_frame,text="Border Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bdcolor_name.place(x=30,y=170)
    bdcolor_enter=tk.Entry(props_frame,width=10,textvariable=bce)
    bdcolor_enter.bind("<Return>",backend_properties.bdcolor_enter)
    bdcolor_enter.bind("<FocusOut>",backend_properties.bdcolor_enter)
    bdcolor_enter.bind("<Return>",backend_properties.bdcolor_enter)
    bdcolor_enter.place(x=140,y=170)
    Button5=tk.Button(props_frame,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button5.place(x=185,y=170)




    #font
    Font=tk.Label(props_frame,text='Font properties',width=15,background="#6D7993",fg="#fef1e8")
    Font.place(x=100,y=200)

    change_fontcolor=tk.Label(props_frame,text="Font Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    change_fontcolor.place(x=30,y=230)
    fontcolor_enter=tk.Entry(props_frame,width=10,textvariable=fce)
    fontcolor_enter.bind("<Return>",backend_properties.fontcolor_enter)
    fontcolor_enter.bind("<FocusOut>",backend_properties.fontcolor_enter)
    fontcolor_enter.bind("<Return>",backend_properties.fontcolor_enter)
    fontcolor_enter.place(x=140,y=230)
    Button1=tk.Button(props_frame,text="Choose",width=10,background="#6D7993",fg="#fef1e8",command=get_color)
    Button1.place(x=185,y=230)

    fontstyle_name=tk.Label(props_frame,text="Font Style:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    fontstyle_name.place(x=30,y=250)
    fontstyle_enter=tk.Entry(props_frame,width=20,textvariable=fse)
    fontstyle_enter.bind("<Return>",backend_properties.fontstyle_enter)
    fontstyle_enter.bind("<FocusOut>",backend_properties.fontstyle_enter)
    fontstyle_enter.bind("<Return>",backend_properties.fontstyle_enter)
    fontstyle_enter.place(x=140,y=250)


    font_size=tk.Label(props_frame,text="Font size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    font_size.place(x=30,y=270)
    fontsize_enter=tk.Entry(props_frame,width=20,textvariable=fsie)
    fontsize_enter.bind("<Return>",backend_properties.fontsize_enter)
    fontsize_enter.bind("<FocusOut>",backend_properties.fontsize_enter)
    fontsize_enter.bind("<Return>",backend_properties.fontsize_enter)
    fontsize_enter.place(x=140,y=270)


    Onfocus=tk.Label(props_frame,text="OnFocus Properties",width=15,background='#6D7993',fg="#fef1e8")
    Onfocus.place(x=100,y=300)

    onfocus_bgcolor=tk.Label(props_frame,text="Onfocus bg:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    onfocus_bgcolor.place(x=30,y=330)
    onfocus_bgcolor_enter=tk.Entry(props_frame,width=10)
    onfocus_bgcolor_enter.bind("<Return>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.bind("<FocusOut>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.bind("<Return>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.place(x=140,y=330)
    Button3=tk.Button(props_frame,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button3.place(x=185,y=330)


    onfocus_textcolor=tk.Label(props_frame,text="Onfocus text:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    onfocus_textcolor.place(x=30,y=350)
    onfocus_textcolor_enter=tk.Entry(props_frame,width=10)
    onfocus_textcolor_enter.bind("<Return>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.bind("<FocusOut>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.bind("<Return>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.place(x=140,y=350)
    Button4=tk.Button(props_frame,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button4.place(x=185,y=350)

    #cursors department


    listbox_enter=tk.Label(props_frame,text="Cursor style",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    listbox_enter.place(x=30,y=370)
    var.set(cursorlist[1])
    listbox=ttk.OptionMenu(props_frame,var,cursorlist[1],*cursorlist,command=backend_properties.cursor_change)
    listbox.place(x=140,y=370)

    cursor_size=tk.Label(props_frame,text="Cursor size",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    cursor_size.place(x=30,y=380)
    cursor_size_enter=tk.Entry(props_frame)
    cursor_size_enter.bind("<Return>")
    cursor_size_enter.bind("<FocusOut>")
    cursor_size_enter.bind("<Return>")
    cursor_size_enter.place(x=140,y=380)



    #on click dept







    #finish onclick dept


#Window area
    win=tk.Label(props_frame,text="Window properties",bd=1,background="#6D7993",fg="#fef1e8")
    win.place(x=100,y=400)

    win_name=tk.Label(props_frame,text="Window name",width=15,bd=1, background="#6D7993",fg="#fef1e8")
    win_name.place(x=30,y=430)
    win_name_enter=tk.Entry(props_frame,width=20)
    win_name_enter.bind("<Return>",backend_properties.window_naming)
    win_name_enter.bind("<FocusOut>",backend_properties.window_naming)
    win_name_enter.bind("<Return>",backend_properties.window_naming)
    win_name_enter.place(x=140,y=430)


    win_icon=tk.Label(props_frame,text="Window Icon",bd=1,width="15",background="#6D7993",fg="#fef1e8")
    win_icon.place(x=30,y=450)
    win_icon_enter=ttk.OptionMenu(props_frame,var2,*Iconlist_win,command=backend_properties.window_icon)
    win_icon_enter.place(x=140,y=450)


#Taskbar properties


    taskbar=tk.Label(props_frame,text="TaskBar Properties",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar.place(x=100,y=480)

    X_taskbar=tk.Label(props_frame,text="X co-ordinates",width=5,bd=1,background="#6D7993",fg="#fef1e8")
    X_taskbar.place(x=30,y=510)
    X_taskbar_enter=tk.Entry(props_frame)
    X_taskbar_enter.bind("<Return>",backend_properties.enter_X)
    X_taskbar_enter.bind('<FocusOut>',backend_properties.enter_X)
    X_taskbar_enter.bind("<Return>",backend_properties.enter_X)
    X_taskbar_enter.place(x=80,y=510)


    Y_taskbar=tk.Label(props_frame,text="Y co-ordinates",width=5,bd=1,background="#6D7993",fg="#fef1e8")
    Y_taskbar.place(x=30,y=530)
    Y_taskbar_enter=tk.Entry(props_frame)
    Y_taskbar_enter.bind("<Return>",backend_properties.enter_Y)
    Y_taskbar_enter.bind('<FocusOut>',backend_properties.enter_Y)
    Y_taskbar_enter.bind("<Return>",backend_properties.enter_Y)
    Y_taskbar_enter.place(x=160,y=530)




    taskbar_color=tk.Label(props_frame,text="Taskbar color",width=15,bd=1,background='#6D7993',fg="#fef1e8")
    taskbar_color.place(x=30,y=510)
    taskbar_color_enter=tk.Entry(props_frame)
    taskbar_color_enter.bind("<Return>",backend_properties.taskbar_colorchange)
    taskbar_color_enter.bind("<FocusOut>",backend_properties.taskbar_colorchange)
    taskbar_color_enter.bind("<Return>",backend_properties.taskbar_colorchange)
    taskbar_color_enter.place(x=140,y=510)

    taskbar_border=tk.Label(props_frame,text="Taskbar border",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_border.place(x=30,y=530)
    taskbar_border_enter=tk.Entry(props_frame)
    taskbar_border_enter.bind("<Return>",backend_properties.taskbar_borderchange)
    taskbar_border_enter.bind("<FocusOut>",backend_properties.taskbar_borderchange)
    taskbar_border_enter.bind("<Return>",backend_properties.taskbar_borderchange)
    taskbar_border_enter.place(x=140,y=530)

    taskbar_height=tk.Label(props_frame,text="Taskbar height",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_height.place(x=30,y=550)
    taskbar_height_enter=tk.Entry(props_frame)
    taskbar_height_enter.bind("<Return>")
    taskbar_height_enter.bind("<FocusOut>")
    taskbar_height_enter.bind("<Return>")
    taskbar_height_enter.place(x=140,y=550)

    taskbar_width=tk.Label(props_frame,text="Taskbar width",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_width.place(x=30,y=570)
    taskbar_width_enter=tk.Entry(props_frame)
    taskbar_width_enter.bind("<Return>")
    taskbar_width_enter.bind("<FocusOut>")
    taskbar_width_enter.bind("<Return>")
    taskbar_width_enter.place(x=140,y=570)

    taskbar_icon=tk.Label(props_frame,text="Taskbar icons",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_icon.place(x=30,y=590)
    taskbar_icon_enter=ttk.OptionMenu(props_frame,var3,*Iconlist_taskbar,command=backend_properties.taskbar_icon)
    taskbar_icon_enter.place(x=140,y=590)














    props_frame.pack()
