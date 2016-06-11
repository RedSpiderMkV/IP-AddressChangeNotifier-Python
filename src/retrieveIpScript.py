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
    try:
        PerformIpCheckAndUpdate()
    except:
        print 'Error in IP update'
    
def PerformIpCheckAndUpdate():
    ipRetriever = IpRetriever()
    fileHandler = IpFileHandler()

    ipComparator = IpComparator(fileHandler, ipRetriever)
    if ipComparator.IsIpAddressDifferent():
        print 'IP address is different'

        provider = SmtpProviderFactory.GetProvider(userName)
        
        if provider == None:
            print 'Error getting email provider'
            return

        mailer = SendMail(userName, password, recipient, provider)
        subject = 'IP Address Changed'
        message = 'New IP: ' + ipComparator.GetNewIpAddress()
        
        mailer.Send(subject, message)
        
        fileHandler.SaveIpInfo(ipComparator.GetNewIpAddress())
    else:
        print 'No change in IP address'

if __name__ == "__main__":
    main()
