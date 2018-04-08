__author__ = 'Harsh'
import tkinter as tk


#this file manages widgets data , changes widgets data in the windows , initialises its property values and saves all the data in a dict and list
frames=[]
widget_props={}
widget_init={}     #has all the list of widgets with id name {id:widget}
button_command={}
btn=0
etry=0
copy_widget=''     # single copied widget data placed here
copy_widgets=[]    #multiple selected widgets list to paste when required
import time

def save_widget_props(widget,variables):      #this function invokes each time a value of the widget is changed so that dict is maintained for props of widgets

    if(widget.winfo_class()!="Entry"):
        variables[1].set(widget.cget('height'))

    variables[0].set(widget.cget('text'))
    #properties_tab.he.set(widget.cget('height'))
    variables[2].set(widget.cget('width'))
    variables[3].set(widget.cget('fg'))
    variables[4].set(widget.cget('font'))
    variables[5].set(widget.cget('font'))
    #properties_tab.aln.set(widget.cget('orient'))
    #properties_tab.acn.set(widget.cget('text'))
    variables[8].set(widget.cget('bd'))
    variables[9].set(widget.cget('background'))
    variables[10].set(widget.cget('highlightbackground'))

def change_property():   #this function deals with changing the value of the properties tab on changing or clicking on the widget
    print()
#functionns for keys(widget id)
def init_widget(widget):                 #this widgets gets invoked when we put widgets first time in firstclick.py
                                         # and it saves all the widgets name in widget_init[]

    key=get_key(widget)

    widget_init.update({key:widget})
    #print("dictionary",widget_init)

    #print(widget_init[0].cget('text'))

def change_command(widget,command,default):    #this function gets invokes for changing the command for a button. set the specific command attribute
    #for each button
    flag=0
    for k,v in button_command.items():     #if  we are changing the command then finding the command item and replacing.
        #print(v)
        if(v==widget):
            flag=1
            button_command[command]=button_command[k]
            del button_command[k]
            break
    if(flag==0):    #if the command is first time for a button.
        button_command.update({command:widget})
    print(button_command)



def get_key(widget):        #this functions creates the keys and returns it
    global btn,etry
    if(widget.winfo_class()=="Button"):
        btn+=1
    if(widget.winfo_class()=="Entry"):
        etry+=1
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
def find_command(widget):                     #this function finds key for the window so that the key can be put in entry box each time
    for k,v in button_command.items():
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
