import markdown2, os

_tab = "\t"

def _start(tag):
    return "<" + tag + ">"

def _end(tag):
    return "</" + tag + ">"

def markdown(markdown_string):
    html = markdown2.markdown(markdown_string)
    rmarkup = _md_convert(html)
    return rmarkup

def _replace_tag(string, old, new):
    string = string.replace(
                            _start(old),
                            _start(new)
                            )
    string = string.replace(
                            _end(old),
                            _end(new)
                            )
    return string

def _list_replace_tag(string, old, newlist):

    nstart = []
    nend = []

    for n in newlist:
        s = _start(n)
        nstart.append(s)

    for n in newlist[::-1]:
        n = _end(n)
        nend.append(n)

    nstart = "".join(nstart)
    nend = "".join(nend)

    string = string.replace(
                            _start(old),
                            nstart
                            )
    string = string.replace(
                            _end(old),
                            nend
                            )
    return string

def _remove_tag(string, tag):
    string = string.replace(
                            _start(tag),""
                            )
    string = string.replace(
                            _end(tag),""
                            )
    return string

def _smart_tag_replace(string, old, new):
    string = string.replace(
                            _start(old),
                            new
                            )
    string = string.replace(
                            _end(old),""
                            )
    return string

def _add_to_tag(string, tag, attribute):
    string = string.replace(
                            _start(tag),
                            _start(tag + " " + attribute)
                            )

    return string

def _img_convert(string):
    imgstart = '<img src="'
    newimgstart = '<a href="'
    string = string.replace(imgstart, newimgstart)

    allend = '" />'
    newallend = '</a>'
    string = string.replace(allend, newallend)

    altstart = '" alt="'
    newaltstart = '">'
    string = string.replace(altstart, newaltstart)

    return string

def _md_convert(string):
    string = _replace_tag(string, "h1", "big")
    string = _replace_tag(string, "em", "i")

    #code
    string = _list_replace_tag(string, "code", ["tt", "span"])
    string = _add_to_tag(string, "span", "background = 'gray'")

    #string = _smart_tag_replace(string, "p", os.linesep)
    string = _remove_tag(string, "p")

    string = _smart_tag_replace(string, "li", _tab + "<b>- </b>")
    string = _remove_tag(string, "ul")
    string = _replace_tag(string, "strong", "big")
    string = _img_convert(string)#converts imgs to links to this imgs

    return string

def markdown_file(markdown_file_path):
    html = markdown2.markdown_path(markdown_file_path)
    lines = html.splitlines()
    nlines = []

    for l in lines:
        nl = _md_convert(l)
        nlines.append(nl)

    return os.linesep.join(nlines)

def _lic_convert(string):
    s = string
    start = "<"
    end = ">"
    url = s[s.find(start)+len(start):s.rfind(end)]

    string = string.replace('<' + url + '>', '<a href="' + url + '">' + url + '</a>')
    return string

def license_file(license_file_path, key_words = {}):
    lic = open(license_file_path, 'r').read()
    lines = lic.splitlines()
    nlines = []

    for l in lines:
        nl = _lic_convert(l)
        nlines.append(nl)

    return os.linesep.join(nlines)
