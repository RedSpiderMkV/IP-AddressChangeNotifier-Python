#!usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:38:14 2014

@author: RedSpiderMkV
"""

from IpRetrieverLib import IpRetriever
from SendMail import SendMail

gmailUserName = "someone@gmail.com"
gmailPassword = "password"
recipient = "recipient@somewhere.com"

def main():
    ipRetriever = IpRetriever(r'../')

    if ipRetriever.IpAddressChanged():
        mailer = SendGMail(gmailUserName, gmailPassword, recipient)
        mailer.Send()

        tkMessageBox.showinfo(title="Ip Change", message="IP Address changed\nNew IP: " + self.response)

if __name__ == "__main__":
    main()