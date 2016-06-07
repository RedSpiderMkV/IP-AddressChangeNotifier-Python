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
    """ IP file handler - handles the reading and writing of the IP address
        to a text file.  When writing to file, also adds a timestamp. """

    """ DateTime format used in date/string conversion. """
    DateTimeFormat = '%d/%m/%Y %H:%M:%S'

    _fileName = ''
    
    _INDEX_IP = 0
    _INDEX_DATE = 1

    def __init__(self):
        """ Initialise file handler with IP address text file. """
        
        location = os.path.realpath(
            os.path.join(os.getcwd(),os.path.dirname(__file__)))
            
        self._fileName = os.path.join(location, 'CurrentIpInfo.txt')
    
    def GetIpAddressFromFile(self):
        """ Get the IP address currently stored in file as a string.
        
            Returns:
                IP address as string. """
                
        return self._getIpInfoFromFile(self._INDEX_IP).rstrip('\n')
    
    def GetIpUpdateDateFromFile(self):
        """ Get the time stamp of when IP address was saved.
        
            Returns:
                IP address saved timestamp as datetime. """
                
        dateTimeStr = self._getIpInfoFromFile(self._INDEX_DATE).rstrip('\n')
        timestamp = time.strptime(dateTimeStr, self.DateTimeFormat)
        
        return timestamp

    def SaveIpInfo(self, ipAddress):
        """ Save the provided IP address along with a timestamp.
        
            Arguments:
                ipAddress: IP address as string. """
                
        timestamp = time.strftime(self.DateTimeFormat)
        with open(self._fileName, 'w') as f:
            f.write(ipAddress)
            f.write('\n')
            f.write(timestamp)
    
    def _getIpInfoFromFile(self, infoIndex):
        """ Get IP info from file.  IP info stored in separate lines.  Index
            specifies which bit of info required.
            
            Arguments:
                infoIndex: Index of info required.
                           _INDEX_IP - get IP address.
                           _INDEX_DATE - get timestamp.
            
            Returns:
                IP Info, either IP address or datetime as a string. """
                
        with open(self._fileName) as f:
            lines = f.readlines()
        
            return lines[infoIndex]
