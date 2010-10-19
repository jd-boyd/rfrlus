#ar = [chr(i) for i in range(ord('0'), ord('9')+1)] 
#ar += [chr(i) for i in range(ord('a'), ord('z')+1)]
#ar += [chr(i) for i in range(ord('A'), ord('Z')+1)] 

ar = ['d', '6', 'e', 'H', 'p', '8', 'D', 'T', 'U', 'l', 'G', 'K', 'g', 'o', '9', 'i', 'N', 'J', 'z', 'w', '2', 'O', 'C', 'k', 'y', '7', 'f', 'a', '1', 'Q', 'A', 'M', '0', 'Y', '5', '3', 'V', 'h', 'r', 'Z', 'c', 'W', 't', 'I', 'x', 'L', 'B', '4', 'j', 'm', 'n', 'S', 'E', 'u', 'R', 'b', 'X', 'F', 's', 'q', 'P', 'v']

rar = dict([(k, i) for i, k in enumerate(ar)])

#ar.append('-')

def encodeV(v):
    l = len(ar)
    res = []
    while v:
        t = v % l
        res.append(ar[t])
        v -= t
        v /= l
    res.reverse()
    return "".join(res)

def decodeV(v):
    l = len(ar)
    t = 0
    for i in range(len(v)):
        t *= l
        t += rar[v[i]]
    return t

if __name__=="__main__":
    z = 2546
    print "start", z
    t = encodeV(z)
    print repr(t)
    print repr(decodeV(t))
    
    
    z = 10000000
    print "start", z
    t = encodeV(z)
    print repr(t)
    print repr(decodeV(t))
    
    for i in range(10000000):
        if not i%10000:
            print "itr", i

        t = encodeV(i)

        if not i==decodeV(t):
            print "FAIL", t, i
