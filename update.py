__author__ = 'Harsh'
import tkinter as tk
#this file manages widgets data , changes widgets data in the windows , initialises its property values and saves all the data in a dict and list
frames=[]
widget_props={}
widget_init={}     #has all the list of widgets with id name {id:widget}
btn=0
copy_widget=''     # single copied widget data placed here
copy_widgets=[]    #multiple selected widgets list to paste when required
import time

def save_widget_props():      #this function invokes each time a value of the widget is changed so that dict is maintained for props of widgets
    print()


#functionns for keys(widget id)
def init_widget(widget):                 #this widgets gets invoked when we put widgets first time in firstclick.py
                                         # and it saves all the widgets name in widget_init[]

    key=get_key(widget)

    widget_init.update({key:widget})
    #print("dictionary",widget_init)

    #print(widget_init[0].cget('text'))


def get_key(widget):                         #this functions creates the keys and returns it
    global btn
    btn+=1
    return str(widget.winfo_class())+str(btn)

def change_key(widget,key,default):               #invokes when we want to change the key (button id) of the widget in dict
    for k,v in widget_init.items():
        #print(v)
        if(v==widget):
            #print('inside')
            #widget_init[key]=v
            widget_init[key]=widget_init[k]
            del widget_init[k]
            break
    #print(widget_init)


def find_key(widget):                     #this function finds key for the window so that the key can be put in entry box each time
    for k,v in widget_init.items():
        #print(v)
        if(v==widget):
            return k

def remove_wid(widget):
      key=find_key(widget)
      widget_init.pop(key)
      print(widget_init)

def update_widget(widget):              # called each time a property changes
    print()
    #print('changed',widget_init)
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
