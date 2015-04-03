import grabbo, os, webbrowser
from gi.repository import Gtk

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

#AD_UI = os.path.join(r, 'ui', 'AboutDialog.xml')

class AD_UI(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)
        
        self._HomeButton = Gtk.Button("Web Page")
        self._Image1 = Gtk.Image().new_from_icon_name("go-home")
        self._HomeButton.set_image(self._Image1)
        
        self._LicenseButton = Gtk.Button("License")
        self._Image2 = Gtk.Image().new_from_icon_name("document-properties")
        self._LicenseButton.set_image(self._Image2)
        
        self._AboutButton = Gtk.Button("About")
        self._Image4 = Gtk.Image().new_from_icon_name("dialog-information")
        self._AboutButton.set_image(self._Image4)
        
        self._RapportButton = Gtk.Button("Rapport")
        self._Image3 = Gtk.Image().new_from_icon_name("dialog-warning")
        self._RapportButton.set_image(self._Image3)
        
        self._CloseButton = Gtk.Button()
        self._Image5 = Gtk.Image().new_from_icon_name("dialog-close")
        self._HomeButton.set_image(self._Image5)

        self.Logo = self.ui.get_object("Logo")
        self._TextView = self.ui.get_object("Text")
        self._ShortDescrpition = self.ui.get_object("ShortDescrpition")
        self._Name = self.ui.get_object("Name")
        self._Version = self.ui.get_object("Version")

        self._InfoBox = self.ui.get_object("InfoBox")
        self._HeaderBox = self.ui.get_object("HeaderBox")

        self._HeaderBar = Gtk.HeaderBar()
        self._HeaderBar.set_custom_title(self._HeaderBox)

class AboutDialog(AD_UI):
    def __init__(self):
        AD_UI.__init__(self)

        self.set_titlebar(self._HeaderBar)
        self.add(self._InfoBox)

        self._AboutButton.hide()

        self._AboutButton.connect("clicked", self.on_about)
        self._HomeButton.connect("clicked", self.on_home)
        self._RapportButton.connect("clicked", self.on_rapport)
        self._CloseButton.connect("clicked", self.on_close)

        self.connect("destroy", self.on_close)
        
    def preshow(self):
        self.set_custom_text(self._abouttext)
        self._InfoBox.show()
        self._HeaderBar.show()

    def on_close(self, button):
        self.close()

    def set_title(self, title):
        self._HeaderBar.set_title(title)

    def set_license_text_file(self, textfile):
        self._license_text = open(textfile, 'r').read()
        self._LicenseButton.connect("clicked", self.on_license_text)
        
    def set_license_text(self, text):
        self._license_text = text
        self._LicenseButton.connect("clicked", self.on_license_text)

    def on_license_text(self, button):
        self._LicenseButton.hide()
        self._AboutButton.show()
        self.set_custom_text(self._license_text)
        
    def set_license_link(self, link):
        self._license_link = link
        self._LicenseButton.connect("clicked", self.on_license_link)
        
    def on_license_link(self, button):
        self.open_link(self._license_link)

    def set_version(self, version):
        self._Version.set_label(version)

    def set_about_text(self, text):
        self._abouttext = text
        
    def set_about_text_file(self, textfile):
        self._abouttext = open(textfile, 'r').read()

    def set_custom_text(self, text):
        self._TextView.get_buffer().set_text(text)
        self._TextView.show()

    def set_home_page(self, url):
        self._home_page = url

    def set_rapport_page(self, url):
        self._rapport_page = url

    def on_about(self, button):
        self._LicenseButton.show()
        self._AboutButton.hide()
        self.set_custom_text(self._abouttext)

    def set_appname(self, name):
        self._Name.set_label(name)

    def set_shortdescrpition(self, text):
        self._ShortDescrpition.set_label(text)

    def open_link(self, url):
        webbrowser.open_new_tab(url)

    def on_rapport(self, button):
        self.open_link(self._home_page)

    def on_home(self, button):
        self.open_link(self._rapport_page)
        