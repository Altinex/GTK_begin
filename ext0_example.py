import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World", default_width=400, default_height=300)

        self.button = Gtk.Button(label="Click Here", margin=50)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print(dir(MyWindow.props))
        print("================")
        print(dir(Gtk.Button.props))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
