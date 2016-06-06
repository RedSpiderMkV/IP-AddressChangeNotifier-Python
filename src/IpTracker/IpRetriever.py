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

import os
import urllib2

class IpRetriever:
    """ IP Retriever class - retrieves external IP address.  Uses a list
        of URLs from an external file to query IP address."""
    
    __urls = []
    
    def __init__(self):
        """ Initialise retriever with list of URLs which can be checked """        

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(),os.path.dirname(__file__)))        
        
        with open(os.path.join(__location__, 'IpRetrievalUrlList.txt')) as f:
            for line in f:
                self.__urls.append(line)
        
    def GetIpAddress(self):
        """ Get IP address - return the value retrieved from the first URL
            where the query succeeds. """
            
        for i in range(0, len(self.__urls) - 1):
            try:
                request = urllib2.urlopen(self.__urls[1])
                ip = request.read().rstrip('\n')
            
                return ip
            except:
                print 'Error retrieving Ip from url: ' + self.__urls[i]
            finally:
                request.close()
                