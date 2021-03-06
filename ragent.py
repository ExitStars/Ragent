#!/usr/bin/env python
#-*-coding:utf-8-*-

# Modüller
from random import randint
from os import system
from sys import argv
from requests import get
from re import findall
from base64 import b64decode

# Sabitler
bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

# User Agent Listeleri
winlist = ['Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8',
    'Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3',
    'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5',
    'Mozilla/5.0 (Windows; Windows NT 6.1; rv:2.0b2) Gecko/20100720 Firefox/4.0b2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b7) Gecko/20101111 Firefox/4.0b7',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8pre) Gecko/20101114 Firefox/4.0b8pre',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2',
    'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2',
    'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14',
    'Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b4pre) Gecko/20090311 Shiretoko/3.1b4pre']

linlist = ['Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12',
    'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5',
    'Mozilla/5.0 (X11; Linux x86_64; rv:2.0b4) Gecko/20100818 Firefox/4.0b4',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100308 Ubuntu/10.04 (lucid) Firefox/3.6 GTB7.1',
    'Mozilla/5.0 (X11; Linux x86_64; rv:2.0b9pre) Gecko/20110111 Firefox/4.0b9pre',
    'Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)',
    'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:12.0) Gecko/20100101 Firefox/12.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0',
    'Mozilla/5.0 (X11; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.10 Chromium/16.0.912.21 Chrome/16.0.912.21 Safari/535.7',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.04 Chromium/15.0.871.0 Chrome/15.0.871.0 Safari/535.2',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/10.04 Chromium/14.0.813.0 Chrome/14.0.813.0 Safari/535.1',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3pre) Gecko/20090109 Shiretoko/3.1b3pre']

maclist = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19']

andlist = ['Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0',
    'Mozilla/5.0 (Android; Mobile; rv:12.0) Gecko/12.0 Firefox/12.0',
    'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
    'Mozilla/5.0 (Android; Mobile; rv:28.0) Gecko/28.0 Firefox/28.0',
    'Mozilla/5.0 (Android; Tablet; rv:29.0) Gecko/29.0 Firefox/29.0']

moblist = ['Mozilla/5.0 (Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
    'Mozilla/5.0 (Mobile; rv:17.0) Gecko/17.0 Firefox/17.0',
    'Mozilla/5.0 (Tablet; rv:18.1) Gecko/18.1 Firefox/18.1']

tablist = ['Mozilla/5.0 (Tablet; rv:18.1) Gecko/18.1 Firefox/18.1']

# Taslaklar
ualist = {"mac": maclist, "win": winlist, "lin": linlist, "and": andlist, "mob": moblist, "tab": tablist}
stage = ["mac", "win", "lin", "and", "mob", "tab"]
proxyliste = []
update = 0

# Fonksiyonlar
def logo():
    system("clear")
    print "--==["+bold+blue+"nickname"+endcolor+"] [ ExitStars"
    print "--==["+bold+yellow+"MyGitHub"+endcolor+"] [ http://github.com/ExitStars"
    print "--==["+bold+green+"software"+endcolor+"] [ http://github.com/ExitStars/Ragent V3"
    print "-"*54

def help():
    logo()
    print bold+yellow+"Ragent Nedir?"+endcolor
    print "Ragent, user-agent bilgisi ve proxy adresi oluşturan bir modüldür."
    print "İlgili fonksiyonu çağırarak bilgilere ulaşabilirsiniz."
    print "Toplam {} user-agent. ".format(len(winlist)+len(linlist)+len(maclist)+len(tablist)+len(andlist)+len(moblist))
    print "∟ {} Windows, {} Linux, {} Mac, {} Android, {} Mobil, {} Tablet.".format(len(winlist), len(linlist), len(maclist), len(andlist), len(moblist), len(tablist))
    print ""
    print bold+green+"~ UA Ortamları"+endcolor
    print "win (Windows), lin (Linux), mac (Macintosh)"
    print "and (Android), mob (Mobil), tab (Tablet)"
    print ""
    print bold+yellow+"Kullanım Rehberi"+endcolor
    print bold+green+"~ User-Agent Ataması"+endcolor
    print blue+"ua()"+endcolor+"\t\t\t# Random user-agent bilgisi atar."
    print blue+"ua('xxx')"+endcolor+"\t\t# xxx ortamına ait user-agent bilgisi atar."
    print blue+"ua('xxx', 5)"+endcolor+"\t\t# xxx ortamında ki 5 numaralı user-agent bilgisini atar."
    print blue+"ua('ualist')"+endcolor+"\t\t# Tüm user-agent bilgilerini ekrana basar."
    print blue+"ua('ualist', 'xxx')"+endcolor+"\t# xxx ortamına ait user-agent bilgilerini ekrana basar."
    print ""
    print bold+green+"~ Proxy Ataması"+endcolor
    print blue+"ph('rp')"+endcolor+"\t\t# Random proxy adresi atar."
    print blue+"ph('plist')"+endcolor+"\t\t# Mevcut proxy adreslerini listeler."
    print blue+"ph('p', 5)"+endcolor+"\t\t# 5 numaralı proxy adresini atar."
    print blue+"ph('update')"+endcolor+"\t\t# Proxy listesini günceller."

