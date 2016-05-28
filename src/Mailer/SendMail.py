#-------------------------------------------------------------------------------
# Name:        SendMail
# Purpose:     Send an email using SMTP
#
# Author:      RedSpiderMkV
#
# Created:     19/10/2015
# Copyright:   (c) RedSpiderMkV 2016
# Licence:     ..
#-------------------------------------------------------------------------------

import email
import smtplib

class SendMail:
    def __init__(self, userName, password, recipient, provider):
        self.recipient = recipient
        self.gmailUserName = userName
        self.gmailPassword = password
        self.__smtpProvider = provider

    def Send(self, newIp):
        msg = email.message_from_string('New IP: ' + newIp)
        msg['From'] = self.gmailUserName
        msg['To'] = self.recipient
        msg['Subject'] = 'IP Address Changed'

        try:
            session = smtplib.SMTP(self.__smtpProvider, 587)
            session.ehlo()
            session.starttls()
            session.login(self.gmailUserName, self.gmailPassword)
            session.sendmail(self.gmailUserName, self.recipient, msg.as_string())
            session.quit()
        except Exception, e:
            print(e)