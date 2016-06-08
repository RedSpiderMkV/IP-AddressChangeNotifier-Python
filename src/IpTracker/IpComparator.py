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
    def __init__(self, fileHandler, ipRetriever):
        self._fileHandler = fileHandler
        self._ipRetriever = ipRetriever
        
    def IsIpAddressDifferent(self):
        self.SavedIp = self._fileHandler.GetIpAddressFromFile()
        self.RetrievedIpAddress = self._ipRetriever.GetIpAddress()

        return self.SavedIp != self.RetrievedIpAddress