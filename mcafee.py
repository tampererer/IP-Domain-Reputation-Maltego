# -*- coding: utf-8 -*-
from MaltegoTransform import *
import requests
import re

baseurl = "https://www.mcafee.com/enterprise/en-us/"

# domain_risk
def domain_risk():
    try:
        response = requests.get(baseurl + 'threat-intelligence.domaintc.html?vid=' + data)
        response = response.text
        response = response.encode('utf_8')

        if 'ctl00' in response:
            match = re.findall(r"<img id=\"[0-9a-zA-Z_]+\" title=\"([A-Za-z _]+)\" class=\"[a-zA-Z ]+\" src=\"[a-z-/\.]+\" .+>",response,re.M)
            risk = ','.join(match)
            me = mt.addEntity("maltego.Phrase", '%s' % risk + ' Risk')
            me.setLinkLabel("McAfee")
        if 'Web Category:' in response:
            match = re.findall(r"Web Category:\r\n[ ]+(.+)\r\n",response,re.M)
            category = ','.join(match)
            me = mt.addEntity("maltego.Phrase", '%s' % category)
            me.setLinkLabel("McAfee")

    except:
        pass

    return mt

# ip_risk
def ip_risk():
    try:
        response = requests.get(baseurl + 'threat-intelligence.iptc.html?vid=' + data)
        response = response.text
        response = response.encode('utf_8')

        if 'ctl00_breadcrumbContent_imgRisk\" src=\"/enterprise/' in response:
            match = re.findall(r"<img id=\"ctl00_breadcrumbContent_imgRisk\" src=\"[a-z-/]+/([a-zA-Z]+)\.png\"",response,re.M)
            risk = ','.join(match)
            me = mt.addEntity("maltego.Phrase", '%s' % 'Web:' + risk + ' Risk')
            me.setLinkLabel("McAfee")
        if 'ctl00_breadcrumbContent_imgRisk1\" src=\"/enterprise/' in response:
            match = re.findall(r"<img id=\"ctl00_breadcrumbContent_imgRisk1\" src=\"[a-z-/]+/([a-zA-Z]+)\.png\"",response,re.M)
            risk = ','.join(match)
            me = mt.addEntity("maltego.Phrase", '%s' % 'Email:' + risk + ' Risk')
            me.setLinkLabel("McAfee")
        if 'ctl00_breadcrumbContent_imgRisk2\" src=\"/enterprise/' in response:
            match = re.findall(r"<img id=\"ctl00_breadcrumbContent_imgRisk2\" src=\"[a-z-/]+/([a-zA-Z]+)\.png\"",response,re.M)
            risk = ','.join(match)
            me = mt.addEntity("maltego.Phrase", '%s' % 'Network:' + risk + ' Risk')
            me.setLinkLabel("McAfee")

    except:
        pass

    return mt

# 

# 

# 

# main
func = sys.argv[1]
data = sys.argv[2]

mt = MaltegoTransform()
mresult = eval(func)()
mresult.returnOutput()


