#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        IpTracker.py
# Purpose:     Retrieves external IP Address using a number of different sources
#              in case one of them is down.
#
# Author:      RedSpiderMkV
#
# Created:     Mon Jun  6 21:37:27 2016
# Copyright:   (c) RedSpiderMkV 2016
#-------------------------------------------------------------------------------

import urllib2

class IpRetriever:
    __urls = []
    
    def __init__(self):
        with open('IpRetrievalUrlList.txt') as f:
            for line in f:
                self.__urls.append(line)
        
    def GetIpAddress(self):
        for i in range(0, len(self.__urls) - 1):
            try:
                request = urllib2.urlopen(self.__urls[1])
                ip = request.read().rstrip('\n')
            
                return ip
            except:
                print 'Error retrieving Ip from url: ' + self.__urls[i]
            finally:
                request.close()

ipRetriever = IpRetriever()
print ipRetriever.GetIpAddress()