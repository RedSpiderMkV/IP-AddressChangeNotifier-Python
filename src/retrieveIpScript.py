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

gmailUserName = "someone@gmail.com"
gmailPassword = "password"
recipient = "recipient@somewhere.com"
provider = SmtpProviders.OUTLOOK

def main():
    ipRetriever = IpRetriever()
    fileHandler = IpFileHandler()
    
    ipComparator = IpComparator(fileHandler, ipRetriever)
    if ipComparator.IsIpAddressDifferent():
        print 'IP address is different'
        fileHandler.SaveIpInfo(ipComparator.GetNewIpAddress())

        mailer = SendMail(gmailUserName, gmailPassword, recipient, provider)
        mailer.Send(ipComparator.GetNewIpAddress())        
    else:
        print 'No change in IP address'

if __name__ == "__main__":
    main()
