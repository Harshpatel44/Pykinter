__author__ = 'Harsh'

import tkinter as tk
from widgets import first_click
from application_standards import constants as const


class WidgetsTab:
    def __init__(self, main):
        self.main = main

        self.title_height = self.main.h * const.bar_height
        self.title_width = self.main.w * const.widget_frame_width

        self.widget_area_width = self.main.w * const.widget_frame_width
        self.widget_area_height = self.main.h * const.widget_area_height - self.main.h * const.bar_height

        self.button_width = round(self.main.w * const.widgets_button_width)
        self.button_height = round(self.main.h * const.widgets_button_height)
        self.button_x = (self.widget_area_width - self.button_width) / 2
        self.button_y = (self.widget_area_height / 16.5)

        self.widget_font_size = const.widgets_font_size
        self.widget_font = "Courier New"

        self.tab_layout()
        self.tab_buttons()

    def tab_layout(self):
        """ Creating UI Layout"""
        # def on_configure(event):
        #     """ update scrollregion after starting 'mainloop', when all widgets are in canvas """
        #     widget_area_canvas.configure(scrollregion=widget_area_canvas.bbox('all'))

        # widget_area_canvas= tk.Canvas(self.main.widget_frame,scrollregion=(0,0,600,600),
        #                               width=self.widget_area_width,
        #                               height=self.widget_area_height, background="grey")
        #
        # scrollbar=tk.Scrollbar(self.main.widget_frame,command=widget_area_canvas.yview)
        # scrollbar.place(x=20,y=26,height=self.widget_area_height)
        #
        # widget_area_canvas.configure(yscrollcommand=scrollbar.set)
        # widget_area_canvas.bind('<Configure>', on_configure)
        # widget_area_canvas.place(x=0,y=0)

        title = tk.Frame(self.main.widget_frame, height=self.title_height, width=self.title_width,
                         bd=1, relief="raised", background=const.bg_color, highlightbackground=const.main_border)
        title.pack(side="top", fill="both", expand=1)

        self.widget_frame = tk.Frame(self.main.widget_frame, background=const.bg_color, width=self.widget_area_width,
                                height=self.widget_area_height)
        self.widget_frame.pack(side="top")
        # widget_area_canvas.create_window((0,0),window=widget_frame,anchor='nw')
        """ UI Layout Complete """

        title_label = tk.Label(title, text="Widgets", background=const.bg_color, fg=const.primary_font_color)
        title_label.config(font=(const.primary_font, 9))
        title_label.pack(side="top")
        
    def tab_buttons(self):
        button = tk.Button(self.widget_frame, text="Button", bd=0, background="#6D7993", fg="#FFFFFF",
                           relief=tk.SUNKEN, command=lambda: first_click.button(working_window, self.main.dev_frame))
        button.config(font=(self.widget_font, self.widget_font_size))
        button.place(x=self.button_x, y=self.button_y - self.button_height, height=self.button_height, width=self.button_width)
        #
        tool_button = tk.Button(self.widget_frame, text="Tool Button", height=1, width=10, bd=0,
                                background="#6D7993", fg="#FFFFFF", relief=tk.RAISED)
        tool_button.config(font=(self.widget_font, self.widget_font_size))
        tool_button.place(x=self.button_x, y=(self.button_y * 2) - self.button_height, height=self.button_height, width=self.button_width)
        #
        radio_button = tk.Button(self.widget_frame, text="Radio Button", height=1, bd=0, width=15, background="#6D7993",
                                 fg="#FFFFFF", relief=tk.SUNKEN,
                                 command=lambda: first_click.radio_button(working_window))
        radio_button.config(font=(self.widget_font, self.widget_font_size))
        radio_button.place(x=self.button_x, y=(self.button_y * 3) - self.button_height, height=self.button_height, width=self.button_width)
        #
        check_button = tk.Button(self.widget_frame, text="Check Button", height=1, bd=0, width=15, background="#6D7993",
                                 fg="#FFFFFF", relief=tk.GROOVE,
                                 command=lambda: first_click.check_button(working_window))
        check_button.config(font=(self.widget_font, self.widget_font_size))
        check_button.place(x=self.button_x, y=(self.button_y * 4) - self.button_height, height=self.button_height, width=self.button_width)
        #
        entrybox=tk.Button(self.widget_frame,text="Entry Box",height=1,bd=0,width=15,background="#6D7993",
                           fg="#FFFFFF",relief=tk.SOLID,command= lambda: first_click.entry_button(working_window))
        entrybox.config(font=(self.widget_font,self.widget_font_size))
        entrybox.place(x=self.button_x, y=(self.button_y * 5) - self.button_height, height=self.button_height, width=self.button_width)
        #
        label=tk.Button(self.widget_frame, text="Label", height=1, bd=0,width=15, background="#6D7993",
                        fg="#FFFFFF", relief="solid", command=lambda:first_click.label_click(working_window))
        label.config(font=(self.widget_font,self.widget_font_size))
        label.place(x=self.button_x, y=(self.button_y * 6) - self.button_height, height=self.button_height, width=self.button_width)
        #
        scroll_bar=tk.Button(self.widget_frame,text="Scroll Bar",height=1,bd=0,width=15,background="#6D7993",
                             fg="#FFFFFF",relief="solid",command=lambda:first_click.scroll_click(working_window))
        scroll_bar.config(font=(self.widget_font,self.widget_font_size))
        scroll_bar.place(x=self.button_x, y=(self.button_y * 7) - self.button_height, height=self.button_height, width=self.button_width)
        #
        progress_bar=tk.Button(self.widget_frame,text="Progress Bar",height=1,bd=0,width=15,background="#6D7993",
                               fg="#FFFFFF",relief="solid",command=lambda:first_click.progressbar_click(working_window))
        progress_bar.config(font=(self.widget_font,self.widget_font_size))
        progress_bar.place(x=self.button_x, y=(self.button_y * 8) - self.button_height, height=self.button_height, width=self.button_width)
        #
        spin_box=tk.Button(self.widget_frame,text="Spin Box",height=1,bd=0,width=15,background="#6D7993",
                           fg="#FFFFFF",relief="solid",command=lambda:first_click.spinbox_click(working_window))
        spin_box.config(font=(self.widget_font,self.widget_font_size))
        spin_box.place(x=self.button_x, y=(self.button_y * 9) - self.button_height, height=self.button_height, width=self.button_width)
        #
        combo_box=tk.Button(self.widget_frame,text="Combo Box",height=1,bd=0,width=15,background="#6D7993",
                            fg="#FFFFFF",relief="solid",command=lambda:first_click.combobox_click(working_window))
        combo_box.config(font=(self.widget_font,self.widget_font_size))
        combo_box.place(x=self.button_x, y=(self.button_y * 10) - self.button_height, height=self.button_height, width=self.button_width)
        #
        drop_view=tk.Button(self.widget_frame,text="Drop View",height=1,bd=0,width=15,background="#6D7993",
                            fg="#FFFFFF",relief="solid",command=lambda:first_click.dropmenu_click(working_window))
        drop_view.config(font=(self.widget_font,self.widget_font_size))
        drop_view.place(x=self.button_x, y=(self.button_y * 11) - self.button_height, height=self.button_height, width=self.button_width)
        #
        list_view=tk.Button(self.widget_frame,text="List View",height=1,bd=0,width=15,background="#6D7993",
                            fg="#FFFFFF",relief="solid",command=lambda:first_click.listbox_click(working_window))
        list_view.config(font=(self.widget_font,self.widget_font_size))
        list_view.place(x=self.button_x, y=(self.button_y * 12) - self.button_height, height=self.button_height, width=self.button_width)
        #
        frame=tk.Button(self.widget_frame,text="Frame",height=1,bd=0,width=15,background="#6D7993",
                        fg="#FFFFFF",relief="solid")
        frame.config(font=(self.widget_font,self.widget_font_size))
        frame.place(x=self.button_x, y=(self.button_y * 13) - self.button_height, height=self.button_height, width=self.button_width)
        #
        spiner=tk.Button(self.widget_frame,text="Spiner",height=1,bd=0,width=15,background="#6D7993",
                         fg="#FFFFFF",relief="solid")
        spiner.config(font=(self.widget_font,self.widget_font_size))
        spiner.place(x=self.button_x, y=(self.button_y * 14) - self.button_height, height=self.button_height, width=self.button_width)
        #
        shapes=tk.Button(self.widget_frame,text="Shapes",height=1,bd=0,width=15,background="#6D7993",
                         fg="#FFFFFF",relief="solid")
        shapes.config(font=(self.widget_font,self.widget_font_size))
        shapes.place(x=self.button_x, y=(self.button_y * 15) - self.button_height, height=self.button_height, width=self.button_width)
        #
        image_insert=tk.Button(self.widget_frame,text="Image",height=1,bd=0,width=15,background="#6D7993",
                               fg="#FFFFFF",relief="solid",command=lambda:first_click.image_click(working_window))
        image_insert.config(font=(self.widget_font,self.widget_font_size))
        image_insert.place(x=self.button_x, y=(self.button_y * 16) - self.button_height, height=self.button_height, width=self.button_width)
