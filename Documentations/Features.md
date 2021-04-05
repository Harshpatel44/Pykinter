#### Features
* Create Templates and save for future use.
* Customizable taskbar, menubar.
* Double click to write methods for the events.
* An editor to write code + gui generation.
* Able to create rich gui applications using the IDE.



#### Discussion
* Frames packages contains UI for the application.
* All other packages have controller and service layer logic of the feature.
* On clicking a widget, a popup window will ask about widget name and basic properties (everything is optional and default values would be inserted), on clicking okay on the popup, a widget will be created at the center of the GUIWindow.



## When widgets will be created in GUI window, a dictionary will be created with all the information of the widgets.
gui_frame_widgets_props = {
  'widget1': {
    all the properties
  }
}

used all the time.

## Undo Redo (Stack data structure)
widgets_history = A json with key: widget_name, value: widget_type, widget_last position.

if stack n element and n-1 element name is same, element is moved.
else element is new created.

When Undo: remove the widget from dev_window_widgets and create it at a different place if its moved.

## GUIFrame configurations
gui_frame_config = A json file for GUIFrame configurations
used in: geometry tool, while resizing the window