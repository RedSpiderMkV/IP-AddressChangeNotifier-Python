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

from IpTracker.IpRetriever import IpRetriever
from IpTracker.IpFileHandler import IpFileHandler
from IpTracker.IpComparator import IpComparator
from IpUpdateRunner import IpUpdateRunner

userName = "sender"
password = "password"
recipient = "recipient"

def main():    
    try:
        fileHandler = IpFileHandler()
        ipRetriever = IpRetriever()
        ipComparator = IpComparator(fileHandler, ipRetriever)
        
        updateRunner = IpUpdateRunner(fileHandler, ipComparator)
        updateRunner.PerformIpCheckAndUpdate(userName, password, recipient)
    except:
        print 'Error in IP update'

if __name__ == "__main__":
    main()