def ua(islem = None, arg = None):
    if islem == None and arg == None:
        rsayi = randint(0, 5)
        rsis = ualist[stage[rsayi]]
        rua = randint(0,len(rsis)-1)
        return rsis[rua]
    elif islem in stage:
        if arg == None:
            gsis = ualist[islem]
            return gsis[randint(0, len(gsis)-1)]
        else:
            gsis = ualist[islem]
            return gsis[arg]
    elif islem == "ualist":
        if arg == None:
            print bold+green+"<< Windows Listesi >>"+endcolor
            for i in range(0, len(winlist)):
                print bold+green+"ID:"+endcolor+" {}\t{}".format(i, winlist[i])
            print bold+green+"\n\n<< Linux Listesi >>"+endcolor
            for i in range(0, len(linlist)):
                print bold+green+"ID:"+endcolor+" {}\t{}".format(i, linlist[i])
            print bold+green+"\n\n<< Macintosh Listesi >>"+endcolor
            for i in range(0, len(maclist)):
                print bold+green+"ID:"+endcolor+" {}\t{}".format(i, maclist[i])
            print bold+green+"\n\n<< Android Listesi >>"+endcolor
            for i in range(0, len(andlist)):
                print bold+green+"ID:"+endcolor+" {}\t{}".format(i, andlist[i])
            print bold+green+"\n\n<< Mobile Listesi >>"+endcolor
            for i in range(0, len(moblist)):
                print bold+green+"ID:"+endcolor+" {}\t{}".format(i, moblist[i])
            print bold+green+"\n\n<< Tablet Listesi >>"+endcolor
            for i in range(0, len(tablist)):
                print bold+green+"ID:"+endcolor+" {}\t{}".format(i, tablist[i])
        else:
            if arg == "win":
                print bold+green+"<< Windows Listesi >>"+endcolor
                for i in range(0, len(winlist)):
                    print bold+green+"ID:"+endcolor+" {}\t{}".format(i, winlist[i])
            elif arg == "lin":
                print bold+green+"<< Linux Listesi >>"+endcolor
                for i in range(0, len(linlist)):
                    print bold+green+"ID:"+endcolor+" {}\t{}".format(i, linlist[i])
            elif arg == "mac":
                print bold+green+"<< Macintosh Listesi >>"+endcolor
                for i in range(0, len(maclist)):
                    print bold+green+"ID:"+endcolor+" {}\t{}".format(i, maclist[i])
            elif arg == "and":
                print bold+green+"<< Android Listesi >>"+endcolor
                for i in range(0, len(andlist)):
                    print bold+green+"ID:"+endcolor+" {}\t{}".format(i, andlist[i])
            elif arg == "mob":
                print bold+green+"<< Mobile Listesi >>"+endcolor
                for i in range(0, len(moblist)):
                    print bold+green+"ID:"+endcolor+" {}\t{}".format(i, moblist[i])
            elif arg == "tab":
                print bold+green+"<< Tablet Listesi >>"+endcolor
                for i in range(0, len(tablist)):
                    print bold+green+"ID:"+endcolor+" {}\t{}".format(i, tablist[i])
    else:
        print "ragent.py --help, ragent.py -h yada ragent.help()"

def ph(islem = None, arg = None):
    if islem == "rp":
        return proxyliste[randint(0, len(proxyliste)-1)]
    elif islem == "update":
        del proxyliste[:]
        try:
            payload = get("https://proxy-list.org/english/index.php?p=1").text
            payload = payload.encode("utf8")
            aranan = """ <li class="proxy"><script type="text/javascript">(.*?)</script></li>"""
            bulunan = findall(aranan, payload)
            for i in bulunan:
                i = b64decode(i.replace("Proxy('", "").replace("')", ""))
                proxyliste.append(i)
            return 1
        except:
            return 0
    elif islem == "plist":
        return proxyliste
    elif islem == "p" and arg != None:
        return proxyliste[arg]
    else:
        return "Islem Yok"

if len(argv) > 1:
    if argv[1] == "--help" or argv[1] == "-h":
        help()
    else:
        pass
else:
    pass
