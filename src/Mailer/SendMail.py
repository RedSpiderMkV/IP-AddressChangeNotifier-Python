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
    ''' Send an email message. '''
    
    def __init__(self, userName, password, recipient, provider):
        ''' Instantiate new email sending object.
        
            Args:
                userName: user name of account sending the email as string.
                password: account password as string.
                recipient: email recipient address as string.
                provider: smtp provider as string. '''
                
        self.recipient = recipient
        self.userName = userName
        self.passWord = password
        self._smtpProvider = provider

    def Send(self, subject, message):
        ''' Send an email message with specified subject end message.
        
            Args:
                subject: email subject as string.
                message: email message as string. '''
                
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
