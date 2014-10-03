import grabbo, os
from gi.repository import Gtk

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

AD_UI = os.path.join(r, 'ui', 'AboutDialog.xml')


class AboutDialog(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)
        
        self.ui =  grabbo.Builder(self, AD_UI).ui
        
        self._HomeButton = self.ui.get_object("HomeButton")
        self._LicenseButton = self.ui.get_object("LicenseButton")
        self._AboutButton = self.ui.get_object("AboutButton")
        self._RapportButton = self.ui.get_object("RapportButton")
        self.Logo = self.ui.get_object("Logo")
        self._TextView = self.ui.get_object("Text")
        self._ShortDescrpition = self.ui.get_object("ShortDescrpition")
        self._Name = self.ui.get_object("Name")
        
        self._InfoBox = self.ui.get_object("InfoBox")
        self._HeaderBox = self.ui.get_object("HeaderBox")
        
        self._HeaderBar = Gtk.HeaderBar()
        self._HeaderBar.set_title(self._HeaderBox)
        
        self.set_titlebar(self._HeaderBar)
        self.add(self._InfoBox)
        
    
        
        

        
        
        
        
        