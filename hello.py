
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Creating window
window = Gtk.Window(title="Hello World")
# Show window
window.show()
# Connect to delete event (push to x stop main loop)
window.connect("destroy", Gtk.main_quit)
# Run main loop
Gtk.main()
