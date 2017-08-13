PyGtkFX
======

Small lib to make Gtk my way.
Inspired by Granite from elementary OS.
I use it in my [PyFox project][3]

If you want use this your python apps will need:

- [python version 3.x][1]
- Gtk and Webkit from gi repository:
   - Linux - check your dist repos
   - [Windows][2] - download "pygi-aio-*version*-setup.exe"

- partial markdown to markup converter use [markdown2][4]:
`pip install markdown2`

Done:

* IntEntry - Entry specially for int

  ![IntEntry screen shot][5]

* BigLabelButton - Button with big label

* AboutDialog:

  ![AboutDialog screen shot][6]

  * partial support for markdown files as about files
  * partial markdown to markup converter
  * smart license file loader
  * support for license file keywords
* some small fixes to Window and Builder

ToDo:

* Complete markdown to markup converter

[1]:https://www.python.org
[2]:https://sourceforge.net/projects/pygobjectwin32/files/
[3]:https://github.com/jeremi360/PyGtkFX
[4]:https://github.com/trentm/python-markdown2
[5]:shots/IntEntry.png
[6]:shots/AboutDialog.png
