__author__ = 'Harsh'

# in this file , the widget gets placed after getting clicked in widgets tab. creation of all the widgets and layouts of deafult widgets is
# done in this file.
from tkinter import ttk
import tkinter as tk
from widgets.old import functions
from old.program_editor import update

bg_color = "#fef1e8"


def allTime(dev_window_obj):
    global l1, l2, r1, r2, u, d, rect, l, r, rc

    l1 = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)  # creation of 6 dots which makes the selected part of the widget
    l1.place_forget()
    l2 = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)
    l2.place_forget()  # to hide the widget
    r1 = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)
    r1.place_forget()
    r2 = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)
    r2.place_forget()
    u = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)
    u.place_forget()
    d = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)
    d.place_forget()
    l = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)
    l.place_forget()
    r = tk.Canvas(dev_window_obj.working_window, bd=0, highlightthickness=0)
    r.place_forget()
    rc = tk.Canvas(dev_window_obj.centre_frame, height=177, width=160, background="#f7f7f7", bd=0)
    rc.place_forget()
    # rect=root.create_rectangle(0,0,200,200,fill="red")


def moveIn_MF(event, arg):  # when pressed in middle frame , to hide the selection
    widget = event.widget
    widget.bind("<Button-1>", lambda event: forget_all(arg))


def forget_all(root):  # to hide the selection dots
    l1.place_forget()
    l2.place_forget()
    r1.place_forget()
    r2.place_forget()
    u.place_forget()
    d.place_forget()
    l.place_forget()
    r.place_forget()
    rc.place_forget()
    update.clear_selectiondots()  # clears all the selection dots
    update.selected_widget.clear()  # clears the list containing all the widgets that are selected
    root.configure(highlightbackground="#555555")
    print('selected list', update.selected_widget)


def startMultiSelect(event):  # this invokes when we click in working window
    l1.place_forget()  # place forget all the selection dots
    l2.place_forget()
    r1.place_forget()
    r2.place_forget()
    u.place_forget()
    d.place_forget()
    l.place_forget()
    r.place_forget()
    rc.place_forget()
    update.clear_selectiondots()  # clears all the selection dots
    update.selected_widget.clear()  # clears the list containing all the widgets that are selected
    print('selected list', update.selected_widget)


def moveIn_Frame(event_main, centre_frame, taskbar, working_window):  # bindings when we enter in centre frame

    working_window.bind("<Button-1>", lambda event, arg=working_window: startMultiSelect(
        centre_frame))  # to hide the selection_lines when clicked on the frame
    # provide motion and drag the main_frame when taskbar is dragged
    taskbar.bind("<Button-1>", lambda event, arg=taskbar, arg2=centre_frame: functions.start_frame(event, arg, arg2))
    taskbar.bind("<B1-Motion>", lambda event, arg=taskbar, arg2=centre_frame: functions.motion_frame(event, arg, arg2))
    taskbar.bind("<ButtonRelease-1>", lambda event, arg2=centre_frame: functions.stop_frame(event, arg2))


def button(root, root_parent):  # bindings for buttons

    B1 = tk.Button(root, text="Button", height=1, bd=0, width=10, background=bg_color, relief=tk.RAISED)
    B1.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    B1.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    B1.bind("<B1-Motion>", lambda event, arg=B1, arg2=root: functions.motion(event, arg2))
    update.init_widget(B1)
    B1.place(x=10, y=10)


def check_button(root):  # bindings for check buttons
    check = tk.Checkbutton(root, text="Button", height=1, bd=1, width=10, background=bg_color)
    check.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    check.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    check.bind("<B1-Motion>", lambda event, arg=check, arg2=root: functions.motion(event, arg2))
    update.init_widget(check)
    check.place(x=10, y=10)


def radio_button(root):  # bindings for radio button
    radio = tk.Radiobutton(root, text="Button", height=1, bd=1, width=10, background=bg_color)
    radio.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    radio.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    radio.bind("<B1-Motion>", lambda event, arg=radio, arg2=root: functions.motion(event, arg2))
    update.init_widget(radio)
    radio.place(x=10, y=10)


