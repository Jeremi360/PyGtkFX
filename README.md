Grabbo
======

Small lib to make Gtk my way.
I use it in my [cRoWBaR project][3]

If you want use this your python apps will need:

- [python version 3.x][1]
- Gtk and Webkit from gi repository:
   - Linux check your dist repos
   - [Windows][2] - download "pygi-aio-*version*-setup.exe"

- partial markdown to markup converter use [markdown2][4]:
`pip install markdown2`

Done:

* AboutDialog:
  * partial support for markdown files as about files
  * partial markdown to markup converter
  * smart license file loader
  * support for license file keywords
* some small fixes to Window and Builder

ToDo:

* Complete markdown to markup converter

[1]:http://sh.st/nrLQb
[2]:http://sh.st/nrLEb
[3]:https://github.com/jeremi360/cRoWBaR
[4]:https://github.com/trentm/python-markdown2
