__author__ = 'harsh'

#
# #making scrollbar
# import tkinter as tk
# root = tk.Tk()
# frame=tk.Frame(root,width="200",height="200")
# canvas=tk.Canvas(frame,height="123",width="25",background="#dddddd")
# canvas.create_rectangle(2,2,25,25,fill="#dddddd")
# canvas.create_line(7,8,15,15)
# canvas.create_line(15,15,23,8)
# canvas.create_image(image="")
# #canvas.create_line(7,8,17,8)
# canvas.create_rectangle(2,25,25,100,fill="#999999")
# canvas.create_rectangle(2,100,25,123,fill="#dddddd")
# canvas.pack()
# frame.pack()
# root.mainloop()



#making arrows
import tkinter as tk
root=tk.Tk()
def focus_change(event):
        event.widget.configure(background="#777777")
def focus_reset(event):
        event.widget.configure(background="#333333")
btn=tk.Button(root,text="button",background="#555555")
btn.bind('<Enter>',focus_change)
btn.bind('<Leave>',focus_reset)
btn.pack()


entry=tk.Entry(width=10)
entry.pack()
# canvas=tk.Canvas(height="100",width="200",background="#dddddd")
# canvas.create_line(,8,15,15)
# canvas.pack()
root.mainloop()