def entry_button(root):  # bindings for entry button
    entry = tk.Entry(root, background=bg_color)
    entry.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    entry.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    entry.bind("<B1-Motion>", lambda event, arg=entry, arg2=root: functions.motion(event, arg2))
    update.init_widget(entry)
    entry.place(x=10, y=10)


def label_click(root):  # bindings for label click
    label = tk.Label(root, text="Label", background=bg_color)
    label.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    label.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    label.bind("<B1-Motion>", lambda event, arg=label, arg2=root: functions.motion(event, arg2))
    update.init_widget(label)
    label.place(x=10, y=10)


def scroll_click(root):  # bindings for scroll click
    scrollbar = ttk.Scrollbar(root)
    # ttk.Scale(root,length=10)
    # scale=ttk.Scale(root,length=200,orient=tk.VERTICAL)
    # scale.place(x=10,y=10,height=100)
    # scrollbar=''
    # def button():
    #     global scrollbar,image
    #     scrollbar = tk.Label(root,bd=0)
    #
    #     scrollbar.config(image=middle_frame2.image)
    #     scrollbar.image = middle_frame2.image
    #     scrollbar.place(x=10,y=10)
    # button()
    scrollbar.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    scrollbar.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    scrollbar.bind("<B1-Motion>", lambda event, arg=scrollbar, arg2=root: functions.motion(event, arg2))
    update.init_widget(scrollbar)
    scrollbar.place(x=10, y=10, height=100)


def dropmenu_click(root):  # bindings for option menu
    variable = ttk.StringVar(root)
    variable.set('Item1')
    dropmenu = tk.OptionMenu(root, variable, "Item1", "Item2", "Item3")
    dropmenu.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    dropmenu.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    dropmenu.bind("<B1-Motion>", lambda event, arg=dropmenu, arg2=root: functions.motion(event, arg2))
    update.init_widget(dropmenu)
    dropmenu.place(x=10, y=10)


def combobox_click(root):
    combobox = ttk.Combobox(root, background=bg_color)
    combobox.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    combobox.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    combobox.bind("<B1-Motion>", lambda event, arg=combobox, arg2=root: functions.motion(event, arg2))
    update.init_widget(combobox)
    combobox.place(x=10, y=10)


def progressbar_click(root):
    progressbar = ttk.Progressbar(root, length=100)
    progressbar.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    progressbar.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    progressbar.bind("<B1-Motion>", lambda event, arg=progressbar, arg2=root: functions.motion(event, arg2))
    update.init_widget(progressbar)
    progressbar.place(x=10, y=10)


def listbox_click(root):
    listbox = tk.Listbox(root, background=bg_color)
    listbox.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    listbox.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    listbox.bind("<B1-Motion>", lambda event, arg=listbox, arg2=root: functions.motion(event, arg2))
    update.init_widget(listbox)
    listbox.place(x=10, y=10)


def image_click(root):
    imagecanvas = tk.Button(root, background=bg_color)
    imagecanvas.configure(height="10", width="10", relief="flat", bd=0, text="Image Here", fg="black")

    imagecanvas.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    imagecanvas.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    imagecanvas.bind("<B1-Motion>", lambda event, arg=imagecanvas, arg2=root: functions.motion(event, arg2))
    update.init_widget(imagecanvas)
    imagecanvas.place(x=10, y=10)


def spinbox_click(root):
    spinbox = tk.Spinbox(root, background=bg_color)
    spinbox.bind("<Button-1>", lambda event, arg2=root, arg3=rc: functions.start_btn(event, arg2, arg3))
    spinbox.bind("<ButtonRelease-1>", lambda event, arg2=root: functions.stop_btn(event, arg2))
    spinbox.bind("<B1-Motion>", lambda event, arg=spinbox, arg2=root: functions.motion(event, arg2))
    update.init_widget(spinbox)
    spinbox.place(x=10, y=10)
