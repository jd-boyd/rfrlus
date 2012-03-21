import re

r = re.compile(r"%[0-9A-Fa-f][0-9a-fA-F]")

def hexToInt(hexString):
    return int(hexString,16)

def intToChar(i):
    return '%c' % (i)

def deHTTP(s):
    """Removes %xx codes and replaces them with proper ascii"""
    ret = ""
    lastChar = 0
    s=s.replace('+', ' ')
    fi = r.finditer(s)
    for f in fi:
        ret += s[lastChar:f.span()[0]]
        ret += intToChar(hexToInt(s[f.span()[0]+1:f.span()[1]]))
        lastChar=f.span()[1]
    ret += s[lastChar:]
    return ret

