from MaltegoTransform import *
import requests
import re

baseurl = "http://www.ipvoid.com/ip-blacklist-check/"
ip = sys.argv[1]

params ={'ip': ip}
response = requests.post(baseurl, data=params)
response=response.text
response = response.encode('utf_8')
match = re.findall(r"<span class=\"label label-[a-z]+\">BLACKLISTED ([0-9]+/[0-9]+)</span>",response,re.M)
score = ','.join(match)

mt = MaltegoTransform()
me = mt.addEntity("maltego.Phrase", score)
me.setLinkLabel("IPVoid")

mt.returnOutput()


