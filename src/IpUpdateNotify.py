#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        IpUpdateNotify.py
# Purpose:     Check, update and notify of any IP address changes.
#
# Author:      RedSpiderMkV
#
# Created:     19/10/2015
# Copyright:   (c) RedSpiderMkV 2016
# Licence:     ..
#-------------------------------------------------------------------------------

import sys
from IpTracker.IpRetriever import IpRetriever
from IpTracker.IpFileHandler import IpFileHandler
from IpTracker.IpComparator import IpComparator
from IpUpdateRunner import IpUpdateRunner

def main():
    try:
        userName = sys.argv[1]
        password = sys.argv[2]
        recipient = sys.argv[3]
        
        fileHandler = IpFileHandler()
        
        if len(sys.argv) > 4 and sys.argv[4] == '-force':
            fileHandler.SaveIpInfo('NoIP')
        
        ipRetriever = IpRetriever()
        ipComparator = IpComparator(fileHandler, ipRetriever)
        
        updateRunner = IpUpdateRunner(fileHandler, ipComparator)
        updateRunner.PerformIpCheckAndUpdate(userName, password, recipient)
    except Exception, e:
        print 'Error in IP update'
        print e

if __name__ == "__main__":
    main()
