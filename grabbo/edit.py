import grabbo
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

EB_UI = os.path.join(r, 'ui', 'EditBox.xml')

class EditBox(grabbo.Builder):
    def __init__(self, ValueToEdit):
        grabbo.Builder.__init__(self, EB_UI)

        self.value = ValueToEdit
        self.EditButton = self.ui.get_object("EditButton")
        self.entry = self.ui.get_object("entry")
        self.OKButton = self.ui.get_object("OKButton")
        self.NOButton = self.ui.get_object("NOButton")
        self.InBox = self.ui.get_object("InBox")

        self.EditButton.connect("toggled", self.on_edit)
        self.OKButton.connect("clicked", self.on_ok)
        self.NOButton.connect("clicked", self.on_ok)

        self.entry.connect("activate", self.on_ok)

        self.EditButton.show()
        self.InBox.hide()

    def get(self):
        return self.ui.get_object("box")

    def on_edit(self, button):
        if self.EditButton.get_state():
            self.entry.set_text(self.value)
            self.InBox.show_all()
        else:
            self.entry.set_text(self.value)
            self.InBox.hide()

    def on_ok(self, wiget):
        self.value = self.entry.get_text()
        self.InBox.hide()

    def on_no(self, button):
        self.entry.set_text(self.value)



