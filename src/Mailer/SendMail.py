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
        self.userName = userName
        self.passWord = password
        self._smtpProvider = provider

    def Send(self, subject, message):
        msg = email.message_from_string(message)
        msg['From'] = self.userName
        msg['To'] = self.recipient
        msg['Subject'] = subject

        try:
            session = smtplib.SMTP(self._smtpProvider, 587)
            session.ehlo()
            session.starttls()
            session.login(self.userName, self.passWord)
            session.sendmail(self.userName, self.recipient, msg.as_string())
            session.quit()
        except Exception, e:
            print(e)
