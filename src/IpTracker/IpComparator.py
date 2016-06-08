#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     Wed Jun  8 22:55:49 2016
# Copyright:   (c) RedSpiderMkV 2016
#-------------------------------------------------------------------------------

class IpComparator:
    _retrievedIpAddress = ''
    _savedIpAddress = ''
    
    def __init__(self, fileHandler, ipRetriever):
        self._savedIpAddress = fileHandler.GetIpAddressFromFile()
        self._retrievedIpAddress = ipRetriever.GetIpAddress()
        
    def IsIpAddressDifferent(self):
        return self._savedIpAddress != self._retrievedIpAddress
        
    def GetNewIpAddress(self):
        return self._retrievedIpAddress
        
    def GetExistingIpAddress(self):
        return self._savedIpAddress