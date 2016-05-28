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
from IpRetrieverLib import IpRetriever
from SendMail import SendMail
from SmtpProviders import SmtpProviders

gmailUserName = "someone@gmail.com"
gmailPassword = "password"
recipient = "recipient@somewhere.com"

def main():
    ipRetriever = IpRetriever(r'../')

    if ipRetriever.IpAddressChanged():
        mailer = SendMail(gmailUserName, gmailPassword, recipient, SmtpProviders.GMAIL)
        mailer.Send(ipRetriever.NewIp)

        tkMessageBox.showinfo(title="Ip Change", message="IP Address changed\nNew IP: " + ipRetriever.NewIp)

if __name__ == "__main__":
    main()
