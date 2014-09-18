from grabbo.builder import Builder
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

LI_UI = os.path.join(r, 'ui', 'ListItem.xml')

class ListItem(Builder):
    def __init__(self, label, parent):
        Builder.__init__(self, LI_UI)
        self.button = self.ui.get_object("Item")
        self.remove = self.ui.get_object("Remove")
        self.parent = parent

        self.button.set_label(label)

    def get(self):
        return self.ui.get_object("box")

    def on_remove(self, button):
        self.parent.remove(self.get())




