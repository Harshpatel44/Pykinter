__author__ = 'Harsh'


import tkinter  as tk
import backend_properties

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

name_enter=''
height_enter=''
width_enter=''
fontstyle_enter=''

def sync_widget():

    backend_properties.check_configure(name_enter,height_enter,fontstyle_enter)    #configures which attrivutes should be disabled acc to widgets






def prop_tab(self,main,middle_frame3,middle_frame2):



    global name_enter,width_enter,height_enter,fontstyle_enter



    design = tk.Canvas(middle_frame3, width=300, height=25,bg='#99AAAA',highlightthickness=0,background="#333333")    #title canvas
    design.place(x=0,y=0)

    design2=tk.Canvas(middle_frame3,height=495,width=300,scrollregion=(0,0,300,300))   #main canvas
    scrollbar=tk.Scrollbar(middle_frame3,command=design2.yview)
    scrollbar.place(x=280,y=26,height=400)
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


    change_fontcolor=tk.Label(props_frame,text="Font Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    change_fontcolor.place(x=30,y=110)
    fontcolor_enter=tk.Entry(props_frame,width=20,textvariable=fce)
    fontcolor_enter.bind("<Return>",backend_properties.fontcolor_enter)
    fontcolor_enter.bind("<FocusOut>",backend_properties.fontcolor_enter)
    fontcolor_enter.bind("<Return>",backend_properties.fontcolor_enter)
    fontcolor_enter.place(x=140,y=110)

    fontstyle_name=tk.Label(props_frame,text="Font Style:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    fontstyle_name.place(x=30,y=130)
    fontstyle_enter=tk.Entry(props_frame,width=20,textvariable=fse)
    fontstyle_enter.bind("<Return>",backend_properties.fontstyle_enter)
    fontstyle_enter.bind("<FocusOut>",backend_properties.fontstyle_enter)
    fontstyle_enter.bind("<Return>",backend_properties.fontstyle_enter)
    fontstyle_enter.place(x=140,y=130)


    font_size=tk.Label(props_frame,text="Font size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    font_size.place(x=30,y=150)
    fontsize_enter=tk.Entry(props_frame,width=20,textvariable=fsie)
    fontsize_enter.bind("<Return>",backend_properties.fontsize_enter)
    fontsize_enter.bind("<FocusOut>",backend_properties.fontsize_enter)
    fontsize_enter.bind("<Return>",backend_properties.fontsize_enter)
    fontsize_enter.place(x=140,y=150)

    alignment_name=tk.Label(props_frame,text="Align:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    alignment_name.place(x=30,y=170)
    alignment_enter=tk.Entry(props_frame,width=20,textvariable=aln)
    alignment_enter.place(x=140,y=170)


    bgcolor_name=tk.Label(props_frame,text="Background color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bgcolor_name.place(x=30,y=190)
    bg_enter=tk.Entry(props_frame,width=20,textvariable=bcn)
    bg_enter.bind("<Return>",backend_properties.bg_enter)
    bg_enter.bind("<FocusOut>",backend_properties.bg_enter)
    bg_enter.bind("<Return>",backend_properties.bg_enter)
    bg_enter.place(x=140,y=190)

    bd_name=tk.Label(props_frame,text="Border Size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bd_name.place(x=30,y=210)
    bd_enter=tk.Entry(props_frame,width=20,textvariable=bdn)
    bd_enter.bind("<Return>",backend_properties.bd_enter)
    bd_enter.bind("<FocusOut>",backend_properties.bd_enter)
    bd_enter.bind("<Return>",backend_properties.bd_enter)
    bd_enter.place(x=140,y=210)

    bdcolor_name=tk.Label(props_frame,text="Border Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
    bdcolor_name.place(x=30,y=230)
    bdcolor_enter=tk.Entry(props_frame,width=20,textvariable=bce)
    bdcolor_enter.bind("<Return>",backend_properties.bdcolor_enter)
    bdcolor_enter.bind("<FocusOut>",backend_properties.bdcolor_enter)
    bdcolor_enter.bind("<Return>",backend_properties.bdcolor_enter)
    bdcolor_enter.place(x=140,y=230)




    #on focus dept


    onfocus_bgcolor=tk.Label(props_frame,text="Onfocus bg:",width=10,bd=1,background="#6D7993",fg="#fef1e8")
    onfocus_bgcolor.place(x=30,y=250)
    onfocus_bgcolor_enter=tk.Entry(props_frame,width=20)
    onfocus_bgcolor_enter.bind("<Return>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.bind("<FocusOut>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.bind("<Return>",lambda event,arg=0:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_bgcolor_enter.place(x=140,y=250)

    onfocus_textcolor=tk.Label(props_frame,text="Onfocus text:",width=10,bd=1,background="#6D7993",fg="#fef1e8")
    onfocus_textcolor.place(x=30,y=270)
    onfocus_textcolor_enter=tk.Entry(props_frame,width=20)
    onfocus_textcolor_enter.bind("<Return>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.bind("<FocusOut>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.bind("<Return>",lambda event,arg=1:backend_properties.onfocus_bgcolor__enter(event,arg))
    onfocus_textcolor_enter.place(x=140,y=270)





    # bgonfocus_color=tk.Entry(props_frame,width=20)
    # bgonfocus_color.place(x=110,y=30)
    #
    # onfocus_textname=tk.Label(props_frame,text="Name:",width=10,bd=1,background="#333333",fg="#fef1e8")
    # onfocus_textname.place(x=30,y=30)
    #
    # onfocustext_enter=tk.Entry(props_frame,width=20)
    # onfocustext_enter.place(x=110,y=30)



    #finish on focus dept


    #on click dept







    #finish onclick dept









    props_frame.pack()
