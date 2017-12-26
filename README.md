# [McAfee] Maltego Local Transforms
Maltego Local Transforms to use McAfee domain reputation - https://www.mcafee.com/threat-intelligence/domain/

# Prerequisites
- Python 2.7.x + requests, re module

# Setup
- Put domain_to_risk.py and MaltegoTransform.py into your working directory. (e.g. C:\Maltego\Transforms\McAfee)
- Open McAfee.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  
  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\McAfee

# Transforms

Tarnsforms:
- domain_to_risk.py
