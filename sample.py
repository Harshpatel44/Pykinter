# # __author__ = 'harsh'
# #
# #
# # #making scrollbar
# # import tkinter as tk
# # from PIL import ImageTk
# #
# #
# #
# # # b = tk.Label(root,bd=0,height=200,width=200)
# # # image = ImageTk.PhotoImage(file="scrollbar.PNG")
# # # b.config(image=image)
# # # b.image = image
# # # b.place(x=10,y=10)
# # # canvas=tk.Canvas(root,height=400,width=100,background="#555555")
# # # canvas.place(x=10,y=10)
# # # button=tk.Button(canvas,text="button")
# # # button.pack()
# # # f=button.master
# # # f.configure(width=500)
# # # print(button._nametowidget(root))
# #
# # import tkinter as tk
# # main=tk.Tk()
# #
# # canvas=tk.Canvas(main,width=500,height=200,scrollregion=(0,0,200,500))
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # button=tk.Button(canvas,text='button1')
# # button.pack()
# # scrollbar=tk.Scrollbar(main,command=canvas.yview)
# # canvas.pack()
# # canvas.configure(yscrollcommand=scrollbar.set)
# # scrollbar.pack()
# # main.mainloop()
# # # bg_color="#fef1e8"
# # # B1=tk.Button(root,text="Button",height=1,bd=0,highlightthickness=5,highlightbackground="black",width=10,background=bg_color,relief=tk.RAISED)
# # # B1.pack()
# # # ButtonButton=tk.Button(root,text="Button",height=1,width=10,highlightthickness=5,background="#fef1e8",foreground="SystemButtonText",relief=tk.RAISED,bd=0)
# # # ButtonButton.pack()
# # # frame=tk.Frame(root,width="200",height="200")
# # # canvas=tk.Canvas(frame,height="123",width="25",background="#dddddd")
# # # canvas.create_rectangle(2,2,25,25,fill="#dddddd")
# # # canvas.create_line(7,8,15,15)
# # # canvas.create_line(15,15,23,8)
# # #canvas.create_image(image="")
# # #canvas.create_line(7,8,17,8)
# # # canvas.create_rectangle(2,25,25,100,fill="#999999")
# # # canvas.create_rectangle(2,100,25,123,fill="#dddddd")
# # # canvas.pack()
# # # frame.pack()
# #
# #
# #
# #
# # #making arrows
# # # import tkinter as tk
# # # root=tk.Tk()
# # # def focus_change(event):
# # #         event.widget.configure(background="#777777")
# # # def focus_reset(event):
# # #         event.widget.configure(background="#333333")
# # # btn=tk.Button(root,text="button",background="#555555")
# # # btn.bind('<Enter>',focus_change)
# # # btn.bind('<Leave>',focus_reset)
# # # btn.pack()
# # #
# # #
# # # entry=tk.Entry(width=10)
# # # entry.pack()
# # # # canvas=tk.Canvas(height="100",width="200",background="#dddddd")
# # # # canvas.create_line(,8,15,15)
# # # # canvas.pack()
# # # root.mainloop()
#
#
# # from tkinter import *
# # root=Tk()
# # frame1=Frame(root,width=300,height=300)
# # frame1.grid(row=0,column=0)
# # canvas=Canvas(frame1,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
# # frame=Frame(canvas,width=300,height=300)
# # frame.pack()
# # hbar=Scrollbar(frame,orient=HORIZONTAL)
# # hbar.pack(side=BOTTOM,fill=X)
# # hbar.config(command=canvas.xview)
# # vbar=Scrollbar(frame,orient=VERTICAL)
# # vbar.pack(side=RIGHT,fill=Y)
# # vbar.config(command=canvas.yview)
# # canvas.config(width=300,height=300)
# # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
# # canvas.pack(side=LEFT,expand=True,fill=BOTH)
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# # button=Button(canvas,text="main")
# # button.pack()
# #
# #
# # root.mainloop()
#
#
#
#
# # import tkinter as tk
# #
# # root=tk.Tk()
# #
# # vscrollbar = tk.Scrollbar(root)
# #
# # c= tk.Canvas(root,background = "#D2D2D2",yscrollcommand=vscrollbar.set,scrollregion=(0,0,1000,1600))
# #
# # vscrollbar.config(command=c.yview)
# # vscrollbar.pack(side=tk.LEFT, fill=tk.Y)
# #
# # f=tk.Frame(c) #Create the frame which will hold the widgets
# #
# # c.pack(side="left", fill="both", expand=True)
# #
# # #Updated the window creation
# # c.create_window(0,0,window=f, anchor='nw')
# #
# # #Added more content here to activate the scroll
# #
# # #tk.Label(f,wraplength=350 ,text="Det er en kendsgerning, at man bliver distraheret af Det er en kendsgerning, at man bliver distraheret af Det er en kendsgerning, at man bliver distraheret af Det er en kendsgerning, at man bliver distraheret af Det er en kendsgerning, at man bliver distraheret af Det er en kendsgerning, at man bliver distraheret af Det er en kendsgerning, at man bliver distraheret af.").pack()
# # change_name=tk.Label(f,text="Name:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# # change_name.pack()
# # name_enter=tk.Entry(f,width=20)
# # #name_enter.bind("<FocusIn>",backend_properties.check_configure)
# # #name_enter.bind("<Enter>",backend_properties.check_configure)
# #
# # name_enter.pack()
#
# #
# # X_name=tk.Label(f,text="X:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# # X_name.place(x=30,y=70)
# # X_enter=tk.Entry(f,width=20,textvariable=he)
# # X_enter.bind("<Return>",backend_properties.height_enter)
# # X_enter.bind("<FocusOut>",backend_properties.height_enter)
# # X_enter.bind("<Return>",backend_properties.height_enter)
# # X_enter.place(x=140,y=70)
# #
# # Y_name=tk.Label(f,text="Y:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# # Y_name.place(x=30,y=90)
# # Y_enter=tk.Entry(f,width=20,textvariable=he)
# # Y_enter.bind("<Return>",backend_properties.height_enter)
# # Y_enter.bind("<FocusOut>",backend_properties.height_enter)
# # Y_enter.bind("<Return>",backend_properties.height_enter)
# # Y_enter.place(x=140,y=90)
#
#
# height_name=tk.Label(f,text="Height:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# height_name.pack()
# height_enter=tk.Entry(f,width=20)
# # height_enter.bind("<FocusIn>",backend_properties.check_configure)
# # height_enter.bind("<Enter>",backend_properties.check_configure)
#
# height_enter.pack()
#
# width_name=tk.Label(f,text="Width:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# width_name.pack()
# width_enter=tk.Entry(f,width=20)
#
# width_enter.pack()
#
#
#
# alignment_name=tk.Label(f,text="Align:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# alignment_name.pack()
# alignment_enter=tk.Entry(f,width=20)
# alignment_enter.pack()
#
#
# bgcolor_name=tk.Label(f,text="Background color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# bgcolor_name.pack()
# bg_enter=tk.Entry(f,width=10)
#
# bg_enter.pack()
# Button2=tk.Button(f,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8")
# Button2.pack()
#
# bd_name=tk.Label(f,text="Border Size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# bd_name.pack()
# bd_enter=tk.Entry(f,width=20)
#
# bd_enter.pack()
#
# bdcolor_name=tk.Label(f,text="Border Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# bdcolor_name.pack()
# bdcolor_enter=tk.Entry(f,width=10)
#
# bdcolor_enter.pack()
# Button5=tk.Button(f,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8")
# Button5.pack()
#
#
#
#
# #font
# Font=tk.Label(f,text='Font properties',width=15,background="#6D7993",fg="#fef1e8")
# Font.pack()
#
# change_fontcolor=tk.Label(f,text="Font Color:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# change_fontcolor.pack()
# fontcolor_enter=tk.Entry(f,width=10)
#
# fontcolor_enter.pack()
# Button1=tk.Button(f,text="Choose",width=10,background="#6D7993",fg="#fef1e8")
# Button1.pack()
#
# fontstyle_name=tk.Label(f,text="Font Style:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# fontstyle_name.pack()
# fontstyle_enter=tk.Entry(f,width=20)
#
# fontstyle_enter.pack()
#
#
# font_size=tk.Label(f,text="Font size:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# font_size.pack()
# fontsize_enter=tk.Entry(f,width=20)
#
# fontsize_enter.pack()
#
#
# Onfocus=tk.Label(f,text="OnFocus Properties",width=15,background='#6D7993',fg="#fef1e8")
# Onfocus.pack()
#
# onfocus_bgcolor=tk.Label(f,text="Onfocus bg:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# onfocus_bgcolor.pack()
# onfocus_bgcolor_enter=tk.Entry(f,width=10)
#
# onfocus_bgcolor_enter.pack()
# Button3=tk.Button(f,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8")
# Button3.pack()
#
#
# onfocus_textcolor=tk.Label(f,text="Onfocus text:",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# onfocus_textcolor.pack()
# onfocus_textcolor_enter=tk.Entry(f,width=10)
#
# onfocus_textcolor_enter.pack()
# Button4=tk.Button(f,text="Choose",width=10,height=1,background="#6D7993",fg="#fef1e8")
# Button4.pack()
#
# #cursors department
#
#
# listbox_enter=tk.Label(f,text="Cursor style",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# listbox_enter.pack()
#
#
#
# cursor_size=tk.Label(f,text="Cursor size",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# cursor_size.pack()
# cursor_size_enter=tk.Entry(f)
# cursor_size_enter.bind("<Return>")
# cursor_size_enter.bind("<FocusOut>")
# cursor_size_enter.bind("<Return>")
# cursor_size_enter.pack()
#
#
#
# #on click dept
#
#
#
#
#
#
#
# #finish onclick dept
#
#
# #Window area
# win=tk.Label(f,text="Window properties",bd=1,background="#6D7993",fg="#fef1e8")
# win.pack()
#
# win_name=tk.Label(f,text="Window name",width=15,bd=1, background="#6D7993",fg="#fef1e8")
# win_name.pack()
# win_name_enter=tk.Entry(f,width=20)
#
# win_name_enter.pack()
#
#
# win_icon=tk.Label(f,text="Window Icon",bd=1,width="15",background="#6D7993",fg="#fef1e8")
# win_icon.pack()
#
#
#
# #Taskbar properties
#
#
# taskbar=tk.Label(f,text="TaskBar Properties",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# taskbar.pack()
#
# X_taskbar=tk.Label(f,text="X co-ordinates",width=5,bd=1,background="#6D7993",fg="#fef1e8")
# X_taskbar.pack()
# X_taskbar_enter=tk.Entry(f)
#
# X_taskbar_enter.pack()
#
#
# Y_taskbar=tk.Label(f,text="Y co-ordinates",width=5,bd=1,background="#6D7993",fg="#fef1e8")
# Y_taskbar.pack()
# Y_taskbar_enter=tk.Entry(f)
#
# Y_taskbar_enter.pack()
#
#
#
#
# taskbar_color=tk.Label(f,text="Taskbar color",width=15,bd=1,background='#6D7993',fg="#fef1e8")
# taskbar_color.pack()
# taskbar_color_enter=tk.Entry(f)
#
# taskbar_color_enter.pack()
#
# taskbar_border=tk.Label(f,text="Taskbar border",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# taskbar_border.pack()
# taskbar_border_enter=tk.Entry(f)
#
# taskbar_border_enter.pack()
#
# taskbar_height=tk.Label(f,text="Taskbar height",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# taskbar_height.pack()
# taskbar_height_enter=tk.Entry(f)
# taskbar_height_enter.bind("<Return>")
# taskbar_height_enter.bind("<FocusOut>")
# taskbar_height_enter.bind("<Return>")
# taskbar_height_enter.pack()
#
# taskbar_width=tk.Label(f,text="Taskbar width",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# taskbar_width.pack()
# taskbar_width_enter=tk.Entry(f)
# taskbar_width_enter.bind("<Return>")
# taskbar_width_enter.bind("<FocusOut>")
# taskbar_width_enter.bind("<Return>")
# taskbar_width_enter.pack()
#
# taskbar_icon=tk.Label(f,text="Taskbar icons",width=15,bd=1,background="#6D7993",fg="#fef1e8")
# taskbar_icon.pack()
#
#
#
# #Removed the frame packing
# #f.pack()
#
# #Updated the screen before calculating the scrollregion
# root.update()
# c.config(scrollregion=c.bbox("all"))
#
# root.mainloop()



import tkinter as tk

main=tk.Tk()

btn=tk.Button(text="harsh",anchor=tk.CENTER)
btn.pack()
main.mainloop()
