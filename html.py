class HDocIter:
    def __init__(self, a=[]):
        self.all=a
    def __iter__(self):
        return iter(self.all)

class HDoc:
    def __init__(self):
        self.head = []
        self.body = []
    def addHead(self, str):
        self.head += [str + "\n"]
    def addScript(self, fileName):
        self.addHead('<script type="text/javascript" src="%s"></script>' % fileName)
    def add(self, str):
        self.body += [str + "\n"]
    def outputHead(self):
        ret = "".join(self.head)
        return head(ret)
    def outputBody(self):
        ret = "".join(self.body)
        return body(ret)
    def output(self):
        ret = self.outputHead()
        ret += self.outputBody()
        return "".join(html(ret))
    def __iter__(self):
        return HDocIter([htmlOpen, headOpen] + self.head + [headClose, "<body>"] + self.body + ["</body>", htmlClose])

    def addBr():
        self.add(br())

def tag(t):
    return lambda(b): "<"+t+">"+b+"</"+t+">"

htmlOpen = """<!DOCTYPE html>""" + '<html>'
htmlClose = "</html>"

def html(b):
    return [htmlOpen, b, htmlClose]

title = tag('title')

headOpen = '<head><meta http-equiv="Content-Type" content="text/html;charset=utf-8" />' 
headClose = "</head>\n"

def head(t):
    return headOpen + t + headClose

def script(t):
    return "<script type='text/javascript'>\n" + t + "\n</script>\n"

def body(b):
    return "<body>" + b + "</body>"

def li(l):
    return "<li>" + l + "</li>\n"

def p(b):
    return "<p>" + b + "</p>"

def br():
    return "<br />\n"

def hr():
    return "<hr />\n"

def h1(entry):
    return "<h1>" + entry + "</h1>"

def h2(entry):
    return "<h2>" + entry + "</h2>"

def table(entry):
    return "<table>" + entry + "</table>\n"

def tr(entry):
    return "<tr>" + entry + "</tr>\n"

def td(entry):
    return "<td>" + entry + "</td>"

def textField(name, value):
    return "<input type='text' name='%s' value='%s' />" % (name, value)

def hiddenField(name, value):
    return "<input type='hidden' name='%s' value='%s' />" % (name, value)

def passwordField(name, value):
    return "<input type='password' name='%s' />" % (name)

def ahref(target, text):
    return "<a href=\"" + target + "\">" + text + "</a>"

def option(val, b, s):
    ret = "<option "
    if s:
        ret += "selected "
    if type(val)==str:
        ret += "value='%s'" % (val)
    else:
        ret += "value='%s'" % (repr(val))
    ret += ">"
    ret += b
    ret += "</option>\n"
    return ret

def title(v):
    return "<title>"+v+"</title>"

