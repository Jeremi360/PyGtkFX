import grabbo, os, webbrowser
from gi.repository import Gtk

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)


class AboutDialog(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)
        
        self._HeaderBox = Gtk.HBox()
        
        self._HomeButton = Gtk.Button("Web Page")
        self._Image1 = Gtk.Image().new_from_icon_name("go-home", 4)
        self._HomeButton.set_image(self._Image1)
        self._HomeButton.connect("clicked", self.on_home)
        self._HeaderBox.add(self._HomeButton)
        
        self._LicenseButton = Gtk.Button("License")
        self._Image2 = Gtk.Image().new_from_icon_name("document-properties", 4)
        self._LicenseButton.set_image(self._Image2)
        self._HeaderBox.add(self._LicenseButton)
        
        self._AboutButton = Gtk.Button("About")
        self._Image4 = Gtk.Image().new_from_icon_name("dialog-information", 4)
        self._AboutButton.set_image(self._Image4)
        self._AboutButton.connect("clicked", self.on_about)
        self._HeaderBox.add(self._AboutButton)
        self._AboutButton.hide()
        
        self._RapportButton = Gtk.Button("Rapport")
        self._Image3 = Gtk.Image().new_from_icon_name("dialog-warning", 4)
        self._RapportButton.set_image(self._Image3)
        self._RapportButton.connect("clicked", self.on_rapport)
        self._HeaderBox.add(self._RapportButton)
        
        self._HeaderBar = Gtk.HeaderBar()
        self._HeaderBar.set_custom_title(self._HeaderBox)
        self.set_titlebar(self._HeaderBar)
        self._HeaderBar.set_decoration_layout(":close")
        self._HeaderBar.set_name("About")
        
        self._InfoBox = Gtk.VBox()
        
        self._Logo = Gtk.Image().new_from_icon_name("applications-development", 4)
        self._InfoBox.add(self._Logo)
        
        self._TextView = Gtk.TextView()
        self._scrolledwindow1 = Gtk.ScrolledWindow()
        self._scrolledwindow1.add(self._TextView)
        self._InfoBox.add(self._scrolledwindow1)
        
        self._ShortDescrpition = Gtk.Label("Awesome App")
        self._InfoBox.add(self._ShortDescrpition)
        
        self._Name = Gtk.Label()
        self._Name.set_markup("<b>AppName</b>")
        self._InfoBox.add(self._Name)
        
        self._Version = Gtk.Label("0.3")
        self._InfoBox.add(self._Version)
        
        self.add(self._InfoBox)

        
    def preshow(self):
        self.set_custom_text(self._abouttext)
        self._InfoBox.show()
        self._HeaderBar.show()
        self.show_all()

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
        markup = "<b>" + name + "</b>"
        self._Name.set_label(markup)

    def set_shortdescrpition(self, text):
        self._ShortDescrpition.set_label(text)
        
    def get_logo(self):
        return self._Logo

    def open_link(self, url):
        webbrowser.open_new_tab(url)

    def on_rapport(self, button):
        self.open_link(self._home_page)

    def on_home(self, button):
        self.open_link(self._rapport_page)
        