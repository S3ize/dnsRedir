#!/usr/bin/env python

from dnsRedir import *

def testBits() :
    for n in xrange(256) :
        a,b,c,d = getBits(n, 1,2,2,3)
        n2 = putBits((1,2,2,3), a,b,c,d)
        if n != n2 :
            print n, n2, a,b,c,d

def testParse(buf) :
    m = DNSMsg(buf)
    s1 = str(m)
    print m

    b = m.put()
    print 'encoded:', b.encode('hex')
    m2 = DNSMsg(b)
    s2 = str(m2)
    print 'decoded:', m2
    print 'same?', s1 == s2
    #for n,(x1,x2) in enumerate(zip(s1, s2)) :
    #    print n, x1, x2, x1 == x2
    return

def testParses() :
    print 'simple query'
    buf = '\x85%\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x03foo\x03bar\x00\x00\x01\x00\x01'
    testParse(buf)

    print
    print 'complex response'
    buf = '''da12 8180
     0001 0008 0000 000a 0874 6865 6e65 7773
     6803 636f 6d00 00ff 0001 c00c 0001 0001
     0001 386a 0004 48eb c992 c00c 0002 0001
     0001 50e7 000c 036e 7333 0268 6503 6e65
     7400 c00c 0002 0001 0001 50e7 0006 036e
     7332 c03e c00c 0002 0001 0001 50e7 0006
     036e 7331 c03e c00c 0002 0001 0001 50e7
     0006 036e 7334 c03e c00c 0002 0001 0001
     50e7 0006 036e 7335 c03e c00c 0006 0001
     0001 50e7 0023 c064 0a68 6f73 746d 6173
     7465 72c0 3e77 fc96 1900 002a 3000 0007
     0800 093a 8000 0151 80c0 0c00 0f00 0100
     0150 e700 2700 0102 6d78 0874 6865 6e65
     7773 6803 636f 6d04 6375 7374 0162 0b68
     6f73 7465 6465 6d61 696c c015 c03a 0001
     0001 0000 8abf 0004 d8da 8402 c03a 001c
     0001 0000 167a 0010 2001 0470 0300 0000
     0000 0000 0000 0002 c052 0001 0001 0000
     1178 0004 d8da 8302 c052 001c 0001 0000
     1677 0010 2001 0470 0200 0000 0000 0000
     0000 0002 c064 0001 0001 0000 1a98 0004
     d8da 8202 c076 0001 0001 0000 1677 0004
     d842 0102 c076 001c 0001 0000 d5c1 0010
     2001 0470 0400 0000 0000 0000 0000 0002
     c088 0001 0001 0000 be49 0004 d842 5012
     c088 001c 0001 0000 d5c1 0010 2001 0470
     0500 0000 0000 0000 0000 0002 c0cb 0001
     0001 0000 0d77 0004 4062 2404'''.replace('\n','').replace(' ','').decode('hex')
    testParse(buf)

    print
    print 'ipv6 response'
    buf = '\x00\x01\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x1c\x00\x01\xc0\x0c\x00\x1c\x00\x01\x00\x00\x00\xc1\x00\x10 \x01H`@\x07\x08\x01\x00\x00\x00\x00\x00\x00\x10\x13'
    testParse(buf)

if __name__ == '__main__' :
    testBits()
    testParses()
