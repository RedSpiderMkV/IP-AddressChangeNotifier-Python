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


#import tkMessageBox
#from IpRetrieverLib import IpRetriever
import time
from Mailer.SendMail import SendMail
from Mailer.SmtpProviders import SmtpProviders
from IpTracker.IpRetriever import IpRetriever
from IpTracker.IpFileHandler import IpFileHandler
from IpTracker.IpComparator import IpComparator

gmailUserName = "someone@gmail.com"
gmailPassword = "password"
recipient = "recipient@somewhere.com"

def main():
    ipRetriever = IpRetriever()
    fileHandler = IpFileHandler()
    
    ipComparator = IpComparator(fileHandler, ipRetriever)
    if ipComparator.IsIpAddressDifferent():
        print 'IP address is different'
        fileHandler.SaveIpInfo(ipComparator.GetNewIpAddress())
    else:
        print 'No change in IP address'

#    ipAddress = ipRetriever.GetIpAddress()
#    print 'Retrieved IP Address: ', ipAddress
#    
#    fileHandler = IpFileHandler()
#    #fileHandler.SaveIpInfo(ipAddress)
#    print 'IP Address In File: ', fileHandler.GetIpAddressFromFile()
#    
#    timestamp = fileHandler.GetIpUpdateDateFromFile()
#    if timestamp == None:
#        print 'No timestamp'
#    else:
#        print 'IP Address Timestamp: ', time.strftime(
#                                        fileHandler.DateTimeFormat, timestamp)

    #if ipRetriever.IpAddressChanged():
    #    mailer = SendMail(gmailUserName, gmailPassword, recipient, SmtpProviders.GMAIL)
    #    mailer.Send(ipRetriever.NewIp)

    #    tkMessageBox.showinfo(title="Ip Change", message="IP Address changed\nNew IP: " + ipRetriever.NewIp)

if __name__ == "__main__":
    main()
