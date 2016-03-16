import os, sys, webbrowser
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import grabbo
from grabbo import markup
from gi.repository import Gtk

class AboutDialog(grabbo.Window):
    def __init__(self,
                 app_name = "App Name",
                 short_des = "Short App Descrpition",
                 home_page = "http://app_home_page.com",
                 report_page = "http://app_home_page.com/raport_bugs"):

        grabbo.Window.__init__(self)

        self._HeaderBox = Gtk.HBox()

        self._HomeButton = grabbo.HomeButton("Web Page")
        self._HomeButton.connect("clicked", self.on_home)

        self._Image3 = Gtk.Image().new_from_icon_name("dialog-warning", 4)
        self._ReportButton = grabbo.StandardButton("report", self._Image3)
        self._ReportButton.connect("clicked", self.on_report)

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
        InfoList.append(self._Name)

        self._ShortDescrpition = Gtk.Label()
        InfoList.append(self._ShortDescrpition)

        self._Version = Gtk.Label("0.3")
        InfoList.append(self._Version)

        for w in InfoList:
            self._InfoBox.pack_start(w, False, False, 1)

        self._TextAbout = Gtk.Label()
        sw1 = Gtk.ScrolledWindow()
        sw1.add(self._TextAbout)

        self._TextLicense = Gtk.Label()
        sw2 = Gtk.ScrolledWindow()
        sw2.add(self._TextLicense)

        left = Gtk.Justification.LEFT
        center = Gtk.Justification.CENTER
        self._TextAbout.set_justify(left)
        self._TextLicense.set_justify(center)

        self._TextStack = Gtk.Stack()
        self._TextStack.add_titled(sw1, "about", "About")
        self._TextStack.add_titled(sw2, "license", "License")

        self._TextSwitcher = Gtk.StackSwitcher()
        self._TextSwitcher.set_stack(self._TextStack)

        self._HeaderBox.add(self._HomeButton)
        self._HeaderBox.add(self._TextSwitcher)
        self._HeaderBox.add(self._ReportButton)

        self._InfoBox.pack_start(self._TextStack, True, True, 1)

        self.add(self._InfoBox)

        self.set_appname(app_name)
        self.set_shortdescrpition(short_des)
        self.set_report_page(report_page)
        self.set_home_page(home_page)

        self._license_file = ""
        self._about_file = ""

    def _new_text(self, name):
        newtext = Gtk.Label()
        sw = Gtk.ScrolledWindow()
        sw.add(newtext)
        self._TextStack.add_titled(sw, name.lower(), name.capitalize())
        return newtext

    def add_text(self, text, name):
        t = self._new_text(name)
        t.set_text(text)

    def add_text_file(self, text_file_path, name):
        self.add_text(open(text_file_path, 'r').read())

    def add_markdown_file(self, markdown_file_path, name):
        m = markup.markdown_file(markdown_file_path)
        t = self._new_text(name)
        t.set_markup(m)

    def set_title(self, title):
        self._HeaderBar.set_title(title)

    def set_version(self, version):
        self._Version.set_label(version)

    def set_license_text(self, text):
        buff = self._TextLicense
        buff.set_text(text)

    def set_license_text_file(self, text_file_path):
        self.set_license_text(open(text_file_path, 'r').read())
        self._license_file = text_file_path

    def set_license_file(self, textfile):
        buff = self._TextLicense
        self._license_file = textfile
        m = markup.license_file(textfile)
        buff.set_markup(m)

    def set_license_keywords(self, dkws):
        lic = self._license_file
        m = markup.license_file(lic).splitlines()

        nl = []

        for s in m:
            for i in dkws.items():
                s = s.replace("{" + i[0] + "}", i[1])

            nl.append(s)

        nl = os.linesep.join(nl)

        buff = self._TextLicense
        buff.set_markup(nl)

    def set_about_text(self, text):
        buff = self._TextAbout
        buff.set_text(text)

    def set_about_text_file(self, text_file_path):
        self.set_about_text(open(text_file_path, 'r').read())
        self._about_file = text_file_path

    def set_about_markdown_file(self, markdown_file_path):
        m = markup.markdown_file(markdown_file_path)
        self._TextAbout.set_markup(m)
        self._about_file = markdown_file_path

    def set_home_page(self, url):
        self._home_page = url

    def set_report_page(self, url):
        if url == None:
            self._ReportButton.hide()

        else:
            self._ReportButton.show()
            self._report_page = url

    def set_appname(self, name):
        markup = "<b>" + name + "</b>"
        self._Name.set_markup(markup)

    def set_shortdescrpition(self, text):
        markup = "<i>" + text + "</i>"
        self._ShortDescrpition.set_markup(markup)

    def get_shortdescrpition(self):
        return self._ShortDescrpition.get_text()

    def get_logo(self):
        return self._Logo

    def open_link(self, url):
        webbrowser.open_new_tab(url)

    def on_report(self, button):
        self.open_link(self._report_page)

    def on_home(self, button):
        self.open_link(self._home_page)

if __name__ == '__main__':
    #example of use
    ad = AboutDialog(
                    app_name = "Grabbo About Dialog",
                    short_des = "Python Gtk 3 Widget Framework",
                    report_page = "https://github.com/jeremi360/Grabbo/issues",
                    home_page = "https://github.com/jeremi360/Grabbo"
                    )

    ad.set_version("0.3")

    license_path = os.path.join(os.path.dirname(__file__), '..', "LICENSE")
    about_path = os.path.join(os.path.dirname(__file__), '..', "README.md")

    ad.set_license_file(license_path)
    oneline = "one line to give the program's name and a brief idea of what it does."
    ad.set_license_keywords({
                            "project":"Grabbo", "year":"2016",
                            "fullname":"Jeremi Biernacki",
                            "name of author":"Jeremi Biernacki",
                            oneline:ad.get_shortdescrpition()
                            })

    ad.set_about_markdown_file(about_path)

    ad.show_all() #show() - don't works :(
    Gtk.main()
