#-------------------------------------------------------------------------------
# Name:        retrieveIpScript
# Purpose:     Send an email using SMTP
#
# Author:      RedSpiderMkV
#
# Created:     19/10/2015
# Copyright:   (c) RedSpiderMkV 2016
# Licence:     ..
#-------------------------------------------------------------------------------

from Mailer.SendMail import SendMail
from Mailer.SmtpProviders import SmtpProviders
from IpTracker.IpRetriever import IpRetriever
from IpTracker.IpFileHandler import IpFileHandler
from IpTracker.IpComparator import IpComparator

userName = "test"
password = "password"
recipient = "recpt"
provider = SmtpProviders.OUTLOOK

def main():
    ipRetriever = IpRetriever()
    fileHandler = IpFileHandler()

    fileHandler.SaveIpInfo('192.168.2.2')    
    
    ipComparator = IpComparator(fileHandler, ipRetriever)
    if ipComparator.IsIpAddressDifferent():
        print 'IP address is different'
        fileHandler.SaveIpInfo(ipComparator.GetNewIpAddress())

        mailer = SendMail(userName, password, recipient, provider)
        mailer.Send(ipComparator.GetNewIpAddress())        
    else:
        print 'No change in IP address'

if __name__ == "__main__":
    main()
