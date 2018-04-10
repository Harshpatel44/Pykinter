import tkinter  as tk
import backend_properties
import update
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor


#this file deals with the layout of the right section of the application , that is properties tab .
root=tk.Tk()
root.withdraw()


#creating variables for global declaration of stringvar to use for showing updated properties on selecting widget
ne=''
he=''
we=''
fce=''
fse=''
fsie=''
aln=''
acn=''
bdn=''
bcn=''
bce=''
variables=[ne,he,we,fce,fse,fsie,aln,acn,bdn,bcn,bce]
var=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()

name_enter=''
height_enter=''
width_enter=''
fontstyle_enter=''


def enter(event):
    widget=event.widget
    widget.configure(bg='#96858F')
def leave(event):
    widget=event.widget
    widget.configure(bg="#6D7993")
def get_color():
    color=askcolor()
    print(color)

Iconlist_win=["abc","def"]
Iconlist_taskbar=["abc","bdg"]
cursorlist=["arrow","circle","cross","dotbox","exchange","fleur","heart","clock","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"]
def sync_widget(selected):
    global variables
    backend_properties.check_configure(name_enter,height_enter,fontstyle_enter)    #configures which attrivutes should be disabled acc to widgets
    update.save_widget_props(selected,variables)




def prop_tab(self,main,middle_frame3,middle_frame2):



    global name_enter,width_enter,height_enter,fontstyle_enter



    design = tk.Canvas(middle_frame3, width=300, height=25,bg='#99AAAA',highlightthickness=0,background="#333333")    #title canvas
    design.place(x=0,y=0)
    vscrollbar=tk.Scrollbar(middle_frame3)

    design2=tk.Canvas(middle_frame3,height=495,width=300,yscrollcommand=vscrollbar.set,scrollregion=(0,0,300,1200))   #main canvas

    vscrollbar.config(command=design2.yview)
    vscrollbar.pack(side=tk.LEFT, fill=tk.Y)


    props_frame=tk.Frame(design2,height=2000,width=300)                                #mainframe inside canvas
    design2.pack(side="left", fill="both", expand=True)

    design2.create_window((0,0),window=props_frame,anchor='nw')



    global variables
    variables[0]=tk.StringVar(props_frame,value="")
    variables[1]=tk.StringVar(props_frame,value="")
    variables[2]=tk.StringVar(props_frame,value="")
    variables[3]=tk.StringVar(props_frame,value="")
    variables[4]=tk.StringVar(props_frame,value="")
    variables[5]=tk.StringVar(props_frame,value="")
    variables[6]=tk.StringVar(props_frame,value="")
    variables[7]=tk.StringVar(props_frame,value="")
    variables[8]=tk.StringVar(props_frame,value="")
    variables[9]=tk.StringVar(props_frame,value="")
    variables[10]=tk.StringVar(props_frame,value="")


    change_name=tk.Label(props_frame,text="Name:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    change_name.place(x=30,y=50)
    name_enter=tk.Entry(props_frame,width=20,textvariable=variables[0])
    #name_enter.bind("<FocusIn>",backend_properties.check_configure)
    #name_enter.bind("<Enter>",backend_properties.check_configure)
    name_enter.bind("<Tab>",backend_properties.name_enter)
    name_enter.bind("<FocusOut>",backend_properties.name_enter)
    name_enter.bind("<Return>",backend_properties.name_enter)
    name_enter.place(x=140,y=50)



    height_name=tk.Label(props_frame,text="Height:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    height_name.place(x=30,y=70)
    height_enter=tk.Entry(props_frame,width=20,textvariable=variables[1])
    # height_enter.bind("<FocusIn>",backend_properties.check_configure)
    # height_enter.bind("<Enter>",backend_properties.check_configure)
    height_enter.bind("<Return>",backend_properties.height_enter)
    height_enter.bind("<FocusOut>",backend_properties.height_enter)
    height_enter.bind("<Return>",backend_properties.height_enter)
    height_enter.place(x=140,y=70)

    width_name=tk.Label(props_frame,text="Width:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    width_name.place(x=30,y=90)
    width_enter=tk.Entry(props_frame,width=20,textvariable=variables[2])
    width_enter.bind("<Return>",backend_properties.width_enter)
    width_enter.bind("<FocusOut>",backend_properties.width_enter)
    width_enter.place(x=140,y=90)



    alignment_name=tk.Label(props_frame,text="Align:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    alignment_name.place(x=30,y=110)
    alignment_enter=tk.Entry(props_frame,width=20)
    alignment_enter.bind("<Return>",backend_properties.width_enter)
    alignment_enter.bind("<FocusOut>",backend_properties.width_enter)
    alignment_enter.place(x=140,y=110)


    bgcolor_name=tk.Label(props_frame,text="Background color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bgcolor_name.place(x=30,y=130)
    bg_enter=tk.Entry(props_frame,width=10,textvariable=variables[9])
    bg_enter.bind("<Return>",backend_properties.bg_enter)
    bg_enter.bind("<FocusOut>",backend_properties.bg_enter)
    bg_enter.bind("<Return>",backend_properties.bg_enter)

    def enter(event):
        widget=event.widget
        widget.configure(bg='#96858F')
    def leave(event):
        widget=event.widget
        widget.configure(bg="#6D7993")
    bg_enter.place(x=140,y=130)
    Button2=tk.Button(props_frame,text="Choose",relief="flat",bd=0,width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button2.bind("<Enter>",enter)
    Button2.bind("<Leave>",leave)
    Button2.place(x=185,y=130)

 #Border properties
    border_props=tk.Label(props_frame,text="Border Properties",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    border_props.place(x=100,y=160)

    bd_size=tk.Label(props_frame,text="Border Size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bd_size.place(x=30,y=190)
    bd_size_enter=tk.Entry(props_frame,width=20,textvariable=variables[8])
    bd_size_enter.bind("<Return>",backend_properties.bd_enter)
    bd_size_enter.bind("<FocusOut>",backend_properties.bd_enter)
    bd_size_enter.bind("<Return>",backend_properties.bd_enter)
    bd_size_enter.place(x=140,y=190)

    bdcolor_name=tk.Label(props_frame,text="Border Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bdcolor_name.place(x=30,y=210)
    bdcolor_enter=tk.Entry(props_frame,width=10,textvariable=variables[10])
    bdcolor_enter.bind("<Return>",backend_properties.bdcolor_enter)
    bdcolor_enter.bind("<FocusOut>",backend_properties.bdcolor_enter)
    bdcolor_enter.bind("<Return>",backend_properties.bdcolor_enter)
    bdcolor_enter.place(x=140,y=210)
    Button5=tk.Button(props_frame,text="Choose",relief="flat",bd=0,width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button5.bind("<Enter>",enter)
    Button5.bind("<Leave>",leave)
    Button5.place(x=185,y=210)




    #font
    Font=tk.Label(props_frame,text='Font properties',width=15,background="#6D7993",fg="#fef1e8")
    Font.place(x=100,y=260)

    change_fontcolor=tk.Label(props_frame,text="Font Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    change_fontcolor.place(x=30,y=300)
    fontcolor_enter=tk.Entry(props_frame,width=10,textvariable=variables[3])
    fontcolor_enter.bind("<Return>",backend_properties.fontcolor_enter)
    fontcolor_enter.bind("<FocusOut>",backend_properties.fontcolor_enter)
    fontcolor_enter.bind("<Return>",backend_properties.fontcolor_enter)
    fontcolor_enter.place(x=140,y=300)
    Button1=tk.Button(props_frame,text="Choose",relief="flat",bd=0,width=10,background="#6D7993",fg="#fef1e8",command=get_color)
    Button1.bind("<Enter>",enter)
    Button1.bind("<Leave>",leave)
    Button1.place(x=185,y=300)

    fontstyle_name=tk.Label(props_frame,text="Font Style:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    fontstyle_name.place(x=30,y=320)
    fontstyle_enter=tk.Entry(props_frame,width=20,textvariable=variables[4])
    fontstyle_enter.bind("<Return>",backend_properties.fontstyle_enter)
    fontstyle_enter.bind("<FocusOut>",backend_properties.fontstyle_enter)
    fontstyle_enter.bind("<Return>",backend_properties.fontstyle_enter)
    fontstyle_enter.place(x=140,y=320)


    font_size=tk.Label(props_frame,text="Font size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    font_size.place(x=30,y=340)
    fontsize_enter=tk.Entry(props_frame,width=20,textvariable=variables[5])
    fontsize_enter.bind("<Return>",backend_properties.fontsize_enter)
    fontsize_enter.bind("<FocusOut>",backend_properties.fontsize_enter)
    fontsize_enter.bind("<Return>",backend_properties.fontsize_enter)
    fontsize_enter.place(x=140,y=340)


    Button_bold=tk.Button(props_frame,text="BOLD",width=15,bd=0,background="#6D7993",fg="#fef1e8",command=lambda event,arg=0:backend_properties.Font_styling)
    Button_bold.config(relief="raised")
    Button_bold.bind("<Enter>",enter)
    Button_bold.bind("<Leave>",leave)
    Button_bold.bind("<Button-1>",lambda event,arg=0:backend_properties.Font_styling(event,arg))
    # Button_bold.bind("<FocusOut>",lambda event,arg=0:backend_properties.Font_styling(event,arg))
    # Button_bold.bind("<Return>",lambda event,arg=0:backend_properties.Font_styling(event,arg))

    Button_bold.place(x=100,y=370)

    Button_italic=tk.Button(props_frame,text="ITALIC",width=15,bd=0,background="#6D7993",fg="#fef1e8",command=lambda event,arg=2:backend_properties.Font_styling)
    Button_italic.config(relief="raised")
    Button_italic.bind("<Enter>",enter)
    Button_italic.bind("<Leave>",leave)
    Button_italic.bind("<Button-1>",lambda event,arg=1:backend_properties.Font_styling(event,arg))
    # Button_italic.bind("<FocusOut>",lambda event,arg=1:backend_properties.Font_styling(event,arg))
    # Button_italic.bind("<Return>",lambda event,arg=1:backend_properties.Font_styling(event,arg))
    Button_italic.place(x=100,y=395)

    Button_underline=tk.Button(props_frame,text="UNDERLINE",width=15,bd=0,background="#6D7993",fg="#fef1e8",command=lambda event,arg=2:backend_properties.Font_styling)
    Button_italic.config(relief="sunken",bd=0)
    Button_underline.bind("<Enter>",enter)
    Button_underline.bind("<Leave>",leave)
    Button_underline.bind("<Button-1>",lambda event,arg=2:backend_properties.Font_styling(event,arg))
    # Button_underline.bind("<FocusOut>",lambda event,arg=2:backend_properties.Font_styling(event,arg))
    # Button_underline.bind("<Return>",lambda event,arg=2:backend_properties.Font_styling(event,arg))
    Button_underline.place(x=100,y=420)

#cursors department

    cursor_dept=tk.Label(props_frame,text="Cursor properties:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    cursor_dept.place(x=100,y=450)
    listbox_enter=tk.Label(props_frame,text="Cursor style",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    listbox_enter.place(x=30,y=480)
    var.set(cursorlist[1])
    listbox=ttk.OptionMenu(props_frame,var,cursorlist[1],*cursorlist,command=backend_properties.cursor_change)
    listbox.place(x=140,y=480)

    cursor_size=tk.Label(props_frame,text="Cursor size",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    cursor_size.place(x=30,y=500)
    cursor_size_enter=tk.Entry(props_frame)
    cursor_size_enter.bind("<Return>")
    cursor_size_enter.bind("<FocusOut>")
    cursor_size_enter.bind("<Return>")
    cursor_size_enter.place(x=140,y=500)



#Window area
    win=tk.Label(props_frame,text="Window properties",bd=1,background="#6D7993",fg="#fef1e8")
    win.place(x=100,y=545)

    win_name=tk.Label(props_frame,text="Window name",width=15,bd=1, background="#6D7993",fg="#fef1e8")
    win_name.place(x=30,y=570)
    win_name_enter=tk.Entry(props_frame,width=20)
    win_name_enter.bind("<Return>",backend_properties.window_naming)
    win_name_enter.bind("<FocusOut>",backend_properties.window_naming)
    win_name_enter.bind("<Return>",backend_properties.window_naming)
    win_name_enter.place(x=140,y=570)


    win_icon=tk.Label(props_frame,text="Window Icon",bd=1,width="15",background="#6D7993",fg="#fef1e8")
    win_icon.place(x=30,y=590)
    win_icon_enter=ttk.OptionMenu(props_frame,var2,*Iconlist_win,command=backend_properties.window_icon)
    win_icon_enter.place(x=140,y=590)

    window_op=tk.Label(props_frame,text="Window Opacity",bd=1,width=15,background="#6D7993",fg="#fef1e8")
    window_op.place(x=30,y=610)
    window_op_enter=tk.Entry(props_frame,width=10)
    window_op_enter.place(x=140,y=610)

#Taskbar properties

    taskbar=tk.Label(props_frame,text="TaskBar Properties",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar.place(x=100,y=640)

    X_taskbar=tk.Label(props_frame,text="X",width=5,bd=1,background="#6D7993",fg="#fef1e8")
    X_taskbar.place(x=30,y=670)
    X_taskbar_enter=tk.Entry(props_frame,width=10)
    X_taskbar_enter.bind("<Return>",backend_properties.enter_X)
    X_taskbar_enter.bind('<FocusOut>',backend_properties.enter_X)
    X_taskbar_enter.bind("<Return>",backend_properties.enter_X)
    X_taskbar_enter.place(x=80,y=670)


    Y_taskbar=tk.Label(props_frame,text="Y",width=5,bd=1,background="#6D7993",fg="#fef1e8")
    Y_taskbar.place(x=150,y=690)
    Y_taskbar_enter=tk.Entry(props_frame,width=10)
    Y_taskbar_enter.bind("<Return>",backend_properties.enter_Y)
    Y_taskbar_enter.bind('<FocusOut>',backend_properties.enter_Y)
    Y_taskbar_enter.bind("<Return>",backend_properties.enter_Y)
    Y_taskbar_enter.place(x=200,y=690)




    taskbar_color=tk.Label(props_frame,text="Taskbar color",width=15,bd=1,background='#6D7993',fg="#fef1e8")
    taskbar_color.place(x=30,y=710)
    taskbar_color_enter=tk.Entry(props_frame)
    taskbar_color_enter.bind("<Return>",backend_properties.taskbar_colorchange)
    taskbar_color_enter.bind("<FocusOut>",backend_properties.taskbar_colorchange)
    taskbar_color_enter.bind("<Return>",backend_properties.taskbar_colorchange)
    taskbar_color_enter.place(x=140,y=710)

    taskbar_border=tk.Label(props_frame,text="Taskbar border",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_border.place(x=30,y=730)
    taskbar_border_enter=tk.Entry(props_frame)
    taskbar_border_enter.bind("<Return>",backend_properties.taskbar_borderchange)
    taskbar_border_enter.bind("<FocusOut>",backend_properties.taskbar_borderchange)
    taskbar_border_enter.bind("<Return>",backend_properties.taskbar_borderchange)
    taskbar_border_enter.place(x=140,y=730)

    taskbar_height=tk.Label(props_frame,text="Taskbar height",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_height.place(x=30,y=750)
    taskbar_height_enter=tk.Entry(props_frame)
    taskbar_height_enter.bind("<Return>")
    taskbar_height_enter.bind("<FocusOut>")
    taskbar_height_enter.bind("<Return>")
    taskbar_height_enter.place(x=140,y=750)

    taskbar_width=tk.Label(props_frame,text="Taskbar width",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_width.place(x=30,y=770)
    taskbar_width_enter=tk.Entry(props_frame)
    taskbar_width_enter.bind("<Return>")
    taskbar_width_enter.bind("<FocusOut>")
    taskbar_width_enter.bind("<Return>")
    taskbar_width_enter.place(x=140,y=770)

    taskbar_icon=tk.Label(props_frame,text="Taskbar icons",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    taskbar_icon.place(x=30,y=790)
    taskbar_icon_enter=ttk.OptionMenu(props_frame,var3,*Iconlist_taskbar,command=backend_properties.taskbar_icon)
    taskbar_icon_enter.place(x=140,y=810)

#Onfocus Properties

    Onfocus=tk.Label(props_frame,text="OnFocus Properties",bd=1,width=15,background='#6D7993',fg="#fef1e8")
    Onfocus.place(x=100,y=840)

    onfocus_bgcolor=tk.Label(props_frame,text="Onfocus bg:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    onfocus_bgcolor.place(x=30,y=870)
    onfocus_bgcolor_enter=tk.Entry(props_frame,width=10)
    onfocus_bgcolor_enter.bind("<Return>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.bind("<FocusOut>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.bind("<Return>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.place(x=140,y=870)
    Button3=tk.Button(props_frame,text="Choose",relief="flat",bd=0,width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button3.bind("<Enter>",enter)
    Button3.bind("<Leave>",leave)
    Button3.place(x=185,y=870)



    onfocus_textcolor=tk.Label(props_frame,text="Onfocus text:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    onfocus_textcolor.place(x=30,y=890)
    onfocus_textcolor_enter=tk.Entry(props_frame,width=10)
    onfocus_textcolor_enter.bind("<Return>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.bind("<FocusOut>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.bind("<Return>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.place(x=140,y=890)
    Button4=tk.Button(props_frame,text="Choose",relief="flat",bd=0,width=10,height=1,background="#6D7993",fg="#fef1e8",command=get_color)
    Button4.bind("<Enter>",enter)
    Button4.bind("<Leave>",leave)
    Button4.place(x=185,y=890)

    Onfocus_fontfamily=tk.Label(props_frame,text="Font Family:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_fontfamily.place(x=30,y=910)
    Onfocus_fontfamily_enter=tk.Entry(props_frame,width=20)
    Onfocus_fontfamily_enter.bind("<Return>")
    Onfocus_fontfamily_enter.bind("<FocusOut>")
    Onfocus_fontfamily_enter.bind("<Return>")
    Onfocus_fontfamily_enter.place(x=140,y=910)

    Onfocus_Fontsize=tk.Label(props_frame,text=" Font size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_Fontsize.place(x=30,y=930)
    Onfocus_Fontsize_enter=tk.Entry(props_frame,width=20)
    Onfocus_Fontsize_enter.bind("<Return>")
    Onfocus_Fontsize_enter.bind("<FocusOut>")
    Onfocus_Fontsize_enter.bind("<Return>")
    Onfocus_Fontsize_enter.place(x=140,y=930)


    Onfocus_Bold=tk.Label(props_frame,text="Bold:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_Bold.place(x=30,y=950)
    Onfocus_Bold_enter=tk.Entry(props_frame,width=20)
    Onfocus_Bold_enter.bind("<Return>")
    Onfocus_Bold_enter.bind("<FocusOut>")
    Onfocus_Bold_enter.bind("<Return>")
    Onfocus_Bold_enter.place(x=140,y=950)

    Onfocus_Italic=tk.Label(props_frame,text="Italic:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_Italic.place(x=30,y=970)
    Onfocus_Italic_enter=tk.Entry(props_frame,width=20)
    Onfocus_Italic_enter.bind("<Return>")
    Onfocus_Italic_enter.bind("<FocusOut>")
    Onfocus_Italic_enter.bind("<Return>")
    Onfocus_Italic_enter.place(x=140,y=970)

    Onfocus_Underline=tk.Label(props_frame,text=" Font size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_Underline.place(x=30,y=990)
    Onfocus_Underline_enter=tk.Entry(props_frame,width=20)
    Onfocus_Underline_enter.bind("<Return>")
    Onfocus_Underline_enter.bind("<FocusOut>")
    Onfocus_Underline_enter.bind("<Return>")
    Onfocus_Underline_enter.place(x=140,y=990)


    Onfocus_Border=tk.Label(props_frame,text="Border Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_Border.place(x=30,y=1010)
    Onfocus_Border_enter=tk.Entry(props_frame,width=20)
    Onfocus_Border_enter.bind("<Return>")
    Onfocus_Border_enter.bind("<FocusOut>")
    Onfocus_Border_enter.bind("<Return>")
    Onfocus_Border_enter.place(x=140,y=1010)


    Onfocus_Bordersize=tk.Label(props_frame,text="Border Size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_Bordersize.place(x=30,y=1030)
    Onfocus_Bordersize_enter=tk.Entry(props_frame,width=20)
    Onfocus_Bordersize_enter.bind("<Return>")
    Onfocus_Bordersize_enter.bind("<FocusOut>")
    Onfocus_Bordersize_enter.bind("<Return>")
    Onfocus_Bordersize_enter.place(x=140,y=1030)

    Onfocus_name=tk.Label(props_frame,text="Name:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_name.place(x=30,y=1050)
    Onfocus_name_enter=tk.Entry(props_frame,width=20)
    Onfocus_name_enter.bind("<Return>")
    Onfocus_name_enter.bind("<FocusOut>")
    Onfocus_name_enter.bind("<Return>")
    Onfocus_name_enter.place(x=140,y=1050)

    Onfocus_height=tk.Label(props_frame,text="Height:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_height.place(x=30,y=1070)
    Onfocus_height_enter=tk.Entry(props_frame,width=20)
    Onfocus_height_enter.bind("<Return>")
    Onfocus_height_enter.bind("<FocusOut>")
    Onfocus_height_enter.bind("<Return>")
    Onfocus_height_enter.place(x=140,y=1070)


    Onfocus_width=tk.Label(props_frame,text="Width:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_width.place(x=30,y=1090)
    Onfocus_width_enter=tk.Entry(props_frame,width=20)
    Onfocus_width_enter.bind("<Return>")
    Onfocus_width_enter.bind("<FocusOut>")
    Onfocus_width_enter.bind("<Return>")
    Onfocus_width_enter.place(x=140,y=1090)


    Onfocus_winname=tk.Label(props_frame,text="Window Name:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_winname.place(x=30,y=2010)
    Onfocus_winname_enter=tk.Entry(props_frame,width=20)
    Onfocus_winname_enter.bind("<Return>")
    Onfocus_winname_enter.bind("<FocusOut>")
    Onfocus_winname_enter.bind("<Return>")
    Onfocus_winname_enter.place(x=140,y=2010)


    Onfocus_winicon=tk.Label(props_frame,text="Window Icon:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_winicon.place(x=30,y=2030)
    Onfocus_winicon_enter=tk.Entry(props_frame,width=20)
    Onfocus_winicon_enter.bind("<Return>")
    Onfocus_winicon_enter.bind("<FocusOut>")
    Onfocus_winicon_enter.bind("<Return>")
    Onfocus_winicon_enter.place(x=140,y=2030)


    Onfocus_winopacity=tk.Label(props_frame,text="Window Opacity:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    Onfocus_winopacity.place(x=30,y=2050)
    Onfocus_winopacity_enter=tk.Entry(props_frame,width=20)
    Onfocus_winopacity_enter.bind("<Return>")
    Onfocus_winopacity_enter.bind("<FocusOut>")
    Onfocus_winopacity_enter.bind("<Return>")
    Onfocus_winopacity_enter.place(x=140,y=2050)





















