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
    __urls = [r'http://www.portvisibility.co.uk/visibility/tools/myip.php',
              r'http://icanhazip.com/',
              r'http://ipinfo.io/ip',
              r'https://www.trackip.net/ip',
              r'https://wtfismyip.com/text']
        
    def GetIpAddress(self):
        for i in range(0, len(self.__urls) - 1):
            try:
                request = urllib2.urlopen(self.__urls[1])
                ip = request.read().rstrip('\n')
            
                return ip
            except:
                print 'Error retrieving Ip from url: ' + self.__urls[i]

ipRetriever = IpRetriever()
print ipRetriever.GetIpAddress()