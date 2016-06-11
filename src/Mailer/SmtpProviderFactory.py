#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     Sat Jun 11 20:05:25 2016
# Copyright:   (c) RedSpiderMkV 2016
#-------------------------------------------------------------------------------

from SmtpProviders import SmtpProviders

class SmtpProviderFactory:
    @classmethod
    def GetProvider(self, userAccount):
        emailProvider = None
        
        try:
            emailProvider = userAccount.split('@')[1].split('.')[0]
        except IndexError:
            print 'Invalid email'
            return None

        outlook = ['hotmail', 'live', 'outlook']
        gmail = ['gmail', 'googlemail']
        yahoo = ['yahoo']
        
        if emailProvider in outlook:
            return SmtpProviders.OUTLOOK
        elif emailProvider in gmail:
            return SmtpProviders.GMAIL
        elif emailProvider in yahoo:
            return SmtpProviders.YAHOO
        
        return None
