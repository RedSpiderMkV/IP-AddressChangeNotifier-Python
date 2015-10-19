#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     19/10/2015
# Copyright:   (c) RedSpiderMkV 2015
# Licence:     ..
#-------------------------------------------------------------------------------

import smtplib

class SendGMail:
    def __init__(self, userName, password, recipient):
        self.recipient = recipient
        self.gmailUserName = userName
        self.gmailPassword = password

    def Send(self, newIp):
        headers = "\r\n".join(["from: " + self.gmailUserName,
                       "subject: " + "Ip Address Changed",
                       "to: " + self.recipient,
                       "mime-version: 1.0",
                       "content-type: text/html"])

        body_of_email = "New IP: " + newIp
        content = headers + "\r\n\r\n" + body_of_email

        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.ehlo()
            session.starttls()
            session.login(self.gmailUserName, self.gmailPassword)
            session.sendmail(self.gmailUserName, self.recipient, content)
        except Exception, e:
            print(e)