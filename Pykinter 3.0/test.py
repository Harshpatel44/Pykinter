# import tkinter as tk
# main=tk.Tk()
#
# e1=tk.StringVar()
# e2=tk.StringVar()
#
# entry2=tk.Entry(text="harsh",textvariable=e2)
# entry2.pack()
#
# def do(event):
#     widget=event.widget
#     #string=widget.get()
#     #e1=widget.cget('text')
#     string=widget.cget('text')
#     e1.set(string)
#     #e1.set(e2,tk.END)
# entry=tk.Entry(textvariable=e1)
# entry.bind("<Return>",do)
# entry.pack()
# btn=tk.Button(text="Button")
# btn.pack()
# btn.bind("<Button-1>",do)
#
# main.mainloop()


import tkinter as tk
main = tk.Tk()
main.geometry("100x100")
# widget_frame_1 = tk.Frame(main, height=500, width=200, relief='ridge', background="black",
#                                  bd=1, highlightbackground="white")
# widget_frame_1.pack(side="left")
# widget_frame_2 = tk.Frame(main, height=500, width=200, relief='ridge', background="black",
#                                  bd=1, highlightbackground="white")
# widget_frame_2.pack(side="left")
# widget_frame_3 = tk.Frame(main, height=500, width=200, relief='ridge', background="black",
#                                  bd=1, highlightbackground="white")
# widget_frame_3.pack(side="left")
#
# frame2 = tk.Frame(widget_frame_1, height=20, width=200, relief='ridge', background="grey",
#                                  bd=1, highlightbackground="white")
# frame2.pack(side="left")
main.mainloop()


