__author__ = 'Harsh'
import tkinter as tk

frames=[]
widget_init={}
btn=0
import time
def get_key(widget):
    print('widget class',widget.winfo_class())
    global btn
    if(widget.winfo_class()=="Button"):
        btn+=1
        return "btn"+str(btn)
def init_widget(widget):                 #this widgets gets invoked when we put widgets first time in firstclick.py
                                         # and it saves all the widgets name in widget_init[]

    key=get_key(widget)

    widget_init.update({key:widget})
    print("dictionary",widget_init)

    #print(widget_init[0].cget('text'))

def change_key(widget,key,default):               #invokes when we want to change the key (button id) of the widget in dict
    for k,v in widget_init.items():
        print(v)
        if(v==widget):
            print('inside')
            #widget_init[key]=v
            widget_init[key]=widget_init[k]
            del widget_init[k]
            break



    print(widget_init)



def find_key(widget):
    for k,v in widget_init.items():
        print(v)
        if(v==widget):
            return k

def update_widget(widget):              # called each time a property changes
    print('changed',widget_init)
    # for i in range(len(widget_init)):
    #     if(widget_init[i]==widget):
    #         print('old',widget_init[i].cget("text"))
    #         widget_init[i]=widget
    #
    #         print('new',widget_init[i].cget('text'))

def frame_append(object):
    frames.append(object)




def sync_data():
    print(widget_init)

    a=''
    for f in widget_init:
        print('here')
        
        print(f.winfo_class())

        if(f.winfo_class()=="Button"):
            print("for button")
            a+="        "+str(f.winfo_class())+str(f.cget('text'))+"=tk."+str(f.winfo_class())+"(self,text=\""+str(f.cget('text'))+"\",height="+str(f.cget('height'))+",width="+str(f.cget('width'))+",background=\""+str(f.cget('background'))+"\",foreground=\""+f.cget('fg')+"\",relief=tk."+str(f.cget('relief')).upper()+",bd="+str(f.cget('bd'))+")\n        "+str(f.winfo_class())+str(f.cget('text'))+".place(x="+str(f.winfo_x())+",y="+str(f.winfo_y()+20)+")\n"
        elif(f.winfo_class()=="Radiobutton"):
            print("for radiobutton")
        elif(f.winfo_class()=="Checkbutton"):
            print("for checkbuttn")
        elif(f.winfo_class()=="Entry"):
            print('for entry')
            a+="        "+str(f.winfo_class())+str(f.cget('text'))+"=tk."+str(f.winfo_class())+"(self,text=\""+str(f.cget('text'))+"\",background=\""+str(f.cget('background'))+"\",foreground=\""+f.cget('fg')+"\",relief=tk."+str(f.cget('relief')).upper()+",bd="+str(f.cget('bd'))+")\n        "+str(f.winfo_class())+str(f.cget('text'))+".place(x="+str(f.winfo_x()+20)+",y="+str(f.winfo_y()+20)+")\n"
        elif(f.winfo_class()=="label"):
            print("for label")
        elif(f.winfo_class()=="TScrollbar"):
            print("for scroll")
        elif(f.winfo_class()=="Tprogressbar"):
            print("for progressbar")
        elif(f.winfo_class()=="Spinbox"):
            print("for spinbox")
        elif(f.winfo_class()=="TCombobox"):
            print("for combobox")
        elif(f.winfo_class()=="Listbox"):
            print("for listbox")

        else:

            a+="        "+str(f.winfo_class())+str(f.cget('text'))+"=tk."+str(f.winfo_class())+"(self,text=\""+str(f.cget('text'))+"\",height="+str(f.cget('height'))+",width="+str(f.cget('width'))+",background=\""+str(f.cget('background'))+"\",foreground=\""+f.cget('fg')+"\",relief=tk."+str(f.cget('relief')).upper()+",bd="+str(f.cget('bd'))+")\n        "+str(f.winfo_class())+str(f.cget('text'))+".place(x="+str(f.winfo_x()+20)+",y="+str(f.winfo_y()+20)+")\n"
        #print(a)
    return a
