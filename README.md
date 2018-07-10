# [IP-Domain-Reputation] Maltego Local Transforms
Maltego Local Transforms to use the following services.  
McAfee Threat Library - https://www.mcafee.com/content/enterprise/en-us/threat-center.html  
URLVoid - http://www.urlvoid.com/  
IPVoid - http://www.ipvoid.com/  

# Prerequisites
- Python 2.7.x + requests, re module
- Python 3.6.x will probably work.

# Setup
- Put mcafee.py, ipvoid.py, urlvoid.py and MaltegoTransform.py into your working directory. (e.g. C:\Maltego\Transforms\Reputation)
- Open Reputation.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  
  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\Reputation

# Transforms
McAfee
- domain_risk
- ip_risk

URLVoid
- domain_blacklisted

IPVoid
- ip_blacklisted
