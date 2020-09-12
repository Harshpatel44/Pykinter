__author__ = 'Harsh'
import properties_tab

def set_properties(widget):
    print(widget.cget("text"))

    properties_tab.ne.set(widget.cget("text"))
    properties_tab.name_enter.update()
    print("done for this thing")