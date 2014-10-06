import grabbo, os, webbrowser
from gi.repository import Gtk

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

AD_UI = os.path.join(r, 'ui', 'AboutDialog.xml')


class AboutDialog(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)

        self.ui =  grabbo.Builder(AD_UI).ui

        self._HomeButton = self.ui.get_object("HomeButton")
        self._LicenseButton = self.ui.get_object("LicenseButton")
        self._AboutButton = self.ui.get_object("AboutButton")
        self._RapportButton = self.ui.get_object("RapportButton")
        self.Logo = self.ui.get_object("Logo")
        self._TextView = self.ui.get_object("Text")
        self._ShortDescrpition = self.ui.get_object("ShortDescrpition")
        self._Name = self.ui.get_object("Name")
        self._Version = self.ui.get_object("Version")

        self._InfoBox = self.ui.get_object("InfoBox")
        self._HeaderBox = self.ui.get_object("HeaderBox")

        self._HeaderBar = Gtk.HeaderBar()
        self._HeaderBar.set_custom_title(self._HeaderBox)
        #self._HeaderBar.set_decoration_layout("close")

        self.set_titlebar(self._HeaderBar)
        self.add(self._InfoBox)

        self._AboutButton.hide()

        self._AboutButton.connect("clicked", self.on_about)
        self._HomeButton.connect("clicked", self.on_home)
        self._RapportButton.connect("clicked", self.on_rapport)

    def set_title(self, title):
        self._HeaderBar.set_title(title)

    def set_license_custom(self, textfile):
        self._custom_license = textfile
        self._LicenseButton.connect("clicked", self.on_custom_license)

    def on_custom_license(self, button):
        self._LicenseButton.hide()
        self._AboutButton.show()
        txt = open(self._custom_license, 'r').read()
        self._TextView.get_buffer().set_text(txt)

    def set_version(self, version):
        self._Version.set_label(version)

    def set_about_text(self, text):
        self._abouttext = text

    def set_home_page(self, url):
        self._home_page = url

    def set_rapport_page(self, url):
        self._rapport_page = url

    def on_about(self, button):
        self._LicenseButton.show()
        self._AboutButton.hide()
        txt = open(self._abouttext, 'r').read()
        self._TextView.get_buffer().set_text(txt)

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










