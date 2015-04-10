import grabbo, webbrowser
from gi.repository import Gtk


class AboutDialog(grabbo.Window):
    def __init__(self,
                 about_text = ["Some text about my awesome App", "string"],
                 report_page = "https://github.com/jeremi360/Grabbo/issues",
                 home_page = "https://github.com/jeremi360/Grabbo"):
        
        grabbo.Window.__init__(self)
        
        if about_text[1] == "string":
            self.set_about_text(about_text[0])
        elif about_text[1] == ("path" or "file"):
            self.set_about_text_file(about_text[0])
        
        self.set_repot_page(report_page)
        self.set_home_page(home_page)
        
        self._HeaderBox = Gtk.HBox()
        
        self._HomeButton = grabbo.HomeButton("Web Page")
        self._HomeButton.connect("clicked", self.on_home)
        self._HeaderBox.add(self._HomeButton)
        
        self._Image2 = Gtk.Image().new_from_icon_name("document-properties", 4)
        self._LicenseButton = grabbo.StandardButton("License", self._Image2)
        self._HeaderBox.add(self._LicenseButton)
        
        self._AboutButton = grabbo.AboutButton()
        self._AboutButton.connect("clicked", self.on_about)
        self._HeaderBox.add(self._AboutButton)
        self._AboutButton.hide()
        
        self._Image3 = Gtk.Image().new_from_icon_name("dialog-warning", 4)
        self._repotButton = grabbo.StandardButton("repot", self._Image3)
        self._repotButton.connect("clicked", self.on_repot)
        self._HeaderBox.add(self._repotButton)
        
        self._HeaderBar = Gtk.HeaderBar()
        self._HeaderBar.set_custom_title(self._HeaderBox)
        self.set_titlebar(self._HeaderBar)
        self._HeaderBar.set_show_close_button(True)
        self._HeaderBar.set_decoration_layout(":close")
        
        self._InfoBox = Gtk.VBox()
        InfoList = []
        
        self._Logo = Gtk.Image().new_from_icon_name("applications-development", 4)
        InfoList.append(self._Logo)
        
        self._Name = Gtk.Label()
        self._Name.set_markup("<b>AppName</b>")
        InfoList.append(self._Name)
        
        self._ShortDescrpition = Gtk.Label("Awesome App")
        InfoList.append(self._ShortDescrpition)
        
        self._Version = Gtk.Label("0.3")
        InfoList.append(self._Version)
        
        for w in InfoList:
            self._InfoBox.pack_start(w, False, False, 1)
        
        self._TextView = Gtk.TextView()
        self._scrolledwindow1 = Gtk.ScrolledWindow()
        self._scrolledwindow1.add(self._TextView)
        self._InfoBox.pack_start(self._scrolledwindow1, True, True, 1)
        
        self.add(self._InfoBox)
        
    def preshow(self):
        self.set_custom_text(self._abouttext)
        self._InfoBox.show()
        self._HeaderBar.show()
        self._AboutButton.hide()

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

    def set_repot_page(self, url):
        self._repot_page = url

    def on_about(self, button):
        self._LicenseButton.show()
        self._AboutButton.hide()
        self.set_custom_text(self._abouttext)
        
    def on_close(self, button):
        self.close()

    def set_appname(self, name):
        markup = "<b>" + name + "</b>"
        self._Name.set_label(markup)

    def set_shortdescrpition(self, text):
        self._ShortDescrpition.set_label(text)
        
    def get_logo(self):
        return self._Logo

    def open_link(self, url):
        webbrowser.open_new_tab(url)

    def on_repot(self, button):
        self.open_link(self._repot_page)

    def on_home(self, button):
        self.open_link(self._home_page)
        