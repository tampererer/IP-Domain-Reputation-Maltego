from MaltegoTransform import *
import requests
import re

baseurl = "http://www.urlvoid.com/scan/"
domain = sys.argv[1]

response = requests.get(baseurl + domain)
response=response.text
response = response.encode('utf_8')
match = re.findall(r"<span class=\"label label-[a-z]+\">([0-9]+/[0-9]+)</span>",response,re.M)
score = ','.join(match)

mt = MaltegoTransform()
me = mt.addEntity("maltego.Phrase", score)
me.setLinkLabel("URLVoid")

mt.returnOutput()

