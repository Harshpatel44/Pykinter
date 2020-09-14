import tkinter as tk
main=tk.Tk()

e1=tk.StringVar()
e2=tk.StringVar()

entry2=tk.Entry(text="harsh",textvariable=e2)
entry2.pack()

def do(event):
    widget=event.widget
    #string=widget.get()
    #e1=widget.cget('text')
    string=widget.cget('text')
    e1.set(string)
    #e1.set(e2,tk.END)
entry=tk.Entry(textvariable=e1)
entry.bind("<Return>",do)
entry.pack()
btn=tk.Button(text="Button")
btn.pack()
btn.bind("<Button-1>",do)

main.mainloop()