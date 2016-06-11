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
from Mailer.SmtpProviderFactory import SmtpProviderFactory
from IpTracker.IpRetriever import IpRetriever
from IpTracker.IpFileHandler import IpFileHandler
from IpTracker.IpComparator import IpComparator

userName = "sender"
password = "password"
recipient = "recipient"

def main():
    ipRetriever = IpRetriever()
    fileHandler = IpFileHandler()

    fileHandler.SaveIpInfo('192.168.2.2')    
    
    ipComparator = IpComparator(fileHandler, ipRetriever)
    if ipComparator.IsIpAddressDifferent():
        print 'IP address is different'
        fileHandler.SaveIpInfo(ipComparator.GetNewIpAddress())

        provider = SmtpProviderFactory.GetProvider(userName)
        
        if provider == None:
            print 'Error getting email provider'
            return

        mailer = SendMail(userName, password, recipient, provider)
        mailer.Send(ipComparator.GetNewIpAddress())        
    else:
        print 'No change in IP address'

if __name__ == "__main__":
    main()
