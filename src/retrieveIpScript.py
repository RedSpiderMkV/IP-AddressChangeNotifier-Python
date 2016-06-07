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

gmailUserName = "someone@gmail.com"
gmailPassword = "password"
recipient = "recipient@somewhere.com"

def main():
    ipRetriever = IpRetriever()
    ipAddress = ipRetriever.GetIpAddress()
    print 'Retrieved IP Address: ', ipAddress
    
    fileHandler = IpFileHandler()
    fileHandler.SaveIpInfo(ipAddress)
    print 'IP Address In File: ', fileHandler.GetIpAddressFromFile()
    print 'IP Address Timestamp: ', time.strftime(fileHandler.DateTimeFormat,
                                      fileHandler.GetIpUpdateDateFromFile())

    #if ipRetriever.IpAddressChanged():
    #    mailer = SendMail(gmailUserName, gmailPassword, recipient, SmtpProviders.GMAIL)
    #    mailer.Send(ipRetriever.NewIp)

    #    tkMessageBox.showinfo(title="Ip Change", message="IP Address changed\nNew IP: " + ipRetriever.NewIp)

if __name__ == "__main__":
    main()
