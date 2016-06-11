#-------------------------------------------------------------------------------
# Name:        IpUpdateRunner.py
# Purpose:     Run the IP address update and notify process.
#
# Author:      RedSpiderMkV
#
# Created:     Sat Jun 11 23:42:23 2016
# Copyright:   (c) RedSpiderMkV 2016
#-------------------------------------------------------------------------------

from Mailer.SendMail import SendMail
from Mailer.SmtpProviderFactory import SmtpProviderFactory

class IpUpdateRunner:
    ''' Ip update runner class - does the IP check. '''
    
    def __init__(self, fileHandler, ipComparator):
        ''' Instantiate new update runner.
        
            Args:
                fileHandler: IpFileHandler object - used to read/write IP address.
                ipComparator: IpComparator object - used to compare IP address. '''
                
        self._fileHandler = fileHandler
        self._ipComparator = ipComparator
        
    def PerformIpCheckAndUpdate(self, userName, password, recipient):
        ''' Perform the IP check task.
        
            Args:
                userName: email sending user name as string.
                password: email account password as string.
                recipient: email recipient address as string. '''
                
        if self._ipComparator.IsIpAddressDifferent():
            print 'IP address is different'
    
            provider = SmtpProviderFactory.GetProvider(userName)
            
            if provider == None:
                print 'Error getting email provider'
                return
    
            mailer = SendMail(userName, password, recipient, provider)
            subject = 'IP Address Changed'
            message = 'New IP: ' + self._ipComparator.GetNewIpAddress()
            
            mailer.Send(subject, message)
            
            self._fileHandler.SaveIpInfo(self._ipComparator.GetNewIpAddress())
        else:
            print 'No change in IP address'
