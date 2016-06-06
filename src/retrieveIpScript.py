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


import tkMessageBox
#from IpRetrieverLib import IpRetriever
from Mailer.SendMail import SendMail
from Mailer.SmtpProviders import SmtpProviders
from IpTracker.IpRetriever import IpRetriever

gmailUserName = "someone@gmail.com"
gmailPassword = "password"
recipient = "recipient@somewhere.com"

def main():
    ipRetriever = IpRetriever()
    print ipRetriever.GetIpAddress()

    #if ipRetriever.IpAddressChanged():
    #    mailer = SendMail(gmailUserName, gmailPassword, recipient, SmtpProviders.GMAIL)
    #    mailer.Send(ipRetriever.NewIp)

    #    tkMessageBox.showinfo(title="Ip Change", message="IP Address changed\nNew IP: " + ipRetriever.NewIp)

if __name__ == "__main__":
    main()
