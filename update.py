__author__ = 'Harsh'
import tkinter as tk
frames=[]
properties=[]
def get_data(widget):
    print(widget)
    #print(widget.cget('text'))
    properties.append(widget)

def frame_append(object):
    frames.append(object)



def sync_data():
    a=''
    for f in properties:
        print(f.winfo_class())
        if(f.winfo_class()=="Entry"):
            a+="        "+str(f.winfo_class())+str(f.cget('text'))+"=tk."+str(f.winfo_class())+"(self,text=\""+str(f.cget('text'))+"\",background=\""+str(f.cget('background'))+"\",foreground=\""+f.cget('fg')+"\",relief=tk."+str(f.cget('relief')).upper()+",bd="+str(f.cget('bd'))+")\n        "+str(f.winfo_class())+str(f.cget('text'))+".place(x="+str(f.winfo_x()+20)+",y="+str(f.winfo_y()+20)+")\n"
        else:
            a+="        "+str(f.winfo_class())+str(f.cget('text'))+"=tk."+str(f.winfo_class())+"(self,text=\""+str(f.cget('text'))+"\",height="+str(f.cget('height'))+",width="+str(f.cget('width'))+",background=\""+str(f.cget('background'))+"\",foreground=\""+f.cget('fg')+"\",relief=tk."+str(f.cget('relief')).upper()+",bd="+str(f.cget('bd'))+")\n        "+str(f.winfo_class())+str(f.cget('text'))+".place(x="+str(f.winfo_x()+20)+",y="+str(f.winfo_y()+20)+")\n"
        #print(a)
    return a
