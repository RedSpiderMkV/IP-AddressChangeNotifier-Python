#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        IpFileHandler.py
# Purpose:     Reads curren IP address stored in file and writes new IP address
#              to file with a date stamp.
#
# Author:      RedSpiderMkV
#
# Created:     Tue Jun  7 22:16:28 2016
# Copyright:   (c) RedSpiderMkV 2016
#-------------------------------------------------------------------------------

import os
import time

class IpFileHandler:
    _fileName = ''
    
    _INDEX_IP = 0
    _INDEX_DATE = 1

    def __init__(self):
        location = os.path.realpath(
            os.path.join(os.getcwd(),os.path.dirname(__file__)))
            
        self._fileName = os.path.join(location, 'CurrentIpInfo.txt')
    
    def GetIpAddressFromFile(self):
        return self._getIpInfoFromFile(self._INDEX_IP).rstrip('\n')
    
    def GetIpUpdateDateFromFile(self):
        return self._getIpInfoFromFile(self._INDEX_DATE).rstrip('\n')

    def SaveIpInfo(self, ipAddress):
        timestamp = time.strftime('%d/%m/%Y %H:%M:%S')
        with open(self._fileName, 'w') as f:
            f.write(ipAddress)
            f.write('\n')
            f.write(timestamp)
    
    def _getIpInfoFromFile(self, infoIndex):
        with open(self._fileName) as f:
            lines = f.readlines()
        
            return lines[infoIndex]
