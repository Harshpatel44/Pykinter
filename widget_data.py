__author__ = 'harsh'
import functions
import tkinter as tk
#this file manages all the widgets data
main_list=[]
def get_data(widget,key,data):
    if functions.selected not in main_list:    #if new element
        a={functions.selected:{'key':'b1'}}
        print(type(a))
        main_list.append({functions.selected:{'key':'b1'}})
        #print(main_list)


    print(main_list)
    main_list[0]
    # print(main_list[0].winfo_class())
    # for i in main_list[0].keys():
    # #print(main_list[0].config())
    #     print(main_list[0].cget(i))
