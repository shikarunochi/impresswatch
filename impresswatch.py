
import urllib.request
import xml.etree.ElementTree as ET
import datetime
from datetime import datetime
import ssl
import io,sys

ssl._create_default_https_context = ssl._create_unverified_context
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

MAX_CONTENT = 5

siteList = [
			{"siteName":"クラウドWatch", "url":"https://cloud.watch.impress.co.jp/data/rss/1.0/clw/feed.rdf","color":"#9fd9f6", "id":"clw"},
			{"siteName":"PC Watch", "url":"https://pc.watch.impress.co.jp/data/rss/1.0/pcw/feed.rdf","color":"#36f", "id":"pcw"},
			{"siteName":"デジカメWatch", "url":"https://dc.watch.impress.co.jp/data/rss/1.0/dcw/feed.rdf","color":"#2e6162", "id":"dcw"},
			{"siteName":"AKIBA PC Hotline!", "url":"https://akiba-pc.watch.impress.co.jp/data/rss/1.0/ah/feed.rdf","color":"#ffa824", "id":"ah"},
			{"siteName":"AV Watch", "url":"https://av.watch.impress.co.jp/data/rss/1.0/avw/feed.rdf","color":"#5e5858", "id":"avw"},
			{"siteName":"GAME Watch", "url":"https://game.watch.impress.co.jp/data/rss/1.0/gmw/feed.rdf","color":"#0c6", "id":"gmw"},
			{"siteName":"ケータイWatch", "url":"https://k-tai.watch.impress.co.jp/data/rss/1.0/ktw/feed.rdf","color":"#ffacb7", "id":"ktw"},
			{"siteName":"INTERNET Watch", "url":"https://internet.watch.impress.co.jp/data/rss/1.0/iw/feed.rdf","color":"#ffde00", "id":"iw"},
			{"siteName":"窓の杜", "url":"https://forest.watch.impress.co.jp/data/rss/1.0/wf/feed.rdf","color":"#390", "id":"wf"},
			{"siteName":"家電 Watch", "url":"https://kaden.watch.impress.co.jp/data/rss/1.0/kdw/feed.rdf","color":"#42b6ff", "id":"kdw"},
			{"siteName":"仮想通貨 Watch", "url":"https://crypto.watch.impress.co.jp/data/rss/1.0/ctw/feed.rdf","color":"#ffb400", "id":"ctw"}
			]

print ("<!DOCTYPE HTML><html lang='ja'>")
print ("<html><head><meta charset='UTF-8'/>")
print ("<style type='text/css'>")
print ("ul, ol { padding: 0; }")
print ("ul li, ol li {");
print ("  border-left: solid 6px #4169e1;background: #f0f8ff;")
print ("  margin-bottom: 3px;line-height: 1.5;padding: 0.5em;")
print ("  list-style-type: none!important;")
print ("}")
print ("</style>")
print ("<body>")
now = datetime.now()

print ("<div>取得時刻 [" + '{0:%Y/%m/%d %H:%M:%S}'.format(now) + "]</div>")

for site in siteList:

	url = site["url"]
	domain = url[:url.find('data')]
	siteName = site["siteName"]
	siteColor =  site["color"]
	id  =  site["id"]
	req = urllib.request.Request(url)

	with urllib.request.urlopen(req) as response:
		XmlData = response.read()
		
	root = ET.fromstring(XmlData)

	count = 0
	for child in root:
		count = count + 1
		if count == 1:
			print("<div style='background-color:" + siteColor + ";'>" + siteName + "</div>")
			print("<ul>")
		elif count > 1 and count <= MAX_CONTENT + 1:
			title = child[0].text
			link = child[1].text
			dateText = child[2].text
			dateStr = dateText[0:10] + " " + dateText[11:19]
			linkId = link[-12:]
			#urlの data より前 + ID + 上4桁 + "/" + 下3桁 + list.jpg"
			imageSrc = domain + "img/" + id + "/list/" + linkId[0:4] + "/" + linkId[4:7] + "/list.jpg"
			
			if dateStr != None:
				print("<li>")
				print("<image src='" + imageSrc + "' width=240 onerror=\"this.style.display='none'\" style='float:left' />")
				print("<a href='" + link + "'>" + title + "</a><br/>" + " (" + dateStr + ")<div style='clear:both'/></li>" )
				
		else:
			break
	print("</ul>")

print ("<hr/><p>Twitter:<a href='https://twitter.com/shikarunochi'>@shikarunochi</a></p>")
print ("</body></html>")