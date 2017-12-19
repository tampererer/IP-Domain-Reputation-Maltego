from MaltegoTransform import *
import requests
import re

domain = sys.argv[1]

response = requests.get('https://www.mcafee.com/threat-intelligence/domain/default.aspx?domain=' + domain)
response = response.text
response = response.encode('utf_8')
match = re.findall(r"<img id=\"[0-9a-zA-Z_]+\" title=\"([A-Za-z _]+)\" class=\"[a-zA-Z ]+\" src=\"/img/banners/threat/risk-meters/[a-z-]+\.png\" .+ />",response,re.M)
risk = ','.join(match)

mt = MaltegoTransform()
me = mt.addEntity("maltego.Phrase", risk)
me.setLinkLabel("McAfee")

mt.returnOutput()

